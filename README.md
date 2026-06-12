# 🌿 Arogya AI

### Multilingual Healthcare Assistant for Rural Communities

Arogya AI is an AI-powered healthcare assistant designed to provide reliable and accessible health information for rural communities. The system combines WHO medical documents, Retrieval-Augmented Generation (RAG), medical utility tools, and Groq AI to deliver informative responses in multiple languages.

---

# 📌 Problem Statement

People living in rural areas often face challenges in accessing reliable healthcare information. Internet connectivity, language barriers, and lack of awareness can make it difficult to obtain trusted medical guidance.

Arogya AI addresses this challenge by providing:

* Easy-to-understand healthcare information
* Support for regional languages
* WHO document-based responses
* Built-in medical calculators and utilities
* AI-powered fallback responses

---

# 🚀 Features

## 📚 WHO Document-Based Question Answering

* Upload WHO PDF documents.
* Generate embeddings automatically.
* Retrieve relevant information using FAISS vector search.
* Answer questions based on WHO content.

---

## ⚕ Built-in Medical Tools

The application includes ten healthcare utility tools:

### 1. BMI Calculator

Calculates Body Mass Index from weight and height.

### 2. Blood Pressure Classification

Classifies blood pressure levels.

### 3. Diabetes Risk Information

Provides common diabetes risk factors.

### 4. Symptom Checker

Performs basic symptom-based guidance.

### 5. Drug Information

Provides information about common medicines.

### 6. Heart Rate Analyzer

Checks whether heart rate is normal.

### 7. Daily Water Intake Recommendation

Suggests recommended water consumption.

### 8. Daily Calorie Information

Provides average calorie requirements.

### 9. Pregnancy BMI Guidance

Offers general pregnancy BMI recommendations.

### 10. Temperature Checker

Detects possible fever conditions.

---

## 🤖 Groq AI Fallback

If information is unavailable in:

1. WHO documents
2. Medical tools

the application automatically uses Groq AI to provide general healthcare information.

---

## 🌍 Multilingual Support

Users can ask questions in different languages:

* English
* Telugu
* Hindi
* Tamil

The chatbot responds in the same language used by the user.

---

## 🔊 Text-to-Speech Support

Users can listen to generated responses using speech synthesis.

---

## 📄 PDF Upload Support

Users can upload WHO PDF documents directly from the interface and create a vector database without modifying the source code.

---

# 🧠 System Workflow

```text
User Question
      ↓
WHO PDF Retrieval (RAG)
      ↓
Medical Tools
      ↓
Groq AI Fallback
      ↓
Final Response
```

---

# 🛠 Technology Stack

## Frontend

* Streamlit

## AI & LLM

* Groq API
* Llama 3.1 8B Instant

## RAG Framework

* LangChain

## Vector Database

* FAISS

## Embeddings

* HuggingFace Sentence Transformers

## PDF Processing

* PyPDFDirectoryLoader
* RecursiveCharacterTextSplitter

---

# 📂 Project Structure

```text
Health_Rag/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── assets/
│   ├── logo.png
│   └── styles.css
│
├── data/
│   └── documents/
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── retriever.py
│   ├── rag_chain.py
│   └── llm.py
│
├── tools/
│   └── medical_tools.py
│
├── utils/
│   ├── helper.py
│   └── ui_components.py
│
└── vectorstore/
```

---

# ⚙ Installation

### Clone the repository

```bash
git clone <repository-url>
cd Health_Rag
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 💡 Example Questions

### WHO Document Questions

* What are symptoms of diabetes?
* What causes malaria?
* How can dengue be prevented?

### Medical Tool Questions

* Calculate BMI for 70 kg and 1.75 m
* My BP is 150/95
* Heart rate is 110
* Daily water intake

### Multilingual Questions

**Telugu**

* డెంగ్యూ లక్షణాలు ఏమిటి?

**Hindi**

* डायबिटीज के लक्षण क्या हैं?

**Tamil**

* காய்ச்சலின் அறிகுறிகள் என்ன?

---

# ⚠ Disclaimer

This project provides educational healthcare information only.

It is not intended to diagnose diseases, prescribe medications, or replace professional medical advice.

For medical emergencies, users should consult qualified healthcare professionals.

---

# 👨‍💻 Author

### Kurakula Anuhya

**Arogya AI – Multilingual Healthcare Assistant for Rural Communities**
