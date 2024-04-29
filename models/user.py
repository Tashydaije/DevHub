from sqlalchemy import Column, String, Integer, DateTime
from models.base_model import BaseModel
from datetime import datetime
from flask_bcrypt import Bcrypt

class User(BaseModel):
    """User model for handling registration, login, and authentication"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)  # hash passwords
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, username, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.hash_password(password)
    
    def hash_password(self, password):
        bcrypt = Bcrypt()
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def json(self):
    # Return a dictionary representation of the user (excluding sensitive fields)
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email
        }