import os
from app.services.skill_extractor import extract_skills


def read_resume(file_path):
    text = ""

    try:
        with open(file_path, "r", errors="ignore") as f:
            text = f.read()
    except:
        text = ""

    return text


def parse_resume(file_path):
    text = read_resume(file_path)

    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills
    }