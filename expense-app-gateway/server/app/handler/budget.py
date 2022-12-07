from urllib import response
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import budget
from typing import Union
import json
from app.models import budget as budget_model

router = APIRouter()
budget_service = budget.BudgetService()

@router.post("/")
async def CreateBudget(budget: budget_model.CreateBudgetForm):
    return await budget_service.CreateBudget(budget)

@router.get("/{budget_id}")
async def GetOneBudget(budget_id: int):
    return await budget_service.GetOneBudget(budget_id)

@router.get("/")
async def GetAllBudgetsPaginated(page_number: int, page_size: int):
    return await budget_service.GetAllBudgetsPaginated(page_number, page_size)

@router.put("/{budget_id}")
async def UpdateBudget(budget_id: int, budget: budget_model.CreateBudgetForm):
    return await budget_service.UpdateBudget(budget_id, budget)

@router.delete("/{budget_id}")
async def DeleteBudget(budget_id: int):
    return await budget_service.DeleteBudget(budget_id)

