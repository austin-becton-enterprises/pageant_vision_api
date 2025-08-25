from sqlalchemy.orm import Session
from app.db import session
from app.db.models import User
from ..models.hax_models.pv_person import PVPerson
from app.db import crud
import logging

class DatabaseService:

    def __init__(self, db_url: str = None):
        # db_url is unused; using SessionLocal from app.db.session
        self.SessionLocal = session.SessionLocal

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def get_user(with_email: str) -> "User | None":
        db = session.SessionLocal()
        try:
            user = db.query(User).filter(
                User.email == with_email
            ).first()
            return user
        finally:
            db.close()

    @staticmethod
    def update_session_version_and_token(user_id: int, token: str = None) -> User:
        db = session.SessionLocal()
        try:
            updated_user = crud.update_session_version_and_token(db, user_id, token)
            if updated_user is None:
                logging.warning(f"update_session_version_and_token: No user found with id={user_id}")
            return updated_user
        except Exception as e:
            logging.error(f"Exception in update_session_version_and_token: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def add_log(email: str, success: str, ip_address: str = None, user_agent: str = None, user_id: int = None, user_token: str = None):
        db = session.SessionLocal()
        try:
            from app.db.models import LoginLog
            from datetime import datetime
            import time as time_mod
            log = LoginLog(
                username=email,
                ip=ip_address or "",
                time=int(time_mod.time()),
                success=success,
                user_token=user_token
            )
            db.add(log)
            db.commit()
        finally:
            db.close()

    @staticmethod
    def get_purchases_for_user(user_id: int):
        db = session.SessionLocal()
        try:
            from app.db.models import Purchase
            results = db.query(Purchase).filter(Purchase.user_id == user_id).all()
            # Make sure to call as_dict() if you want dicts
            # return [purchase.as_dict() for purchase in results]
            return results
        finally:
            db.close()

    @staticmethod
    def get_videos_by_category_ids(category_ids: set):
        from app.db.models import LiveEvent
        db = session.SessionLocal()
        try:
            if not category_ids:
                return []
            return db.query(LiveEvent).filter(LiveEvent.category.in_(category_ids)).all()
        finally:
            db.close()

    @staticmethod
    def get_videos_by_video_ids(video_ids: set):
        from app.db.models import LiveEvent
        db = session.SessionLocal()
        try:
            if not video_ids:
                return []
            return db.query(LiveEvent).filter(LiveEvent.id.in_(video_ids)).all()
        finally:
            db.close()