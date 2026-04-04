from flask import Blueprint, render_template, redirect, url_for, request

app_bp = Blueprint('applications', __name__)

applications_data = []


# SHOW APPLICATIONS
@app_bp.route('/applications')
def applications():
    return render_template('applications.html', applications=applications_data)


# ✅ APPLY ROUTE
@app_bp.route('/apply', methods=['POST'])
def apply_job():
    company = request.form.get('company')
    role = request.form.get('role')
    ctc = request.form.get('ctc')

    applications_data.append({
        "company": company,
        "role": role,
        "status": "Applied",
        "ctc": ctc
    })

    return redirect(url_for('applications.applications'))