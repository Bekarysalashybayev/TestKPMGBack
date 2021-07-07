from sqlalchemy import text
from sqlalchemy.orm import Session
from models.company import Company
from schemas.company import CompanyCreate


def get_company_values(db: Session, start_date, end_date):
    sub_query = ''
    if start_date != '':
        sub_query = "where t1.date between '" + start_date + "' and '" + end_date + "'"

    q = text("select t1.title, sum(t1.fact_qliq) as fact_qliq_total, sum(t1.fact_qoil) as fact_qoil_total, "
             "sum(t1.forecast_qliq) as forecast_qliq_total, sum(t1.forecast_qoil) as forecast_qoil_total "
             "from(select title, date, (fact_qliq_data1 + fact_qliq_data2) as fact_qliq, "
             "(fact_qoil_data1 + fact_qoil_data2) as fact_qoil, "
             "(forecast_qliq_data1 + forecast_qliq_data2) as forecast_qliq, "
             "(forecast_qoil_data1 + forecast_qoil_data2) as forecast_qoil from company) as t1 " + sub_query +
             " group by t1.title;")
    return db.execute(q).fetchall()


def create_company(db: Session, item: CompanyCreate):
    company = Company(**item)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
