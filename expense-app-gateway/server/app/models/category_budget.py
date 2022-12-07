from optparse import OptParseError
from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class CategoryBudget(BaseModel):
    category_budget_id : Optional[int] = None
    budget_id : int
    name : str
    status : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class CreateCategoryBudgetForm(BaseModel):
    budget_id : int
    name : str
    status : str
    avatar_icon : str
    avatar_color : str
    image_url : str
    class Config:
        schema_extra = {
        "example":
            {
            "budget_id" : 1,
            "name" : "name",
            "status" : "status",
            "avatar_icon" : "avatar_icon",
            "avatar_color" : "avatar_color",
            "image_url" : "image_url"
        } 
  }