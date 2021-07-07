from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine("sqlite:///test.db")
db_url = "mysql+pymysql://root:root@localhost:3306/test1"
engine = create_engine(db_url)
# meta = MetaData()
# conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
