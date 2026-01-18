from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store

DOCS_PATH = "data/policies"

docs = load_documents(DOCS_PATH)
print(f"Loaded {len(docs)} documents")

chunks = split_documents(docs)
print(f"Created {len(chunks)} chunks")

embeddings = get_embeddings()
vector_store = create_vector_store(chunks, embeddings)

print("Vector store created successfully ✅")
