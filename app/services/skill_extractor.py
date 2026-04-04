import re

# MASTER SKILLS DATABASE
SKILLS_DB = [
    "python", "flask", "django", "sql", "mysql",
    "html", "css", "javascript", "react",
    "machine learning", "ai", "data science",
    "aws", "azure", "cloud", "docker", "kubernetes",
    "linux", "networking", "cyber security",
    "testing", "automation", "figma", "ui", "ux",
    "blockchain", "solidity"
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


def extract_skills(text):
    text = clean_text(text)

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))