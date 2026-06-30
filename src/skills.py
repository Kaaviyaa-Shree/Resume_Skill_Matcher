def extract_skills(resume, jd):
    resume_words = set(resume.split())
    jd_words = set(jd.split())

    matched_skills = resume_words.intersection(jd_words)
    missing_skills = jd_words.difference(resume_words)

    return list(matched_skills), list(missing_skills)