from app.extensions import db


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    industry = db.Column(db.String(100))
    location = db.Column(db.String(100))
    logo = db.Column(db.String(200))

    jobs = db.relationship('Job', backref='company', lazy=True)

    def __repr__(self):
        return f"<Company {self.name}>"