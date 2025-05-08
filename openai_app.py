import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv('openai_config.env')

# 1. Load documents
loader = TextLoader("documents/faq.txt")
docs = loader.load()

# 2. Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)

# 3. Create embeddings & FAISS index
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embeddings)

# 4. Build retriever and QA chain
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4.1"),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# 5. Ask user for query
print("📘 Company FAQ Chatbot. Ask a question or type 'exit'.\n")
while True:
    query = input("👤 You: ")
    if query.lower() in ["exit", "quit", "bye"]:
        break
    result = qa_chain({"query": query})
    print("\n🤖 Bot:", result["result"], "\n") 
