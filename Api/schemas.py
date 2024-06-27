# schemas.py
# Définition des schémas Pydantic utilisés pour la validation des données et les réponses API.

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)
