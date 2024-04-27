from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel

class User(BaseModel):
    """User model for handling registration, login, and authentication"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)  # hash passwords

    def __init__(self, username, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password