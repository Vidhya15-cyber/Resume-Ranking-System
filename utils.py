import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def rank_resumes(job_desc_text, resume_texts):
    texts = [job_desc_text] + resume_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(texts)
    similarities = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    return similarities
