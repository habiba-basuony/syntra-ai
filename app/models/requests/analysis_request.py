from pydantic import BaseModel
from typing import List


class TeamMember(BaseModel):
    name: str
    role: str
    skills: List[str]
    hours_per_week: int


class AnalysisRequest(BaseModel):
    project_idea: str
    team: List[TeamMember]
