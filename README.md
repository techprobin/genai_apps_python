# GenAI Apps with Python  
🚀 **Generative AI, LLM Compatibility & Python Implementations**

## 📌 Overview  
This repository enables **Generative AI applications** using various **LLM models** via **Together AI, OpenAI, and other providers**.

### Key Features  
- **Multi-Model Support**: GPT-4 (4.1), Mistral, Llama (3, 4, Maverick), Qwen/2.5, Black-Forest FLUX, Sonic 2, M2-BERT  
- **AI Chatbot & Streaming**: Interactive chat with real-time response generation  
- **Vision & Image Generation**: AI-powered image processing and text-to-image conversion  
- **TTS & Structured Outputs**: Converts text into speech and generates formatted responses  
- **Vector Embeddings & Retrieval**: Efficient data processing for **Retrieval-Augmented Generation (RAG)**  
- **Function Calling & AI Agents**: Supports structured AI workflows  

---

## 🛠 How It Works  
This repository includes a **RAG-based AI chatbot** that extracts answers from FAQ documents by:  
1. **Loading Documents** 📄 – Sample FAQ files are converted into vector embeddings.  
2. **Retrieving Relevant Data** 🔍 – When queried, the system finds the most relevant document.  
3. **Generating AI-Powered Responses** 🤖 – Uses **GPT-4 and other LLMs** to formulate contextual answers.  

---

## 🔧 Installation & Setup  

### Prerequisites  
Ensure you have:  
- **Python 3.8+**  
- **Required dependencies** (installable via `requirements.txt`)  
- **API keys** (for Together AI / OpenAI access)  

### Installation Steps  
```bash
git clone https://github.com/techprobin/genai_apps_python.git  
cd genai_apps_python  
pip install -r requirements.txt  
```  

## 🚀 Running the AI Chatbot  
### Using Together AI  
```bash
export TOGETHERAI_API_KEY=your_togetherai_api_key  
python app_together_open_compatibility.py
```  
### Using OpenAI  
```bash
pip install -r requirements_openai.txt  
export OPENAI_API_KEY=your_openai_api_key  
python openai_app.py
```  
## 📂 Folder Structure  
### local  
/genai_apps_python  
│── src/                # Main Python source files  
│── models/             # Pre-trained AI models  
│── datasets/           # Sample FAQ documents  
│── requirements.txt    # Dependency list  
│── docs/               # Documentation & usage guides

## 💡 Example Chat Session  
👤 User: What is the return policy?  
🤖 AI Bot: You can return any item within 30 days of purchase.

## 📢 Contributions  
- ✅ **Fork this repo** and submit PRs for improvements.  
- ✅ **Feature requests** are welcome via Issues.  
- ✅ **Join discussions** on AI model integrations.  
- ✅ **Follow me** and **star this repo**, along with more repositories of mine.  
- ✅ **Like, Share, and Subscribe** for timely notifications and updates.  
- ✅ **Sponsor me on [Patreon](https://patreon.com/ppgen)** to support more such wonderful work and future developments.  

______________________________________________________________________________________________________________________________________

---  
### Archived Details

### RE-READ with details:

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
