from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response


async def create_upload(Upload):
    con = await create_connection()
    tr = con.transaction()
    try:
        await tr.start()
        statement = await con.fetch(
            "INSERT INTO uploads (size,file_type, name, path, status, created_by, created_at, updated_at, deleted_at) VALUES ($1, $2, $3, $4, $5, $6, $7, $8,$9) RETURNING id",
            Upload.file_size,
            Upload.file_type,
            Upload.name,
            Upload.path,
            Upload.status,
            Upload.created_by,
            datetime.now(),
            datetime.now(),
            None,
        )
        await tr.commit()
        return {
            "message": {
                "id": Upload.name,
                "file_size" : Upload.file_size,
                "file_type": Upload.file_type,
                "path": Upload.path,
                "status": Upload.status,
            },
        }
    finally:
        await con.close()
