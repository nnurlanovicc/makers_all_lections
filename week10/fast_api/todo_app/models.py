from .database import Base
from sqlalchemy import Column,Integer,String


class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True, autoincrement=True)
    task = Column(String(255))
    
