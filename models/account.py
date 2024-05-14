from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from .base_model import BaseModel

class Account(BaseModel):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    platform_id = Column(Integer, ForeignKey('platform.id'), nullable=False)
    access_token = Column(String(255))
    refresh_token = Column(String(255))
    # add unique constraint 4 user_id and platform_id
    UniqueConstraint('user_id', 'platform_id', name='unique_account_per_user_platform')

    def __init__(self, user_id, platform_id, access_token, refresh_token):
        self.user_id = user_id
        self.platform_id = platform_id
        self.access_token = access_token
        self.refresh_token = refresh_token