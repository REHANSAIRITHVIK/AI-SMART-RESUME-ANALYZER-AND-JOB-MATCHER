from app.extensions import db


class Resume(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200))
    extracted_skills = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def get_skills(self):
        return self.extracted_skills.split(',') if self.extracted_skills else []

    def __repr__(self):
        return f"<Resume {self.filename}>"