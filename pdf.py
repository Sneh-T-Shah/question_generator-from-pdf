from langchain.document_loaders import PDFMinerLoader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

def save_pdf(pdf_bytes, filename):
    """
    Function to save a PDF file to local storage.
    """
    with open(filename, "wb") as f:
        f.write(pdf_bytes)
        f.close()

def make_db_from_pdf(filename: str, openai_apikey: str):
    """
    Function to create a database from a PDF file.
    """
    loader = PDFMinerLoader(filename)
    transcript = loader.load()
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(transcript[0].page_content)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    os.environ["OPENAI_API_KEY"] = openai_apikey
    embeddings = OpenAIEmbeddings()
    print(embeddings)
    db = FAISS.from_documents(docs, embeddings)
    return db


def get_response_from_query(db, query, k=5):
    llm = OpenAI()
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])
    prompt = PromptTemplate(
        input_variables=["docs", "query"],
        template="""
        You are a helpful assistant that your task is to generate 3 questions of topic {query} and answers from the pdf file given.
        
        By searching the following data from pdf: {docs}
        The answers of question generated should be complete and from the pdf given and relevant to the topic.
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(docs=docs_page_content, query=query)
    
    return response

