import streamlit as st
from chatbot import Chatbot

def main():
    st.title("LangChain RAG Chatbot")
    st.write("Upload a PDF file and ask your questions.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Save the uploaded file to the uploads directory
        with open(f'uploads/{uploaded_file.name}', "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success("File uploaded successfully!")

        # Initialize the chatbot
        chatbot = Chatbot(uploaded_file.name)

        # User input for queries
        user_query = st.text_input("Ask a question:")
        if st.button("Submit"):
            if user_query:
                response = chatbot.get_response(user_query)
                st.write("Response:", response)
            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()