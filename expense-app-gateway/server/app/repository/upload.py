from enum import Enum
from pydantic import BaseModel, Field ,constr ,condecimal
from datetime import datetime
from app.repository import upload_db
from typing import Optional


class Upload(BaseModel):
    id  : Optional[int] = None
    file_size : int
    file_type : str
    name : str
    size : str
    path : str 
    status : str
    created_by : str
    created_at : datetime
    updated_at : datetime
    deleted_at : datetime

class UploadRepository():
    def __init__(self):
        pass
    def create_upload(self,Upload):
        return upload_db.create_upload(Upload)
    

