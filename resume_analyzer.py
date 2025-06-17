import streamlit as st
import PyPDF2
import nltk
import os
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Data Science Skill Keywords
data_science_skills = [
    "python", "machine learning", "deep learning", "data analysis",
    "pandas", "numpy", "sql", "statistics", "nlp", "regression",
    "classification", "clustering", "tensorflow", "keras",
    "pytorch", "data visualization", "matplotlib", "seaborn",
    "big data", "hadoop", "spark", "scikit-learn"
]

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Read PDF content
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Resume Text:")
    st.write(text)

    # Tokenize and analyze
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation

    # Skill Analysis
    matched_skills = []
    missing_skills = []

    for skill in data_science_skills:
        if skill in tokens:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    st.subheader("✅ Skills Found:")
    st.write(matched_skills)

    st.subheader("⚠ Skills Missing (Consider Adding):")
    st.write(missing_skills)
