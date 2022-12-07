from cProfile import Profile
from datetime import datetime
import uuid

from pydantic import BaseModel
from typing import Optional
import uuid
import datetime
from app.service import category_budget_service
from app.models import category_budget as category_budget_model


class CategoryBudgetService():
    def __init__(self) :
        pass
    def CreateCategoryBudget(self, category_budget: category_budget_model.CreateCategoryBudgetForm):
        return category_budget_service.CreateCategoryBudget(category_budget)
    def GetOneCategoryBudget(self, category_budget_id):
        return category_budget_service.GetOneCategoryBudget(category_budget_id)
    def GetAllCategoryBudgetsPaginated(self, page_number, page_size): 
        return category_budget_service.GetAllCategoryBudgetsPaginated(page_number, page_size)
    def UpdateCategoryBudget(self, category_budget_id, category_budget: category_budget_model.CreateCategoryBudgetForm):
        return category_budget_service.UpdateCategoryBudget(category_budget_id, category_budget)
    def DeleteCategoryBudget(self, category_budget_id):
        return category_budget_service.DeleteCategoryBudget(category_budget_id)