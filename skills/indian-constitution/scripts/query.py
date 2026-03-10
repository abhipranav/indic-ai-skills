#!/usr/bin/env python3
"""
Indian Constitution RAG Query Tool
Ask questions about the Constitution of India and get accurate, cited answers.
"""

import os
import sys
import argparse
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "embeddings", "chroma_db")

def load_vectorstore():
    """Load the ChromaDB vector store with Constitution embeddings."""
    print("🔄 Loading Constitution embeddings...")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )
    
    print(f"✅ Loaded {vectorstore._collection.count()} constitutional chunks")
    return vectorstore

def query_constitution(vectorstore, question, k=5):
    """Query the Constitution and return relevant chunks."""
    print(f"\n🔍 Query: {question}")
    print("=" * 60)
    
    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(question, k=k)
    
    print(f"📚 Found {len(docs)} relevant constitutional provisions:\n")
    
    for i, doc in enumerate(docs, 1):
        print(f"--- Result {i} ---")
        # Extract page info if available
        content = doc.page_content[:800]  # Limit output
        print(content)
        print()
    
    return docs

def format_legal_response(docs, question):
    """Format a lawyer-style response from retrieved chunks."""
    print("\n" + "=" * 60)
    print("⚖️  CONSTITUTIONAL ANALYSIS")
    print("=" * 60)
    
    # Extract key information
    all_content = "\n\n".join([d.page_content for d in docs])
    
    # Look for Article references
    import re
    articles = re.findall(r'Article\s+\d+[A-Z]?', all_content, re.IGNORECASE)
    parts = re.findall(r'Part\s+[IVX]+', all_content, re.IGNORECASE)
    
    if articles:
        print(f"\n📜 Relevant Articles: {', '.join(sorted(set(articles)))}")
    if parts:
        print(f"📖 Constitutional Parts: {', '.join(sorted(set(parts)))}")
    
    print(f"\n📝 Answer to: \"{question}\"")
    print("-" * 60)
    
    # Summarize from top result
    if docs:
        top_content = docs[0].page_content[:500]
        print(top_content + "...")
    
    print("\n⚠️  Disclaimer: This is for informational purposes only.")
    print("   Consult a qualified legal professional for legal advice.")

def main():
    parser = argparse.ArgumentParser(
        description="Query the Constitution of India",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 query.py "What are fundamental rights?"
  python3 query.py "Can the President declare emergency?"
  python3 query.py "How is the Chief Justice appointed?"
  python3 query.py "What does Article 21 say?"
        """
    )
    parser.add_argument("question", help="Your constitutional question")
    parser.add_argument("-k", "--top-k", type=int, default=5, 
                        help="Number of results to return (default: 5)")
    parser.add_argument("--raw", action="store_true",
                        help="Show raw chunks without formatting")
    
    args = parser.parse_args()
    
    # Load vector store
    try:
        vectorstore = load_vectorstore()
    except Exception as e:
        print(f"❌ Error loading embeddings: {e}")
        print("   Make sure embeddings have been created first.")
        sys.exit(1)
    
    # Query
    try:
        docs = query_constitution(vectorstore, args.question, k=args.top_k)
        
        if not args.raw:
            format_legal_response(docs, args.question)
    except Exception as e:
        print(f"❌ Error querying: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
