from app.extensions import db


class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))

    status = db.Column(db.String(50), default="Applied")

    def __repr__(self):
        return f"<Application User:{self.user_id} Job:{self.job_id}>"