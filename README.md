# AI Resume Maker 🚀

An AI-powered Resume Builder that creates professional, ATS-friendly resumes using **LangChain**, **Retrieval-Augmented Generation (RAG)**, and modern LLM workflows. This project intelligently generates personalized resume content based on user skills, experience, projects, and job descriptions.

---

## ✨ Features

* 🧠 AI-generated resume summaries and bullet points
* 📄 ATS-friendly resume formatting
* 🔍 RAG-based retrieval for personalized content generation
* 🤖 LangChain-powered LLM pipelines
* 💼 Job-description-aware resume customization
* 🛠️ Skill extraction and optimization
* 📚 Context-aware project and experience generation
* 🌐 Easy-to-use web interface
* ⚡ Fast and scalable architecture

---

## 🧩 Tech Stack

### Frontend

* React.js / Next.js
* Tailwind CSS

### Backend

* Python
* FastAPI / Flask

### AI & NLP

* LangChain
* OpenAI / LLM APIs
* RAG (Retrieval-Augmented Generation)
* Vector Database (FAISS / ChromaDB)

### Database

* MongoDB / PostgreSQL

---

## 🧠 How It Works

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline to generate high-quality resumes.

### Workflow

1. User enters:

   * Skills
   * Experience
   * Education
   * Projects
   * Target job role

2. Resume data is embedded and stored in a vector database.

3. Relevant context is retrieved using semantic similarity search.

4. LangChain orchestrates:

   * Prompt templates
   * Retrieval chains
   * LLM responses

5. The AI generates:

   * Professional summaries
   * Work experience bullet points
   * Project descriptions
   * Skill recommendations

---

## 🏗️ Architecture

```text
User Input
    ↓
Frontend UI
    ↓
Backend API
    ↓
LangChain Pipeline
    ↓
Vector Database (FAISS/Chroma)
    ↓
RAG Retrieval
    ↓
LLM Generation
    ↓
Professional Resume Output
```

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-resume-maker.git
cd ai-resume-maker
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

### Run the Project

```bash
python app.py
```

or

```bash
uvicorn main:app --reload
```

---

## 📚 LangChain Components Used

* PromptTemplate
* LLMChain
* RetrievalQA
* Conversational Chains
* Memory Modules
* Embedding Models
* Document Loaders

---

## 🔍 RAG Implementation

The project uses **Retrieval-Augmented Generation** to improve resume quality and relevance.

### Why RAG?

* Reduces hallucinations
* Provides context-aware generation
* Improves job-role matching
* Generates realistic project descriptions
* Enhances ATS optimization

### Retrieval Flow

```text
Resume Data → Embeddings → Vector Store
                         ↓
                  Similarity Search
                         ↓
                  Retrieved Context
                         ↓
                     LLM Output
```

---

## 📸 Future Improvements

* PDF export support
* Multiple resume templates
* LinkedIn profile parsing
* AI interview preparation
* Cover letter generation
* Multi-language support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 🌟 Acknowledgements

* LangChain
* OpenAI
* FAISS
* ChromaDB
