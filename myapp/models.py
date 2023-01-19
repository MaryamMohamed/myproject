#for our models (Department and Employee) deal with db
from App import db

class Department(db.Model):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(300), unique=True, nullable=False)
    employees = db.relationship("Employee", backref='department')

    def __init__(self, name):
       self.name = name


class Title(db.Model):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(300), nullable=False)
    employees = db.relationship("Employee", backref='title')

    def __init__(self, name):
       self.name = name



class Employee(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(300), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, name, years_of_experience, department_id, title_id, salary):
       self.name = name
       self.years_of_experience = years_of_experience
       self.title_id = title_id
       self.department_id = department_id
       self.salary = salary
       