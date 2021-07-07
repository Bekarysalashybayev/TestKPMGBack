import datetime

import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.utils import get_db
from services import company as service

company_router = APIRouter()


@company_router.get("/")
async def read_data(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return service.get_company_values(db, start_date, end_date)


@company_router.get("/parse-excel")
async def parse_data(db: Session = Depends(get_db)):
    file = './Задание.xlsx'

    parsed_data = pd.read_excel(file, header=[0, 1, 2])
    parsed_data = parsed_data.iloc[0:, 1:]
    parsed_data = parsed_data.to_dict(orient='record')
    keys = list(parsed_data[0].keys())
    item_keys = {}
    for key in keys[1:]:
        item_keys[key] = '_'.join(key).lower()

    item = {}
    today = datetime.date.today()
    for data in parsed_data:
        item['title'] = data[keys[0]]
        item['date'] = today
        for i in keys[1:]:
            item[item_keys.get(i)] = data[i]

        service.create_company(db, item)
        today = today + datetime.timedelta(days=1)

    return {"msg": "OK"}
