from app.repository.user_budget import UserBudgetRepository
from app.service import user_budget
from app.models import user_budget as user_budget_model

UserBudgetRepository = UserBudgetRepository()

async def CreateUserBudget(user_budget: user_budget_model.CreateUserBudgetForm):
    return await UserBudgetRepository.create_user_budget(user_budget)

async def GetOneUserBudget(user_budget_id):
    return await UserBudgetRepository.get_one_user_budget(user_budget_id)

async def GetAllUserBudgetsPaginated(page_number, page_size):
    return await UserBudgetRepository.get_all_user_budget_paginated(page_number, page_size)

async def UpdateUserBudget(user_budget_id, budget: user_budget_model.CreateUserBudgetForm):
    return await UserBudgetRepository.update_user_budget(user_budget_id, budget)

async def DeleteUserBudget(user_budget_id):
    return await UserBudgetRepository.delete_user_budget(user_budget_id)