from datetime import date

from pydantic import BaseModel


class Company(BaseModel):
    id: int
    title: str
    date: date
    fact_qliq_data1: int
    fact_qliq_data2: int
    fact_qoil_data1: int
    fact_qoil_data2: int
    forecast_qliq_data1: int
    forecast_qliq_data2: int
    forecast_qoil_data1: int
    forecast_qoil_data2: int

    class Config:
        orm_mode = True


class CompanyCreate(BaseModel):
    title: str
    date: date
    fact_qliq_data1: int
    fact_qliq_data2: int
    fact_qoil_data1: int
    fact_qoil_data2: int
    forecast_qliq_data1: int
    forecast_qliq_data2: int
    forecast_qoil_data1: int
    forecast_qoil_data2: int
