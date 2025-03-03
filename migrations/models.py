# models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Define the base class for our models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String(55), unique=True)
    grade = Column(Integer)
    birthday = Column(DateTime)
    enrolled_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, grade={self.grade})>"

# You can add more models (tables) here if needed
