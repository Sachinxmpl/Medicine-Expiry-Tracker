from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    expiry_date = Column(Date)
    quantity = Column(Integer)