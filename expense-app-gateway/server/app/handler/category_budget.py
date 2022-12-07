from urllib import response
from fastapi import APIRouter ,status , File, UploadFile
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from app.service import category_budget
from typing import Union
import json
from app.models import category_budget as category_budget_model

router = APIRouter()
category_budget_service = category_budget.CategoryBudgetService()

@router.post("/")
async def CreateCategoryBudget(category_budget: category_budget_model.CreateCategoryBudgetForm):
    return await category_budget_service.CreateCategoryBudget(category_budget)

@router.get("/{category_budget_id}")
async def GetOneCategoryBudget(category_budget_id: int):
    return await category_budget_service.GetOneCategoryBudget(category_budget_id)

@router.get("/")
async def GetAllCategoryBudgetsPaginated(page_number: int, page_size: int):
    return await category_budget_service.GetAllCategoryBudgetsPaginated(page_number, page_size)

@router.put("/{category_budget_id}")
async def UpdateCategoryBudget(category_budget_id: int, category_budget: category_budget_model.CreateCategoryBudgetForm):
    return await category_budget_service.UpdateCategoryBudget(category_budget_id, category_budget)

@router.delete("/{category_budget_id}")
async def DeleteCategoryBudget(category_budget_id: int):
    return await category_budget_service.DeleteCategoryBudget(category_budget_id)

