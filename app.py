import streamlit as st
from core_logic import parse_resume, build_prompt, call_ai
import os

# --- UI SETTINGS ---
st.set_page_config(page_title="ResumeAI Pro", page_icon="🚀", layout="wide")

# Custom CSS for a clean "SaaS" Look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #003d7a; color: white; }
    .stTextInput>div>div>input { border-radius: 5px; }
    .header-text { color: #003d7a; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 ResumeAI Pro: Industry Architect")
st.markdown("Build a FAANG-ready, single-page LaTeX resume tailored to any Job Description.")

# Sidebar for API config
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Gemini API Key", type="password")
    if api_key: os.environ["GEMINI_API_KEY"] = api_key
    st.info("The output will be raw LaTeX code. Copy it into Overleaf.com to get your PDF.")

# --- INPUT SECTION ---
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📋 Step 1: Target Job")
    jd = st.text_area("Paste Job Description", height=250, placeholder="What job are you applying for?")
    
    st.subheader("📄 Step 2: Base Resume")
    resume_file = st.file_uploader("Upload Current Resume (PDF)", type=['pdf'])

with col2:
    st.subheader("👤 Step 3: Professional Profile")
    
    tab1, tab2, tab3 = st.tabs(["Personal Info", "Experience & Intern", "Coding & Honors"])
    
    with tab1:
        name = st.text_input("Full Name", placeholder="Harsh Gupta")
        email = st.text_input("Professional Email")
        linkedin = st.text_input("LinkedIn Profile Link")
        github = st.text_input("GitHub Profile Link")
        
    with tab2:
        internships = st.text_area("Internships (Details)", placeholder="Company, Role, and what you did...")
        experience = st.text_area("Other Experience", placeholder="Freelance, Societies, Part-time...")
        
    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            leetcode = st.text_input("LeetCode ID")
        with c2:
            solved = st.text_input("Problems Solved", placeholder="e.g. 500+")
        achievements = st.text_area("Achievements", placeholder="IICPC Regionalist, Hackathon Winner, etc.")

# --- GENERATION ---
st.markdown("---")
if st.button("✨ Architect My Tailored Resume"):
    if not jd or not resume_file or not api_key:
        st.error("Please provide JD, Resume File, and API Key.")
    else:
        with st.spinner("Analyzing data and generating professional LaTeX..."):
            try:
                base_text = parse_resume(resume_file)
                user_data = {
                    "name": name, "email": email, "linkedin": linkedin, "github": github,
                    "leetcode": leetcode, "solved": solved, "internships": internships,
                    "experience": experience, "achievements": achievements
                }
                
                prompt = build_prompt(jd, base_text, user_data)
                latex_code = call_ai(prompt)
                
                st.success("✅ Architecture Complete!")
                
                # Download and View
                st.download_button("📥 Download .tex File", data=latex_code, file_name="resume.tex")
                
                with st.expander("📄 View Generated Code (Copy to Overleaf)"):
                    st.code(latex_code, language="latex")
                    
            except Exception as e:
                st.error(f"Error: {e}")
