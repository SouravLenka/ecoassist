🌱 EcoAssist – AI-Powered Sustainability Assistant

EcoAssist is an AI-powered sustainability awareness assistant built using Retrieval-Augmented Generation (RAG) and Streamlit.
It helps users easily understand sustainability policies, waste management rules, energy conservation guidelines, and climate action practices by answering questions directly from trusted documents.

This project was developed as part of an AI for Sustainability Virtual Internship, with a strong focus on responsible AI, real-world relevance, and meaningful impact.

📌 Problem Statement

Many sustainability rules and environmental policies already exist, but they are often:

Stored in long PDF documents

Difficult for students and citizens to understand

Hard to search or interpret quickly

As a result, awareness and correct implementation of sustainable practices remain low.

❓ Key Question

How can AI be used to make sustainability policies more accessible, understandable, and actionable for everyone?

💡 Solution Overview

EcoAssist solves this problem using Retrieval-Augmented Generation (RAG):

Sustainability documents are processed and converted into embeddings

Relevant information is retrieved using vector similarity search

An AI model generates answers only from the retrieved document content

Source documents are displayed to ensure transparency

This approach ensures:

Fact-based responses

No hallucinations

Responsible and explainable AI usage

🎯 SDG Alignment

Primary SDG:

SDG 12 – Responsible Consumption and Production

Secondary SDGs:

SDG 11 – Sustainable Cities and Communities

SDG 13 – Climate Action

🧠 Key Features

📄 PDF-based sustainability knowledge system

🔍 Retrieval-Augmented Generation (RAG)

💬 Natural language question answering

📌 Source-based answers (Responsible AI)

🌍 Sustainability-focused use cases

🖥️ Interactive Streamlit web interface

🛠️ Tech Stack

Programming Language: Python

Frontend: Streamlit

AI Model: FLAN-T5 (Hugging Face Transformers)

Embeddings: Sentence Transformers

Vector Database: FAISS

Libraries & Tools:

LangChain

Transformers

PyPDF

Streamlit

🚀 How It Works (RAG Pipeline)

Sustainability PDFs are loaded into the system

Documents are split into smaller text chunks

Chunks are converted into vector embeddings

Embeddings are stored in a FAISS vector database

User asks a question

Relevant chunks are retrieved using similarity search

The AI generates an answer using only retrieved content

Source documents are shown for transparency

🖥️ Running the Application
1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run the Streamlit App

python -m streamlit run app.py

🧪 Sample Questions

How should electronic waste be disposed?

What are the rules for waste segregation?

What is considered hazardous waste?

How can energy be conserved?

What actions help reduce carbon footprint?
