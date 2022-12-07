from cProfile import Profile
from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import user_budget_service
from app.models import user_budget as user_budget_model


class UserBudgetService():
    def __init__(self) :
        pass
    def CreateUserBudget(self, user_budget: user_budget_model.CreateUserBudgetForm):
        return user_budget_service.CreateUserBudget(user_budget)
    def GetOneUserBudget(self, user_budget_id):
        return user_budget_service.GetOneUserBudget(user_budget_id)
    def GetAllUserBudgetsPaginated(self, page_number, page_size): 
        return user_budget_service.GetAllUserBudgetsPaginated(page_number, page_size)
    def UpdateUserBudget(self, user_budget_id, user_budget: user_budget_model.CreateUserBudgetForm):
        return user_budget_service.UpdateUserBudget(user_budget_id, user_budget)
    def DeleteUserBudget(self, user_budget_id):
        return user_budget_service.DeleteUserBudget(user_budget_id)