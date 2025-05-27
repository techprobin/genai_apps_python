# genai_apps_python
Generative AI, LLM and Python
Together AI Open AI Compatibility bundle supporting GPT-4(4.1), mistral, Llama(3, 4, Maverick), Qwen/2.5, black-forest/FLUX/dev, sonic/2, m2-bert etc.
Chat with a Language Model, Streaming, Vision, Image Gen, TTS, Generating Vector Embeddings, Structured Outputs, Function Calling, Agents etc.
AI Code Interpreter (Python)

Run the requirements file with pip install to fulfill all installations requirements, or manually

# 📘 Company FAQ Chatbot – RAG Demo

This is a simple Retrieval-Augmented Generation (RAG) chatbot built using:

- OpenAI (GPT-4) / Together AI (various models including Mixtral/, Llama(3, 4, Maverick), Qwen/2.5, 
- LangChain
- FAISS (vector database)

## 🔧 How It Works

1. Loads sample FAQ documents.
2. Converts them into vector embeddings.
3. At runtime, retrieves relevant documents based on your question.
4. GPT-4 generates an answer using those documents.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
export TOGETHERAI_API_KEY = your_togetherai_api_key
python app.py
python app_together_open_compatibility.py

pip install -r requirements_openai.txt
#OPENAI_API_KEY = your_openai_api_key
python openai_app.py
```

## 🧠 Example

```
👤 You: What is the return policy?
🤖 Bot: You can return any item within 30 days of purchase.
```
