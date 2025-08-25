from sqlalchemy.orm import Session
from app.db import session
from app.db.models import User
from ..models.hax_models.pv_person import PVPerson
from ..models.hax_models.pv_purchase import PVPurchase
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
    def get_purchases_for_user(user_id: int) -> list:
        db = session.SessionLocal()
        try:
            from app.db.models import Purchase
            #results = db.query(Purchase).filter(Purchase.user_id == user_id).all()
            all_purchases = db.query(Purchase).all()
            # Filter to unique (cat_id, video_id) combos
            unique = {}
            for purchase in all_purchases:
                key = (purchase.cat_id, purchase.video_id)
                if key not in unique:
                    unique[key] = purchase
            unique_purchases = list(unique.values())
            # Convert to PVPurchase objects
            #return [PVPurchase.fromPurchaseModel(purchase) for purchase in results if purchase is not None]
            return [PVPurchase.fromPurchaseModel(purchase) for purchase in unique_purchases if purchase is not None]
        finally:
            db.close()

    @staticmethod
    def get_accesses_for_user(user_id: int) -> list:
        db = session.SessionLocal()
        try:
            from app.db.models import Access
            # Fetch all access records for the user
            all_accesses = db.query(Access).filter(Access.user_id == user_id).all()
            # Filter to unique (cat_id, video_id) combos
            unique = {}
            for access in all_accesses:
                key = (access.cat_id, access.video_id)
                if key not in unique:
                    unique[key] = access
            unique_accesses = list(unique.values())
            # Convert to PVAccess objects if available, else return raw models
            try:
                from ..models.hax_models.pv_access import PVAccess
                return [PVAccess.fromAccessModel(access) for access in unique_accesses if access is not None]
            except ImportError:
                return unique_accesses
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