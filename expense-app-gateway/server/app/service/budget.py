from cProfile import Profile
from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import budget_service
from app.models import budget as budget_model


class BudgetService():
    def __init__(self) :
        pass
    def CreateBudget(self, budget: budget_model.CreateBudgetForm):
        return budget_service.CreateBudget(budget)
    def GetOneBudget(self, budget_id):
        return budget_service.GetOneBudget(budget_id)
    def GetAllBudgetsPaginated(self, page_number, page_size): 
        return budget_service.GetAllBudgetsPaginated(page_number, page_size)
    def UpdateBudget(self, budget_id, budget: budget_model.CreateBudgetForm):
        return budget_service.UpdateBudget(budget_id, budget)
    def DeleteBudget(self, budget_id):
        return budget_service.DeleteBudget(budget_id)