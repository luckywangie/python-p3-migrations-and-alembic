from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from datetime import datetime

# Set up the database engine
DATABASE_URL = "sqlite:///students.db"  # Path to your SQLite database
engine = create_engine(DATABASE_URL)

# Create all tables in the database (if not already created)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new student object with unique email
student = Student(
    name="Jane Doe",
    email="janedoe_unique@example.com",  # Make sure the email is unique
    grade=90,
    birthday=datetime.strptime("2001-05-15", "%Y-%m-%d"),  # Convert string to datetime object
    enrolled_date=datetime.strptime("2023-09-01", "%Y-%m-%d")  # Convert string to datetime object
)

# Add the student to the session and commit the transaction
try:
    session.add(student)
    session.commit()
    print(f"Student {student.name} has been added successfully.")
except Exception as e:
    session.rollback()  # Rollback in case of any error
    print(f"Error adding student: {e}")
finally:
    session.close()
