from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class Budget(BaseModel):
    budget_id : Optional[int] = None
    public_id : Optional[str] = None
    user_id : int
    budget : float
    status : Optional[str] = None
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime


class CreateBudgetForm(BaseModel):
    public_id : Optional[str] = None
    user_id : int
    budget : float
    status : Optional[str] = None
    class Config:
        schema_extra = {
        "example":
            {
            "budget" : 9999.99,
            "user_id" : 1,
            "status" : "note",
        } 
  }