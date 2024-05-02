from sqlalchemy import Column, Integer, ForeignKey, JSON, DateTime
from .base_model import BaseModel
from datetime import datetime

class DataPoint(BaseModel):
    __tablename__ = 'datapoint'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    platform_data = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, account_id, platform_data):
        self.account_id = account_id
        self.platform_data = platform_data