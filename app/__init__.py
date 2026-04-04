import os
from flask import Flask
from app.config import Config
from app.extensions import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Ensure folders exist
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), "../instance"), exist_ok=True)

    # Import Models (IMPORTANT)
    from app.models.user import User
    from app.models.company import Company
    from app.models.job import Job
    from app.models.application import Application
    from app.models.resume import Resume

    # Flask-Login User Loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.resume_routes import resume_bp
    from app.routes.job_routes import job_bp
    from app.routes.application_routes import app_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(app_bp)

    # Default Route
    @app.route("/")
    def home():
        from flask import redirect, url_for
        return redirect(url_for("auth.login"))

    return app