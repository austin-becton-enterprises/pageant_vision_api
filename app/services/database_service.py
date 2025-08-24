from sqlalchemy.orm import Session
from app.db import session
from app.db.models import User
from models.hax_models.pv_person import PVPerson
from app.db import crud

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
    def get_user(with_email: str, and_password: str) -> (PVPerson | None):
        db = session.SessionLocal()
        try:
            user = db.query(User).filter(
                User.email == with_email,
                #TODO: hash password situation
                User.hashed_password == and_password
            ).first()
            PVPerson.fromUserModel(user)
            return user
        finally:
            db.close()

    @staticmethod
    def update_session_version_and_token(user_id: int, token: str = None) -> User:
        db = session.SessionLocal()
        try:
            return crud.update_session_version_and_token(db, user_id, token)
        finally:
            db.close()

    @staticmethod
    def add_log(email: str, log_value: str, ip_address: str = None, user_agent: str = None, user_id: int = None):
        db = session.SessionLocal()
        try:
            from app.db.models import LoginLog
            from datetime import datetime
            log = LoginLog(
                email=email,
                log_value=log_value,
                timestamp=datetime.utcnow(),
                ip_address=ip_address,
                user_agent=user_agent,
                user_id=user_id
            )
            db.add(log)
            db.commit()
        finally:
            db.close()

    @staticmethod
    def get_purchases_for_user(db: Session, user_id: int):
        from app.db.models import Purchase
        return db.query(Purchase).filter(Purchase.user_id == user_id).all()

    @staticmethod
    def get_videos_by_category_ids(db: Session, category_ids: set):
        from app.db.models import LiveEvent
        if not category_ids:
            return []
        return db.query(LiveEvent).filter(LiveEvent.category.in_(category_ids)).all()

    @staticmethod
    def get_videos_by_video_ids(db: Session, video_ids: set):
        from app.db.models import LiveEvent
        if not video_ids:
            return []
        return db.query(LiveEvent).filter(LiveEvent.id.in_(video_ids)).all()
