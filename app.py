from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocessing import clean_text
import streamlit as st
from src.skills import extract_skills
st.set_page_config(page_title="Resume Skill Matcher", layout="centered")
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main content card */
    .block-container {
        background: rgba(255, 255, 255, 0.18); /* MORE contrast */
        backdrop-filter: blur(10px);
        padding: 2.5rem;   /* reduced padding */
        border-radius: 20px;
        max-width: 1100px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.45);
    }

    /* Main title */
    h1 {
        color: #ffffff;
        text-align: center;
        font-weight: 700;
    }

    /* Subheadings */
    h2, h3 {
        color: #f1f1f1;
        font-weight: 600;
    }

    /* Paragraphs & labels */
    p, label, span {
        color: #eaeaea !important;
        font-size: 16px;
    }

    /* Text areas */
    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 14px;
    }

    /* Button */
    button {
        background: linear-gradient(90deg, #ff512f, #dd2476) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.6em 1.6em !important;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 14px rgba(0,0,0,0.35);
    }

    /* Metric container */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        color: #000000;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.35);
        text-align: center;
    }

    /* Metric label */
    div[data-testid="metric-container"] label {
        color: #444 !important;
        font-weight: 600;
    }

    /* Success & error boxes */
    .stAlert {
        border-radius: 15px;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Resume Skill Matcher")
st.write(
    """
    Paste your resume and job description below, 
    then click the 🔍 button to check your skill match and missing skills.
    """
)
st.write("---")  # horizontal line for separation
col1, col2 = st.columns(2)
with col1:
    resume_text = st.text_area(
        "🧾 Resume Text",
        height=150,
        placeholder="Paste your resume text here"
        )

with col2:
    jd_text = st.text_area(
        "📌 Job Description",
        height=150,
        placeholder="Paste the job description here"
        )
if st.button("🔍 Check Match"):
    if resume_text and jd_text:
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)
        #st.subheader("Cleaned Text Preview")
        #st.write("Resume:", clean_resume[:300])
        #st.write("Job Description:", clean_jd[:300])
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([clean_resume, clean_jd])
        #st.write("TF-IDF shape:", tfidf_matrix.shape)
        similarity_score = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]
        match_percentage = round(similarity_score * 100, 2)
        st.metric(label="🔹 Skill Match Percentage", value=f"{match_percentage}%")
        matched_skills, missing_skills = extract_skills(clean_resume, clean_jd)
        st.subheader("Skill Analysis")
        st.write("### ✅ Matched Skills")
        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.info("No matched skills found.")

        st.write("### ❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills!")
    else:
        st.warning("Please paste both Resume and Job Description.")

