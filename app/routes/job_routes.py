import json
import os
from flask import Blueprint, render_template, session

job_bp = Blueprint('jobs', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_jobs():
    with open(os.path.join(BASE_DIR, 'data', 'jobs.json')) as f:
        return json.load(f)


def simple_match(user_skills, job_skills):
    match_count = len(set(user_skills) & set(job_skills))
    return int((match_count / len(job_skills)) * 100) if job_skills else 0


@job_bp.route('/companies')
def companies():
    import json, os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    with open(os.path.join(BASE_DIR, 'data', 'companies.json')) as f:
        companies = json.load(f)

    return render_template('companies.html', companies=companies)


@job_bp.route('/jobs')
def jobs():
    jobs = load_jobs()

    if 'skills' in session:
        user_skills = session['skills']

        for job in jobs:
            job['match'] = simple_match(user_skills, job['skills'])

    return render_template('jobs.html', jobs=jobs)