
#imports from python packages
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates
from typing import Optional
from pathlib import Path
from datetime import DateTime

#imports from local files for data and data schemas
from crafts_api.schemas import GeneralProject
from crafts_api.project_data import PROJECTS


datetime = pendulum.now()
 
#establishing a path to html templates
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "htmlTemplates"))

#establishing an API name and path to the the api, which in this case is using default schema 
crafts_api = FastAPI(title = "Sophie's Never-Ending Project Showcase", openapi_url='/openapi.json')

api_router = APIRouter()

@api_router.get('/', status_code=200)
def root(request:Request)-> dict:
""" get request for initial page """

    return TEMPLATES.TemplateResponse("index.html", 
    {"request": request, "project": PROJECTS}
    )

@api_router.get('project/completed/{id}', status_code=200, response_model=GeneralProject)
def get_projects()

