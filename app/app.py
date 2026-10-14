from fastapi import FastAPI, Depends, HTTPException
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
def get_expenses(name: str | None = None,db: Session = Depends(get_db))-> list[ExpenseResponse]:
    if name is None:
        result = db.execute(select(Expense)).scalars().all()
    else:
        result = db.execute(select(Expense).where(Expense.name == name)).scalars().all()
    return result

@app.get("/expenses/{id}",response_model = ExpenseResponse)
def expenseById(id: int, db: Session = Depends(get_db)) -> ExpenseResponse:
    result = db.execute(select(Expense).where(Expense.id == id)).scalars().one_or_none()
    if result is None:
        raise HTTPException(status_code = 404,detail="Id not found")
    else:
        return result

@app.put("/expenses/{id}", response_model = ExpenseResponse)
def expenseUpdt(id: int, exp: ExpenseCreate, db: Session = Depends(get_db))-> ExpenseResponse:
    item = db.execute(select(Expense).where(Expense.id == id)).scalars().one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="id not found")
    else:
        item.name = exp.name
        item.date = exp.date
        item.amount = exp.amount
        item.description = exp.description

    db.commit()
    db.refresh(item)

    return item

@app.delete("/expenses/{id}")
def expenseDelete(id: int, db: Session = Depends(get_db)):
    item = db.execute(select(Expense).where(Expense.id == id)).scalars().one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="id not found")
    
        
    db.delete(item)
    db.commit()

    return {"message":"Expense deleted successfully"}
        
    