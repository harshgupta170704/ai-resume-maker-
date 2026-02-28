import os
import re
import pdfplumber
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(override=True)

def get_working_model():
    """Dynamically finds a working model to prevent 404s."""
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ['models/gemini-1.5-flash-latest', 'models/gemini-1.5-flash', 'models/gemini-pro']
        for p in priority:
            if p in available: return p
        return available[0]
    except:
        return "gemini-1.5-flash"

def parse_resume(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    return file.getvalue().decode("utf-8", errors="ignore")

def build_prompt(jd, resume_text, data):
    # Professional FAANG-style LaTeX Template
    template = r"""
\documentclass[10pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fontawesome5}
\usepackage{geometry}

\geometry{left=0.4in, top=0.4in, right=0.4in, bottom=0.4in}
\definecolor{primary}{HTML}{003d7a}

\titleformat{\section}{\vspace{-4pt}\scshape\raggedright\large\bfseries\color{primary}}{}{0em}{}[\color{primary}\titlerule \vspace{-5pt}]

\newcommand{\resumeItem}[1]{\item\small{#1 \vspace{-2pt}}}
\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\begin{document}
% AI WILL GENERATE CONTENT HERE
\end{document}
"""

    prompt = f"""
    You are a Senior Technical Recruiter. Create a STUNNING 1-page LaTeX resume.
    
    JD: {jd}
    Old Resume: {resume_text}
    
    CANDIDATE DATA TO INTEGRATE:
    - Name: {data['name']}
    - Email: {data['email']} | GitHub: {data['github']} | LinkedIn: {data['linkedin']}
    - LeetCode: {data['leetcode']} ({data['solved']} solved)
    - Internships: {data['internships']}
    - Experience: {data['experience']}
    - Achievements: {data['achievements']}
    
    STRICT RULES:
    1. Output ONLY valid LaTeX code. No markdown code blocks.
    2. Ensure the resume fits ON ONE PAGE only.
    3. Use the Faang-style template provided.
    4. Highlight competitive programming and internships heavily.
    5. Quantify bullets (e.g. "Improved latency by 30%").
    
    LATEX TEMPLATE:
    {template}
    """
    return prompt

def call_ai(prompt):
    model = genai.GenerativeModel(get_working_model())
    response = model.generate_content(prompt)
    clean = re.sub(r"^```(?:latex)?\s*", "", response.text, flags=re.MULTILINE)
    return re.sub(r"^```\s*", "", clean, flags=re.MULTILINE).strip()
