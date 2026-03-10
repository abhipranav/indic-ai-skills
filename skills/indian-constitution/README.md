# Indian Constitution Lawyer Skill 🇮🇳

> AI-powered legal assistant based on the Constitution of India

⚖️ Ask questions about the Indian Constitution and get accurate, cited answers using RAG (Retrieval Augmented Generation).

## Quick Start

```bash
# Query the Constitution
cd /home/workspace/indic-ai-skills/skills/indian-constitution
python3 scripts/query.py "What are fundamental rights?"

# Get more results
python3 scripts/query.py "Can President declare emergency?" -k 10

# Show raw chunks
python3 scripts/query.py "What does Article 21 say?" --raw
```

## Example Queries

| Question | Article Coverage |
|----------|------------------|
| "What are fundamental rights?" | Articles 12-35 |
| "Right to equality" | Article 14-18 |
| "Freedom of speech" | Article 19 |
| "Can President declare emergency?" | Articles 352, 356, 360 |
| "How are judges appointed?" | Articles 124, 217 |
| "What is GST Council?" | Article 246A, 366(12A) |

## Data Stats

- 📄 **Pages**: 402 (full Constitution)
- 🧩 **Chunks**: 1,726
- 📐 **Embeddings**: 384 dimensions
- 🤖 **Model**: all-MiniLM-L6-v2 (~80MB)
- 💾 **Database**: ChromaDB

## Structure

```
indian-constitution/
├── data/
│   ├── constitution-of-india.pdf    # Original PDF
│   └── constitution-text.txt      # Extracted text
├── embeddings/
│   └── chroma_db/                   # Vector database
├── scripts/
│   └── query.py                    # Query tool
├── references/
│   └── README.md                   # Article reference
└── SKILL.md                        # Full documentation
```

## Technical Details

- **Chunk Size**: 1000 characters
- **Overlap**: 200 characters
- **Similarity**: Cosine
- **Retriever**: Top-5 semantic search

## ⚠️ Disclaimer

This tool provides constitutional information for educational purposes. It is **NOT** a substitute for professional legal advice. Always consult a qualified lawyer for legal matters.

**We the People of India** 🇮🇳
