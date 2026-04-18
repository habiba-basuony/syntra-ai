from pydantic import BaseModel


class DocumentationResponse(BaseModel):
    doc_type: str
    project_name: str
    content: str
