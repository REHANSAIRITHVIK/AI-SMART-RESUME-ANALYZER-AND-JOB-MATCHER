import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    SECRET_KEY = "supersecretkey"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "resumes")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

    # AI Config
    ALLOWED_EXTENSIONS = {"txt", "pdf", "docx"}