import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
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
from app.db.models import Category, LiveEvent, User, Access

def main():
    session = SessionLocal()
    try:
        # Get all categories
        categories = session.query(Category).all()
        print(f"Total categories: {len(categories)}")
        for cat in categories:
            print(f"Category id={cat.id} name={cat.name} background_image={cat.background_image}")

        # Print current UTC time for debugging
        now = datetime.utcnow()
        print(f"\n[DEBUG] Current UTC time: {now}")

        # Print all LiveEvents and their end values for debugging (now also print thumb and muxStreamID)
        all_events = session.query(LiveEvent).all()
        print(f"[DEBUG] Total LiveEvents in DB: {len(all_events)}")
        for event in all_events:
            print(f"[DEBUG] LiveEvent id={event.id} name={event.name} end={event.end} thumb={event.thumb} muxStreamID={event.muxStreamID}")

        # Get all upcoming live events
        events = session.query(LiveEvent).filter(
            func.str_to_date(LiveEvent.end, '%Y-%m-%d %H:%i:%s') > now
        ).all()
        print(f"\nTotal upcoming live events: {len(events)}")
        for event in events:
            print(f"LiveEvent id={event.id} name={event.name} thumb={event.thumb} muxStreamID={event.muxStreamID}")

        # Get accesses for austincbecton@gmail.com
        user = session.query(User).filter(User.email == "austincbecton@gmail.com").first()
        if not user:
            print("\nUser austincbecton@gmail.com not found.")
            return
        accesses = session.query(Access).filter(Access.user_id == user.id).all()
        print(f"\nTotal accesses for {user.email}: {len(accesses)}")
        # Build set of (category_id, video_id) for upcoming events
        upcoming_event_keys = set((str(e.category), str(e.id)) for e in events)
        for access in accesses:
            is_upcoming = (str(access.category_id), str(access.video_id)) in upcoming_event_keys
            print(
                f"Access id={access.id} category_id={access.category_id} video_id={access.video_id} "
                f"grant_time={access.grant_time} purchase_id={access.purchase_id} "
                f"{'**UPCOMING EVENT**' if is_upcoming else ''}"
            )
    finally:
        session.close()

if __name__ == "__main__":
    main()



