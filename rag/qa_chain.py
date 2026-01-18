from transformers import pipeline


def create_qa_chain(vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    qa_pipeline = pipeline(
        task="text2text-generation",
        model="google/flan-t5-base",
        max_length=256
    )

    def ask_question(query: str):
        docs = retriever.invoke(query)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question using ONLY the context below.
        If the answer is not present, say "Information not available in the document."

        Context:
        {context}

        Question:
        {query}
        """

        response = qa_pipeline(prompt)[0]["generated_text"]

        return {
            "result": response,
            "source_documents": docs
        }

    return ask_question
