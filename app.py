import streamlit as st
from utils.file_reader import process_unstructured_pdf
from utils.text_preprocessor import preprocess_text
from utils.faiss_indexer import add_to_index, get_relevant_context
from transformers import pipeline

# Initialize QA model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

st.title("Document Question-Answering AI")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])

if uploaded_file:
    # Process unstructured data
    data = process_unstructured_pdf(uploaded_file)

    # Combine extracted text
    text = data['text'] + "\n" + data['images_text']
    for table in data['tables']:
        text += "\n" + table.to_string()

    # Preprocess and index text
    preprocessed_text = preprocess_text(text)
    sentences, index = add_to_index(preprocessed_text)
    
    question = st.text_input("Ask a question:")
    if question:
        context = get_relevant_context(question, sentences, index)
        answer = qa_pipeline({'context': context, 'question': question})['answer']
        st.write("Answer:", answer)
