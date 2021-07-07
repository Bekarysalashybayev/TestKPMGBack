from sqlalchemy import text
from sqlalchemy.orm import Session
from models.company import Company
from schemas.company import CompanyCreate


def get_company_list(db: Session):
    return db.query(Company).all()


def get_company_titles(db: Session, q):
    q1 = text("select title from company")
    return db.execute(q1).fetchall()


def get_company_values(db: Session, q):
    s = ''
    if q != "":
        s = "where  t1.date between " + q

    q = text("select t1.title,t1. type1, t1.type2, sum(t1.total) as total"
             " from (select title, type1, type2, date, sum(value) as total "
             "from company group by title, type1, type2, date) AS t1  " + s +
             " group by t1.title, t1.type1, t1.type2;")

    return db.execute(q).fetchall()


def create_company(db: Session, item: CompanyCreate):
    company = Company(**item)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
