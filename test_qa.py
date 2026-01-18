from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store
from rag.qa_chain import create_qa_chain

DOCS_PATH = "data/policies"

# Load and prepare documents
docs = load_documents(DOCS_PATH)
chunks = split_documents(docs)

# Create vector store
embeddings = get_embeddings()
vector_store = create_vector_store(chunks, embeddings)

# Create QA chain
qa_chain = create_qa_chain(vector_store)

# Ask a test question
query = "How should electronic waste be disposed?"
result = qa_chain(query)

print("\nQUESTION:", query)
print("\nANSWER:", result["result"])
print("\nSOURCES:")
for doc in result["source_documents"]:
    print("-", doc.metadata.get("source"))
