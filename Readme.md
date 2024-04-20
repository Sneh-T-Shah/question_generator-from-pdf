# PDF to Questions and Answers Generator

A Python project that generates relevant questions and answers from a provided PDF file based on a given topic or query.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sneh-T-Shah/question_generator-from-pdf.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an OpenAI API key from https://openai.com/api/

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run pdf_streamlit.py
   ```

2. In the Streamlit app, upload a PDF file.
3. Enter a query or topic related to the PDF content.
4. Provide your OpenAI API key.
5. Click the "Submit" button.

The app will generate three relevant questions and answers based on the provided PDF file and query.

## Features

- Upload PDF files for processing.
- Generate relevant questions and answers based on a given topic or query.
- Utilizes the OpenAI Language Model for natural language processing.
- Saves the uploaded PDF file to local storage for processing.
- Creates a database from the PDF file using FAISS vector store.
- Performs similarity search on the database to retrieve relevant content.
- Generates questions and answers using the retrieved content and the provided query.
- Displays the generated questions and answers in the Streamlit app.

## Dependencies

- Python 3.7 or higher
- Streamlit
- LangChain
- OpenAI
- FAISS
- PDFMiner

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
