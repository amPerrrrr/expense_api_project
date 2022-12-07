from typing import Optional
from pydantic import BaseModel, Field ,constr ,condecimal 
from datetime import datetime
from app.service import upload_service
class CreateUpload(BaseModel):
    file_size : int
    file_type : str
    name : str
    path : str 
    status : str
    created_by : str




class UploadService():
    def __init__(self):
        pass
    def CreatePublicUpload(self,Upload):
        return upload_service.create_public_upload(Upload)
    def CreatePrivateUpload(self,Upload):
        return upload_service.create_private_upload(Upload)
