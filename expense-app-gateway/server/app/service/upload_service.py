from re import M
from app.repository.upload import UploadRepository
from app.service import upload
import datetime
import uuid
import shutil
import os

UploadRepository = UploadRepository()


async def create_private_upload(file):
    return await UploadRepository.create_upload(file)

async def create_public_upload(file):
    newfileName = uuid.uuid4().hex
    getCurrentPath = os.getcwd()
    getCurrentPath = "./"+getCurrentPath + "/static/public/"
    getFileType = file.filename.split(".")[-1]

    with open(f"{getCurrentPath}{newfileName}.{getFileType}", "wb") as f:
        f.write(file.file.read())
    fileSize = os.path.getsize(f"{getCurrentPath}{newfileName}.{getFileType}")
    CreateUpload = upload.CreateUpload(
        file_size = fileSize,
        file_type=file.content_type,
        name=f"{newfileName}.{getFileType}",
        path=getCurrentPath,
        status="uploaded",
        created_by="user",
    )

    
    return await UploadRepository.create_upload(CreateUpload)

