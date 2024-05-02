from sqlalchemy import Column, Integer, ForeignKey, String
from .base_model import BaseModel

class Account(BaseModel):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    platform_id = Column(Integer, ForeignKey('platform.id'), nullable=False)
    access_token = Column(String(255))
    refresh_token = Column(String(255))

    def __init__(self, user_id, platform_id, access_token, refresh_token):
        self.user_id = user_id
        self.platform_id = platform_id
        self.access_token = access_token
        self.refresh_token = refresh_token