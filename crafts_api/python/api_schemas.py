from pydantic import BaseModel

class GeneralProjectBase(BaseModel):
    name: str
    category: str
    description: str
    inspiration: str
    completion_status: str

class GeneralProject(GeneralProjectBase):
    id: int

