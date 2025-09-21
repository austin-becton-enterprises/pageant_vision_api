import os
from sqlalchemy import create_engine, text
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

print(f"[DEBUG] Using database: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.models import Category, LiveEvent

def main():
    session = SessionLocal()
    try:
        # Disable foreign key checks
        session.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
        
        num_events = session.query(LiveEvent).count()
        num_categories = session.query(Category).count()
        print(f"Deleting {num_events} live events and {num_categories} categories...")

        # Use raw SQL for deletion
        session.execute(text("DELETE FROM live_events;"))
        session.execute(text("DELETE FROM categories;"))
        session.commit()

        # Re-enable foreign key checks
        session.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
        print("All live events and categories have been deleted.")
    finally:
        session.close()

if __name__ == "__main__":
    main()
