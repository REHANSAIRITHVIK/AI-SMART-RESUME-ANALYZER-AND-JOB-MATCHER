from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# TEMP STORAGE (replace with DB later)
users = []

@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        for user in users:
            if user['email'] == email and check_password_hash(user['password'], password):
                session['user'] = user['name']
                return redirect(url_for('dashboard.dashboard'))

        flash("Invalid Credentials")

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        users.append({
            "name": name,
            "email": email,
            "password": password
        })

        flash("Registered Successfully!")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))