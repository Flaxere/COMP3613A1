from App.database import db
from .user import User

class Applicant(User):
    __tablename__ = 'applicant'
    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120),nullable=False)
    phone_number = db.Column(db.String(120),nullable=False)
    email_address = db.Column(db.String(120),nullable=False)
    # applications = db.Relationship('Application', backref='applicant')
    applications = db.Relationship('Job', secondary = 'application', backref='applicants')

    __mapper_args__ = {
        'polymorphic_identity': 'applicant'
    }


    def __init__(self,username,password,first_name,last_name,phone_number,email_address):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

   
        

