from sqlalchemy.orm import Session 
from . import api_schemas, project_model

def get_all_projects(db:Session):
    return db.query(project_model.Project).all()

def get_project(db: Session, project_id: int):
    return db.query(project_model.Project).filter(project_model.Project.id == project_id).first()

def create_project(db: Session, project: api_schemas.GeneralProjectBase):
    db_project = project_model.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
