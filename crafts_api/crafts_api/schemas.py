from pydantic import BaseModel
from typing import Sequence
from datetime import DateTime

mytime = DateTime('US/Eastern')

class GeneralProject(BaseModel):
    id: int
    name: str
    category: str
    description: str
    inspiration: HttpUrl
    completion_status: str # must contain value in list: ['completed', 'in-progress', 'future']
    # time_spent = None
    # approx_date_began = None
    # due_date = None

    # Method for Checking if Project Instance is Completed:
        # If Completed, Create and Set `self.time_spent` attribute
        # If In-Progress, Create and Set `self.approx_date_began` attribute
        # If Future, Create and Set `self.due_date` attribute


class SearchedProject(BaseModel):
    results: Sequence[]