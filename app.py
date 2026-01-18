import streamlit as st

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store
from rag.qa_chain import create_qa_chain


st.set_page_config(
    page_title="EcoAssist 🌱",
    page_icon="🌍",
    layout="wide"
)

st.title("🌱 EcoAssist – AI Sustainability Assistant")
st.markdown(
    "Ask questions about **sustainability rules, waste management, energy conservation, and climate policies**."
)

@st.cache_resource
def load_rag_system():
    DOCS_PATH = "data/policies"

    docs = load_documents(DOCS_PATH)
    chunks = split_documents(docs)

    embeddings = get_embeddings()
    vector_store = create_vector_store(chunks, embeddings)

    qa_chain = create_qa_chain(vector_store)
    return qa_chain


qa_chain = load_rag_system()

question = st.text_input(
    "💬 Enter your sustainability-related question:",
    placeholder="e.g. How should electronic waste be disposed?"
)

# Generate Answer

if st.button("🔍 Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking... 🌿"):
            result = qa_chain(question)

        st.subheader("✅ Answer")
        st.write(result["result"])

        st.subheader("📄 Source Documents")
        for doc in result["source_documents"]:
            st.write("•", doc.metadata.get("source"))
