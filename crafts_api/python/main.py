
#imports from python packages
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from python import api_schemas, crud, project_model, database



# establishing a path to html templates
# BASE_PATH = Path(__file__).resolve().parent
# TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "htmlTemplates"))

#establishing an API name and path to the the api, which in this case is using default schema 
app = FastAPI(title = "Sophie's Never-Ending Project Showcase")

project_model.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {'message': 'i hope that this works'}

@app.get("/projects")
def get_all_projects(db: Session = Depends(get_db)):
    return crud.get_all_projects(db)
    
# @app.get("/search/", status_code=200, response_model= api_schemas.GeneralProject)
# def search_projects(keyword:str, db: Session = Depends(get_db)):
#     """creating a function to search the API based on any word contained in the project's dictionary"""
#     def all_terms_check(project):
#         """this function checks the keyword against ANY of the string values in name, category, and description"""
#         values = project.values()
#         for value in values:
#             if type(value) is str:
#                 if keyword in value:
#                     return True
#         return False
#         results = list(filter(all_terms_check, PROJECTS))
#     return {"results":results}


@app.post("/projects/", response_model=api_schemas.GeneralProject)
def create_project(project: api_schemas.GeneralProjectBase, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


def validate_completion_status(status: str):
    VALID_EXPRESSIONS = ['completed', 'in-progress', 'future']
    if status in VALID_EXPRESSIONS:
        return status
    else:
        raise Exception("Invalid status given.")

# @app.get('/', status_code=200)
# async def root():
#     return {"projects": PROJECTS}


# @app.post('/project/', status_code=201,)
# async def add_project(GeneralProject) -> dict:
#     """add a new project"""
#     new_project_id = len(PROJECTS)+1
#     project_entry = GeneralProject()
#     PROJECTS.append(project_entry)
#     return project_entry

# def project_status(self):
# # Method for Checking if Project Instance is Completed:
#     if self.completion_status == 'completed' :
#         self.time_spent = input('how long did this project take?')
#     elif self.completion_status == 'in-progress':
#         self.approx_date_began = input('when did you start this?')
#     elif self.completion_status == 'future':
#         self.due_date = input('when is this project due?')