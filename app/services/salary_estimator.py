def estimate_salary(skills):
    base_salary = 10  # LPA

    skill_bonus = {
        "python": 8,
        "machine learning": 6,
        "ai": 10,
        "cloud": 9,
        "aws": 8,
        "docker": 7,
        "kubernetes": 5,
        "react": 7,
        "blockchain": 5,
        "cyber security": 9
        "AI ML": 8
    }

    total = base_salary

    for skill in skills:
        if skill in skill_bonus:
            total += skill_bonus[skill]

    if total > 25:
        total = 25  # cap

    return f"₹{total} LPA"


def estimate_ctc(salary):
    # Simple logic: CTC = salary + 20%
    value = int(salary.replace("₹", "").replace(" LPA", ""))
    ctc = int(value * 1.2)

    return f"₹{ctc} LPA"