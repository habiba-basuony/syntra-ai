from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class DocType(str, Enum):
    SRS = "SRS"
    WEEKLY_REPORT = "weekly_report"
    GANTT = "gantt"
    FINAL_PRESENTATION = "final_presentation"


class TaskInfo(BaseModel):
    title: str
    assigned_to: str
    status: str
    due_date: Optional[str] = None


class DocumentationRequest(BaseModel):
    project_name: str
    doc_type: DocType
    tasks: List[TaskInfo]
    team_members: List[str]
    project_description: str
    progress_summary: Optional[str] = None
