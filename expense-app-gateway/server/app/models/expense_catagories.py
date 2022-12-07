from turtle import update
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class ExpenseCatagories(BaseModel):
    expense_catagories_id : Optional[int] = None
    public_id : Optional[str] = None
    organization_id : int
    avatar_icon : str
    avatar_color : str
    image_url: str
    use_avatar: bool
    description: str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime
    
class CreateExpenseCatagoriesForm(BaseModel):
    public_id : Optional[str] = None
    organization_id : int
    avatar_icon : str
    avatar_color : str
    name : str
    image_url: str
    use_avatar: bool
    description: str
    class Config:
        schema_extra = {
        "example":
            {
            "organization_id" : 1,
            "avatar_icon" : "test",
            "avatar_color" : "test",
            "name" : "name",
            "image_url": "image_url",
            "use_avatar": True,
            "description": "description",
            
        } 
  }