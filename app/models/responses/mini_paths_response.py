from pydantic import BaseModel
from typing import List


class PathStep(BaseModel):
    step: int
    topic: str
    resource: str
    duration: str


class MiniPathResponse(BaseModel):
    missing_skill: str
    mini_path: List[PathStep]
