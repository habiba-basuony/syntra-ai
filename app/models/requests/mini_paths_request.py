from pydantic import BaseModel
from typing import List


class MiniPathRequest(BaseModel):
    task_title: str
    task_description: str
    member_skills: List[str]
    missing_skill: str
