# ChatGPT-like Conversational AI Web App  
A lightweight, open-source chatbot built using **Python**, **Flask**, and **Hugging Face Transformers**.  
This project replicates a ChatGPT-style chat interface and integrates an open-source Large Language Model (LLM) for generating human-like responses.

---

##  Features
- ChatGPT-style interface  
- Flask-based backend API  
- Open-source LLM using Hugging Face Transformers  
- Real-time chat functionality  
- Clean and responsive frontend  
- Customizable prompt system  
- Local model inference (no external API required)

---

##  Tech Stack

### **Frontend**
- HTML  
- CSS  
- JavaScript  

### **Backend**
- Python  
- Flask  

### **AI Model**
- Hugging Face Transformers  
- Torch  
- Tokenizers  

---

##  Project Structure
project/
│── app.py
│── requirements.txt
│── model/ # Downloaded model files here
│── static/
│ ├── style.css
│ └── script.js
│── templates/
└── index.html


---

## 🔧 Installation

Follow these steps to run the project on your system.

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-chatbot-project.git
cd your-chatbot-project

```
### **2. Create virtual environment and requirements.txt installation.**
```bash
python3 -m venv venv
```
#for wwindows
```
venv\Scripts\activate
```

# for linux\macOs
```
source venv/bin/activate

```
# install depedencies
```
pip install -r requirements.txt
```
## Run the bot
```
python app.py
```
#or
```
python3 app.py
```
