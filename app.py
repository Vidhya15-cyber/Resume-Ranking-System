import streamlit as st
import os
from utils import extract_text_from_pdf, rank_resumes

st.title("📄 Resume Ranking System for HR")
st.write("Upload a Job Description and multiple resumes (PDF) to get a ranked list.")

# Upload JD
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# Upload resumes
resume_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if jd_file and resume_files:
    jd_text = extract_text_from_pdf(jd_file)
    resume_texts = [extract_text_from_pdf(file) for file in resume_files]
    similarity_scores = rank_resumes(jd_text, resume_texts)

    ranked = sorted(zip(resume_files, similarity_scores), key=lambda x: x[1], reverse=True)

    st.subheader("📊 Ranked Resumes:")
    for idx, (file, score) in enumerate(ranked):
        st.write(f"{idx + 1}. {file.name} — Similarity Score: **{score:.2f}**")
