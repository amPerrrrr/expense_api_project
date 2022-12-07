from urllib import response
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import user_budget
from typing import Union
import json
from app.models import user_budget as user_budget_model

router = APIRouter()
user_budget_service = user_budget.UserBudgetService()

@router.post("/")
async def CreateUserBudget(user_budget: user_budget_model.CreateUserBudgetForm):
    return await user_budget_service.CreateUserBudget(user_budget)

@router.get("/{user_budget_id}")
async def GetOneUserBudget(user_budget_id: int):
    return await user_budget_service.GetOneUserBudget(user_budget_id)

@router.get("/")
async def GetAllUserBudgetsPaginated(page_number: int, page_size: int):
    return await user_budget_service.GetAllUserBudgetsPaginated(page_number, page_size)

@router.put("/{user_budget_id}")
async def UpdateUserBudget(user_budget_id: int, user_budget: user_budget_model.CreateUserBudgetForm):
    return await user_budget_service.UpdateUserBudget(user_budget_id, user_budget)

@router.delete("/{user_budget_id}")
async def DeleteUserBudget(user_budget_id: int):
    return await user_budget_service.DeleteUserBudget(user_budget_id)

