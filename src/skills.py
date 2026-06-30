from src.skill_database import SKILLS

def extract_skills(resume, jd):
    resume_skills = {skill for skill in SKILLS if skill in resume}
    jd_skills = {skill for skill in SKILLS if skill in jd}

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    return sorted(matched_skills), sorted(missing_skills)