# LangChain RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot using LangChain and Streamlit. The chatbot can accept PDF files through a web interface and provide answers to user queries based on the content of those files.

## Project Structure

```
langchain-rag-chatbot
├── src
│   ├── main.py            # Entry point for the Streamlit application
│   ├── chatbot.py         # Contains the Chatbot class for processing queries
│   ├── document_loader.py  # Functions for loading and processing PDF files
│   ├── retriever.py       # Defines the Retriever class for information retrieval
│   └── config.py         # Configuration settings for the application
├── uploads                # Directory for temporarily storing uploaded PDF files
├── requirements.txt       # Lists project dependencies
└── README.md              # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd langchain-rag-chatbot
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit application by executing:
   ```bash
   streamlit run src/main.py
   ```

## Usage Guidelines

- Upload a PDF file using the provided interface.
- Enter your query in the input box.
- The chatbot will process the PDF and return relevant answers based on the content.

## Overview of Functionality

- **PDF Upload**: Users can upload PDF documents which are processed for text extraction.
- **Query Processing**: The chatbot uses LangChain's RAG capabilities to generate responses based on user queries.
- **Information Retrieval**: The system retrieves relevant information from the uploaded documents using vector embeddings and similarity search techniques.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.