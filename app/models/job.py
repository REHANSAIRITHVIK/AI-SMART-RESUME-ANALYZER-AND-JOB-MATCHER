from app.extensions import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    skills = db.Column(db.Text)
    salary = db.Column(db.String(50))
    ctc = db.Column(db.String(50))
    vacancies = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    applications = db.relationship('Application', backref='job', lazy=True)

    def get_skills_list(self):
        return self.skills.split(',')

    def __repr__(self):
        return f"<Job {self.title}>"