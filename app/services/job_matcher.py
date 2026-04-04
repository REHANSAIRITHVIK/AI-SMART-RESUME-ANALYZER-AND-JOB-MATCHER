def calculate_match(user_skills, job_skills):
    if not job_skills:
        return 0

    user_skills = set([s.lower() for s in user_skills])
    job_skills = set([s.lower() for s in job_skills])

    matched = user_skills.intersection(job_skills)

    score = (len(matched) / len(job_skills)) * 100

    return int(score)


def match_jobs(user_skills, jobs):
    matched_jobs = []

    for job in jobs:
        job_skills = job.get("skills", [])

        match_score = calculate_match(user_skills, job_skills)

        if match_score > 30:
            job_copy = job.copy()
            job_copy["match"] = match_score
            matched_jobs.append(job_copy)

    # SORT BY BEST MATCH
    matched_jobs = sorted(matched_jobs, key=lambda x: x["match"], reverse=True)

    return matched_jobs