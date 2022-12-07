from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class UserBudget(BaseModel):
    user_budget_id : Optional[int] = None
    budget_id : int
    user_id : int
    status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateUserBudgetForm(BaseModel):
    budget_id : int
    user_id : int
    status : str
    class Config:
        schema_extra = {
        "example":
            {
            "budget_id" : 1,
            "user_id" : 1,
            "status" : "status"
        } 
  }