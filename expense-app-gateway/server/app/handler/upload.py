
from fastapi import APIRouter ,status , File , UploadFile
from app.config.database import  create_connection, close_connection
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import upload  
import json


router = APIRouter()

uploadService = upload.UploadService()

@router.post("/public")
async def create_public_upload(
  file: UploadFile = File(description="A file read as UploadFile"),
):
    return await uploadService.CreatePublicUpload(file)
