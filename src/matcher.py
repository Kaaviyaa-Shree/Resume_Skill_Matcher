def calculate_match_percentage(matched_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0

    percentage = (len(matched_skills) / len(jd_skills)) * 100
    return round(percentage, 2)