from app.repository.budget import BudgetRepository
from app.service import budget
from app.models import budget as budget_model

BudgetRepository = BudgetRepository()

async def CreateBudget(budget: budget_model.CreateBudgetForm):
    return await BudgetRepository.create_budget(budget)

async def GetOneBudget(budget_id):
    return await BudgetRepository.get_one_budget(budget_id)

async def GetAllBudgetsPaginated(page_number, page_size):
    return await BudgetRepository.get_all_budget_paginated(page_number, page_size)

async def UpdateBudget(budget_id, budget: budget_model.CreateBudgetForm):
    return await BudgetRepository.update_budget(budget_id, budget)

async def DeleteBudget(budget_id):
    return await BudgetRepository.delete_budget(budget_id)