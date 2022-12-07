from app.repository.category_budget import CategoryBudgetRepository
from app.service import category_budget
from app.models import category_budget as category_budget_model

CategoryBudgetRepository = CategoryBudgetRepository()

async def CreateCategoryBudget(category_budget: category_budget_model.CreateCategoryBudgetForm):
    return await CategoryBudgetRepository.create_category_budget(category_budget)

async def GetOneCategoryBudget(category_budget_id):
    return await CategoryBudgetRepository.get_one_category_budget(category_budget_id)

async def GetAllCategoryBudgetsPaginated(page_number, page_size):
    return await CategoryBudgetRepository.get_all_category_budget_paginated(page_number, page_size)

async def UpdateCategoryBudget(category_budget_id, category_budget: category_budget_model.CreateCategoryBudgetForm):
    return await CategoryBudgetRepository.update_category_budget(category_budget_id, category_budget)

async def DeleteCategoryBudget(category_budget_id):
    return await CategoryBudgetRepository.delete_category_budget(category_budget_id)