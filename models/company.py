from sqlalchemy import Column, Integer, VARCHAR, Date
from config.db import Base


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(VARCHAR(255))
    date = Column(Date)
    fact_qliq_data1 = Column(Integer)
    fact_qliq_data2 = Column(Integer)
    fact_qoil_data1 = Column(Integer)
    fact_qoil_data2 = Column(Integer)
    forecast_qliq_data1 = Column(Integer)
    forecast_qliq_data2 = Column(Integer)
    forecast_qoil_data1 = Column(Integer)
    forecast_qoil_data2 = Column(Integer)

