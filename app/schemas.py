from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class ExpenseCreate(BaseModel):
    name: str
    description: str
    date: date
    amount: Decimal

class ExpenseResponse(BaseModel):
    id: int
    name: str
    description: str
    date: date
    amount: Decimal
