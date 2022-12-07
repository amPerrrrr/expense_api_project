from enum import unique
import json
import re
from app.config.database import create_connection
from datetime import date, datetime
import uuid
import asyncpg.exceptions as pg_exceptions
from app.errs.err import err_response
from app.models import budget as budget_model

async def create_budget(budget: budget_model.Budget):
    con = await create_connection()
    statement = await con.fetch(
        "INSERT INTO budget (public_id, budget, user_id, status, created_at, updated_at, deleted_at) VALUES ($1,$2,$3,$4,$5,$6,$7) RETURNING id",
        str(uuid.uuid4()),
        budget.budget,
        budget.user_id,
        budget.status,
        datetime.now(),
        datetime.now(),
        None
    )
    await con.close()
    return ({
        "message" : {
            "id" : ((statement[0].get("id"))),
        }
    })


async def get_one_budget(budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM budget WHERE id = $1 AND deleted_at IS NULL",
        budget_id
    )
    await con.close()
    return statement

async def get_all_budget_paginated(page_number, page_size):
    con = await create_connection()
    statement = await con.fetch(
        "SELECT * FROM budget WHERE deleted_at IS NULL ORDER BY id DESC LIMIT $1 OFFSET $2",
        page_size,
        (page_number - 1) * page_size
    )
    await con.close()
    return statement

async def update_budget(budget_id, budget: budget_model.Budget):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE budget SET budget = $1, user_id = $2, status = $3, updated_at = $4 WHERE id = $5 RETURNING id",
        budget.budget,
        budget.user_id,
        budget.status,
        datetime.now(),
        budget_id
    )
    await con.close()
    return ({
        "message":{
            "id":((statement[0].get("id")))
        }
    })
    
async def delete_budget(budget_id):
    con = await create_connection()
    statement = await con.fetch(
        "UPDATE budget_id SET deleted_at = $1 WHERE id = $2",
        datetime.now(),
        budget_id
    )
    await con.close()
    return statement