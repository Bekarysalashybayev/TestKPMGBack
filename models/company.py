from sqlalchemy import Column, Integer, VARCHAR, Date
from config.db import Base


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    day = Column(Integer)
    title = Column(VARCHAR(255))
    date = Column(Date)
    type1 = Column(VARCHAR(255))
    type2 = Column(VARCHAR(255))
    type3 = Column(VARCHAR(255))
    value = Column(Integer)

