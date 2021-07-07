import datetime
import copy
import gc
from collections import defaultdict

from fastapi import APIRouter, Depends
from openpyxl import load_workbook
import pandas as pd
from sqlalchemy.orm import Session

from config.utils import get_db
from services import company as service
from schemas.company import CompanyCreate

companyR = APIRouter()
file = '/home/beka/Рабочий стол/Задание.xlsx'


def replenish(data_list, val):
    l1 = data_list[0]
    for i in range(len(data_list)):
        if val in str(data_list[i]):
            data_list[i] = l1
        else:
            l1 = data_list[i]
    return data_list


# 'Unnamed:'
@companyR.get("/")
async def read_data(q: str, db: Session = Depends(get_db)):
    print(q)
    cc = service.get_company_values(db, q)

    arr = []
    o = {
        "name": '',
        "fact": {
            "qliq": '',
            "qoil": '',
        },
        "forecast": {
            "qliq": '',
            "qoil": '',
        },
    }

    if cc:
        t = cc[0].title
        for c in cc:
            if c.title != t:
                arr.append(o)
                t = c.title
                o = {
                    "name": '',
                    "fact": {
                        "qliq": '',
                        "qoil": '',
                    },
                    "forecast": {
                        "qliq": '',
                        "qoil": '',
                    },
                }
            o["name"] = t
            if c.type1 == "fact":
                if c.type2 == "Qliq":
                    o["fact"]["qliq"] = int(c.total)
                if c.type2 == "Qoil":
                    o["fact"]["qoil"] = int(c.total)
            if c.type1 == "forecast":
                if c.type2 == "Qliq":
                    o["forecast"]["qliq"] = int(c.total)
                if c.type2 == "Qoil":
                    o["forecast"]["qoil"] = int(c.total)

        arr.append(o)
    return arr


@companyR.get("/parse-exel")
async def read_data(db: Session = Depends(get_db)):
    xl = pd.read_excel(file, engine='openpyxl')
    day = xl.iloc[2:, :1]
    days = day.values.tolist()

    xl = xl.iloc[:, 1:-2]
    lst = xl.columns.values.tolist()

    xl = xl.fillna(method='ffill').values.tolist()

    lst = replenish(lst, 'Unnamed:')
    xl[0] = replenish(xl[0], 'nan')

    l1 = xl[0]
    l2 = xl[1]
    today = datetime.date.today()

    for index, x in enumerate(xl[2:]):
        company_title = x[0]
        d = days[index][0]
        for i in range(1, len(x)):
            item = {
                "title": company_title,
                "date": today,
                "type1": lst[i],
                "type2": l1[i],
                "type3": l2[i],
                "value": x[i],
                "day": int(d)
            }
            service.create_company(db, item)
        today = today + datetime.timedelta(days=1)

    cc = service.get_company_list(db)
    return cc


@companyR.post("/test")
async def add_data(item: CompanyCreate, db: Session = Depends(get_db)):
    c = service.create_company(db, item)
    return c
