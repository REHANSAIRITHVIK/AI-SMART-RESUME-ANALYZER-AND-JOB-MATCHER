from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from app.services.resume_parser import parse_resume

resume_bp = Blueprint('resume', __name__)

UPLOAD_FOLDER = 'uploads/resumes'


# ✅ THIS FIXES /resume PAGE
@resume_bp.route('/resume', methods=['GET'])
def resume_page():
    skills = session.get('skills', [])
    matched_jobs = session.get('matched_jobs', [])

    return render_template(
        'resume.html',
        skills=skills,
        matched_jobs=matched_jobs
    )


# ✅ UPLOAD + AI PROCESSING
@resume_bp.route('/upload_resume', methods=['POST'])
def upload_resume():
    file = request.files['resume']

    if file:
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        # AI Parsing
        result = parse_resume(path)

        session['skills'] = result['skills']

    return redirect(url_for('dashboard.dashboard'))