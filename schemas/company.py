from datetime import date

from pydantic import BaseModel


class Company(BaseModel):
    id: int
    day: int
    title: str
    date: date
    type1: str
    type2: str
    type3: str
    value: int

    class Config:
        orm_mode = True


class CompanyCreate(BaseModel):
    day: int
    title: str
    date: date
    type1: str
    type2: str
    type3: str
    value: int
