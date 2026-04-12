import os
from app import create_app

# Create Flask app instance
app = create_app()

# Ensure required folders exist (important for deployment)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "resumes")
INSTANCE_FOLDER = os.path.join(BASE_DIR, "instance")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INSTANCE_FOLDER, exist_ok=True)


# Optional: Create database automatically on startup (safe for SQLite)
from app.extensions import db

with app.app_context():
    db.create_all()


# Entry point for WSGI servers (Gunicorn, uWSGI, etc.)
if __name__ == "__main__":
    app.run()