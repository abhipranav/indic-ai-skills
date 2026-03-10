---
name: indian-constitution
description: AI Lawyer powered by the Constitution of India. Query the Indian Constitution using RAG (Retrieval Augmented Generation) to get accurate, cite
[truncated]
 → ARTICLE_14: Equality before law
- "What are the fundamental duties?" → List all 11 duties from Part IV-A
- "Can the President declare emergency?" → Article 352, 356, 360 types
- "How is a bill passed?" → Article 107-108, 111 procedure
- "What is judicial review?" → Articles 32, 136, 226, 227 power
- "Can states levy GST?" → Article 246A, 366(12A) - GST Council

## Constitutional Hierarchy

### Parts of the Constitution
1. **Part I**: The Union and its Territory (Articles 1-4)
2. **Part II**: Citizenship (Articles 5-11)
3. **Part III**: Fundamental Rights (Articles 12-35)
4. **Part IV**: Directive Principles of State Policy (Articles 36-51)
5. **Part IVA**: Fundamental Duties (Article 51A)
6. **Part V**: The Union (Articles 52-151)
7. **Part VI**: The States (Articles 152-237)
8. **Part VII**: The States in Part B of First Schedule (Repealed)
9. **Part VIII**: The Union Territories (Articles 239-242)
10. **Part IX**: The Panchayats (Articles 243-243O)
11. **Part IXA**: The Municipalities (Articles 243P-243ZG)
12. **Part IXB**: The Co-operative Societies (Articles 243ZH-243ZT)
13. **Part X**: The Scheduled and Tribal Areas (Articles 244-244A)
14. **Part XI**: Relations between the Union and the States (Articles 245-263)
15. **Part XII**: Finance, Property, Contracts and Suits (Articles 264-300A)
16. **Part XIII**: Trade, Commerce and Intercourse (Articles 301-307)
17. **Part XIV**: Services under the Union and the States (Articles 308-323)
18. **Part XIVA**: Tribunals (Articles 323A-323B)
19. **Part XV**: Elections (Articles 324-329A)
20. **Part XVI**: Special Provisions (Articles 330-342)
21. **Part XVII**: Official Language (Articles 343-351)
22. **Part XVIII**: Emergency Provisions (Articles 352-360)
23. **Part XIX**: Miscellaneous (Articles 361-367)
24. **Part XX**: Amendment of the Constitution (Article 368)
25. **Part XXI**: Temporary, Transitional and Special Provisions (Articles 369-392)
26. **Part XXII**: Short Title, Commencement, Authoritative Text (Articles 393-395)

### Important Schedules
- **First Schedule**: Names of States and UTs
- **Second Schedule**: Salaries and allowances
- **Third Schedule**: Forms of Oaths
- **Fourth Schedule**: Allocation of seats in Rajya Sabha
- **Fifth Schedule**: Provisions for Scheduled Areas
- **Sixth Schedule**: Provisions for Tribal Areas
- **Seventh Schedule**: Union, State, Concurrent Lists
- **Eighth Schedule**: Official Languages (22 languages)
- **Ninth Schedule**: Laws protected from judicial review
- **Tenth Schedule**: Anti-defection provisions
- **Eleventh Schedule**: Panchayat powers
- **Twelfth Schedule**: Municipality powers

## Data Source

- **Document**: Constitution of India (as of July 2024)
- **Source**: https://cdnbbsr.s3waas.gov.in/
- **Pages**: 402
- **Chunks**: 1,726
- **Embedding Model**: all-MiniLM-L6-v2 (384 dimensions)
- **Vector Store**: ChromaDB
- **Chunk Size**: 1000 characters with 200 overlap

## Important Notes

1. **Not Legal Advice**: This skill provides constitutional information but is NOT a substitute for professional legal counsel.

2. **Updated as of 2024**: Contains amendments up to the 106th Constitutional Amendment Act, 2023.

3. **Citations**: All responses include relevant Article numbers for verification.

4. **Interpretation**: Constitutional interpretation varies; consult Supreme Court judgments for authoritative interpretation.

## Use Cases

### For Citizens
- Know your fundamental rights
- Understand voting procedures
- Learn about legal protections

### For Law Students
- Quick constitutional research
- Article cross-referencing
- Amendment tracking

### For Lawyers
- Draft legal arguments
- Find constitutional provisions
- Verify citations

### For UPSC/PSC Aspirants
- Constitutional studies
- Quick revision
- Article memorization

## Technical Details

### Embedding Model
- **Model**: all-MiniLM-L6-v2
- **Size**: ~80MB (much smaller than Gemma-300M)
- **Dimensions**: 384
- **Speed**: Fast CPU inference
- **Accuracy**: High quality for semantic search

### Retrieval Settings
- **Top-k**: 5 chunks per query
- **Similarity**: Cosine similarity
- **Chunk overlap**: 200 characters (for context continuity)

## Future Enhancements

- [ ] Add Supreme Court judgments
- [ ] Add legal commentary
- [ ] Add bare acts integration
- [ ] Add amendment history
- [ ] Add comparative constitutional law

---

**We the People of India** 🇮🇳  
*Created: March 2026*  
*Constitution Version: As of July 2024*
