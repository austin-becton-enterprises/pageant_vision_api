import os
from datetime import datetime, timedelta
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
        # Create categories with all required fields
        categories_data = [
            {
                "name": "Miss America",
                "group_cost": "100",
                "startdate": "2025-10-01",
                "pvtv_cat": 1,
                "num_contestants": 50,
                "net_percentage": "10",
                "dir_split": "5",
                "logo": "miss_america_logo.jpg",
                "group_only": "no",
                "background_image": "https://files.pageantvision.com/logos/ncusathumb1.jpg",
                "location": "Atlantic City"
            },
            {
                "name": "Miss Universe",
                "group_cost": "120",
                "startdate": "2025-10-06",
                "pvtv_cat": 2,
                "num_contestants": 80,
                "net_percentage": "12",
                "dir_split": "6",
                "logo": "miss_universe_logo.jpg",
                "group_only": "no",
                "background_image": "https://files.pageantvision.com/logos/ncusathumb1.jpg",
                "location": "Las Vegas"
            },
            {
                "name": "Miss World",
                "group_cost": "110",
                "startdate": "2025-10-11",
                "pvtv_cat": 3,
                "num_contestants": 70,
                "net_percentage": "11",
                "dir_split": "5",
                "logo": "miss_world_logo.jpg",
                "group_only": "no",
                "background_image": "https://files.pageantvision.com/logos/ncusathumb1.jpg",
                "location": "London"
            },
        ]
        categories = []
        for cat_data in categories_data:
            cat = Category(**cat_data)
            session.add(cat)
            categories.append(cat)
        session.commit()  # Commit to get IDs

        # Prepare live events for each category with all required fields
        event_names = [
            ["Miss America's Teen", "Miss America Finals"],
            ["Miss Universe Prelim", "Miss Universe Finals"],
            ["Miss World Talent", "Miss World Finals"],
        ]
        live_events = []
        base_date = datetime(2025, 10, 1, 19, 0, 0)
        for idx, cat in enumerate(categories):
            for j, event_name in enumerate(event_names[idx]):
                start = base_date + timedelta(days=idx*5 + j*2)
                end = start + timedelta(hours=3)
                event = LiveEvent(
                    name=event_name,
                    embed="",
                    embed2="",
                    embed3="",
                    forceShow=2,
                    start=start.strftime('%Y-%m-%d %H:%M:%S'),
                    end=end.strftime('%Y-%m-%d %H:%M:%S'),
                    category=cat.id,
                    cost="50",
                    location=cat.location,
                    timezone="America/New_York",
                    pvtv="",
                    stream_key="",
                    stream_key2="",
                    muxStreamID=f"mux_{cat.id}_{j}",
                    vote_category=None,
                    vote_end=None,
                    viewable_date=1,
                    drm=0,
                    replay="yes",
                    sub_category=0,
                    thumb=f"{event_name.lower().replace(' ', '_')}_thumb.jpg"
                )
                session.add(event)
                live_events.append(event)
        session.commit()
        print("Added 3 categories and 6 live events.")
    finally:
        session.close()

if __name__ == "__main__":
    main()
