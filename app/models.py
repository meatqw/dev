from flask_login import UserMixin

from app import db, manager
from datetime import datetime, timedelta

# DB Model Applications
class Applications(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    email = db.Column(db.String(200), primary_key=True)
    phone = db.Column(db.String(200), primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.now())

    
class UserAdmin(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    tg_id = db.Column(db.String(200), primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    

@manager.user_loader
def load_user(user_id):
    return UserAdmin.query.get(user_id)