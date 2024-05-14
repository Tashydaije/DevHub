from sqlalchemy import Column, Integer, String
from .base_model import BaseModel

class Platform(BaseModel):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    api_url = Column(String(255))
    oauth_url = Column(String(255))

    def __init__(self, name, api_url, oauth_url):
        self.name = name
        self.api_url = api_url
        self.oauth_url = oauth_url

    def json(self):
        # return a dictionary represantation of the platform
        return {
            'id': self.id,
            'name': self.name,
            'api_url': self.api_url,
            'oauth_url': self.oauth_url
        }