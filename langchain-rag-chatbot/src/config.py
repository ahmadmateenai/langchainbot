# Configuration settings for the LangChain RAG chatbot

# Model parameters
MODEL_NAME = "gpt-3.5-turbo"  # Specify the model to be used for generation
MAX_TOKENS = 150  # Maximum number of tokens for the response

# File paths
UPLOAD_FOLDER = "uploads/"  # Directory for storing uploaded PDF files
PDF_PROCESSING_PATH = "uploads/processed/"  # Directory for processed PDF files

# Other constants
SIMILARITY_THRESHOLD = 0.7  # Threshold for similarity in retrieval
DEFAULT_RESPONSE = "I'm sorry, I couldn't find an answer to your question."  # Default response when no relevant information is found