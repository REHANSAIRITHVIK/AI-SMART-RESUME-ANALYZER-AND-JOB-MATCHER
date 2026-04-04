import json
import os
from flask import Blueprint, render_template, request, session
from app.services.resume_parser import parse_resume
from app.services.job_matcher import match_jobs

dashboard_bp = Blueprint('dashboard', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_data():
    with open(os.path.join(BASE_DIR, 'data', 'jobs.json')) as f:
        jobs = json.load(f)

    with open(os.path.join(BASE_DIR, 'data', 'companies.json')) as f:
        companies = json.load(f)

    return jobs, companies


def simple_match(user_skills, job_skills):
    match_count = len(set(user_skills) & set(job_skills))
    return int((match_count / len(job_skills)) * 100) if job_skills else 0


@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    jobs, companies = load_data()
    matched_jobs = []

    if 'skills' in session:
        user_skills = session['skills']

        for job in jobs:
            match = simple_match(user_skills, job['skills'])
            if match > 30:
                job_copy = job.copy()
                job_copy['match'] = match
                matched_jobs.append(job_copy)

    return render_template(
        'dashboard.html',
        jobs=jobs,
        companies=companies,
        matched_jobs=matched_jobs
    )