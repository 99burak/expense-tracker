from fastapi import FastAPI, Depends
from app.schemas import ExpenseCreate, ExpenseResponse
from app.database import get_db, Expense
from sqlalchemy.orm import Session
from sqlalchemy import select



app = FastAPI()


@app.get("/")
def root():
    return {"message":"hello world"}


@app.post("/expenses",response_model=ExpenseResponse) 
def add_expense(exp: ExpenseCreate,db: Session = Depends(get_db))-> ExpenseResponse:
    new_exp = Expense (name= exp.name, description= exp.description, date= exp.date , amount= exp.amount)

    db.add(new_exp)
    db.commit()
    db.refresh(new_exp)

    return new_exp


@app.get("/expenses",response_model= list[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db))-> list[ExpenseResponse]:
    result = db.execute(select(Expense)).scalars().all()
    return result