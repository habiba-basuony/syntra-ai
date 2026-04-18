from pydantic import BaseModel
from typing import List


class TaskItem(BaseModel):
    title: str
    description: str
    assigned_to: str
    skills_needed: List[str]
    estimated_hours: int


class AnalysisResponse(BaseModel):
    feasibility: str
    estimated_timeline: str
    risks: List[str]
    suggested_tech_stack: List[str]
    tasks: List[TaskItem]
