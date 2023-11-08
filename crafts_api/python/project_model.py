from sqlalchemy import Column, String, Integer, JSON
from  main import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String, index=True)
    inspiration = Column(String, index=True)
    completion_status = Column(String, index=True)

    
