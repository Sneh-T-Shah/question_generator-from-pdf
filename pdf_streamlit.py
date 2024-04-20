import streamlit as st
import pdf as pdfs 
import os

st.title("PDF to Questions and Answers Generator")
# File uploader widget

with st.form(key='my_form'):
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    query = st.text_area(
        label="Enter any content to generate questions and answers from the PDF file.",
        max_chars=100,
        key="query"
        )
    openai_api_key = st.text_input(
        label="OpenAI API Key",
        key="langchain_search_api_key_openai",
        max_chars=100,
        type="password"
        )
    submit_button = st.form_submit_button(label='Submit')


if uploaded_file is not None:
    st.write("You've uploaded the following PDF file:")
    st.write(uploaded_file.name)

    # Display the contents of the file
    pdf_contents = uploaded_file.read()

    # Save the uploaded PDF file to local storage
    pdfs.save_pdf(pdf_contents, uploaded_file.name)
    st.write("PDF saved successfully.")
    db = pdfs.make_db_from_pdf(uploaded_file.name,openai_api_key)
    st.write("Database created successfully.")
    response = pdfs.get_response_from_query(db, query)
    if response is None:
        response = "No response found."
    st.subheader("Here is the list of generated questions and answers:")
    st.write(response, width=85)
    os.remove(uploaded_file.name)