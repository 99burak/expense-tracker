from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer , Date , String , Numeric

DATABASE_URL = "sqlite:///expense.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True)
    date = Column(Date)
    description = Column(String)
    name = Column(String)
    amount = Column(Numeric(10,2))

Base.metadata.create_all(engine)


