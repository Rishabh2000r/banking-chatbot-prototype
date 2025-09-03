# 💡 Banking Chatbot Prototype  

A simple chatbot prototype using NLP + retrieval for answering banking-related FAQs.  

---

## 📦 Features
- Mock dataset with common banking questions and answers  
- Sentence transformer model (Hugging Face) for semantic similarity search  
- Flask-based API endpoint to query the bot  
- Basic command-line interface for testing  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Rishabh2000r/banking-chatbot-prototype.git
cd banking-chatbot-prototype
```

### 2. Setup a virtual environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

The Flask server will start at `http://localhost:5000`.

---

## 🔍 How to Use

**Option A: Via API (curl example)**
```bash
curl -X POST "http://127.0.0.1:5000/ask" -H "Content-Type: application/json" -d '{"query": "How do I open an account?"}'
```

**Option B: Command-line interface**
Run `python chatbot.py` and type your question (type `exit` to quit).

---

## 📦 Technologies Used
- Python 3.x  
- Flask (for API)  
- Hugging Face Transformers + Sentence Transformers (NLP model)  

---

## 📝 Notes
- This is a **prototype**; no real banking APIs or compliance checks are integrated.  
- For production use, expand with proper authentication, error handling, and database storage.

---

> 🔧 Want to improve this? Add more FAQs, try different models, or build a web interface!  

--- 

💬 Feel free to fork, contribute, or suggest improvements.