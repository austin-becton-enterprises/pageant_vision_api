import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '../.env.staging')
load_dotenv(dotenv_path=env_path)

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB")
DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.models import Category, LiveEvent

def main():
    session = SessionLocal()
    try:
        num_categories = session.query(Category).count()
        num_live_events = session.query(LiveEvent).count()
        print(f"Total categories: {num_categories}")
        print(f"Total live events: {num_live_events}")

        first_category = session.query(Category).first()
        first_live_event = session.query(LiveEvent).first()
        print("First Category object:", first_category.name)
        print("First Category location:", first_category.location)
        print("First LiveEvent object:", first_live_event)
    finally:
        session.close()

if __name__ == "__main__":
    main()
