from sqlalchemy.orm import Session
from .models import (
    User, Purchase, Category, Access, AccessRemoved, DLAccess,
    # ...add all other models as you migrate them...
)
from . import schemas

# Make sure you define UserUpdate, PurchaseUpdate, CategoryUpdate, AccessUpdate, AccessRemovedUpdate, DLAccessUpdate, etc. in your schemas.py

# USERS CRUD

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# PURCHASES CRUD

def create_purchase(db: Session, purchase: schemas.PurchaseCreate):
    db_purchase = Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def get_purchase(db: Session, purchase_id: int):
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()

def get_purchases_by_user(db: Session, user_id: int):
    return db.query(Purchase).filter(Purchase.user_id == user_id).all()

def update_purchase(db: Session, purchase_id: int, purchase_update: schemas.PurchaseUpdate):
    db_purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
    if not db_purchase:
        return None
    for key, value in purchase_update.dict(exclude_unset=True).items():
        setattr(db_purchase, key, value)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def delete_purchase(db: Session, purchase_id: int):
    db_purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
    if not db_purchase:
        return None
    db.delete(db_purchase)
    db.commit()
    return db_purchase

# CATEGORIES CRUD

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, category_update: schemas.CategoryUpdate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        return None
    for key, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category

# ACCESS CRUD

def create_access(db: Session, access: schemas.AccessCreate):
    db_access = Access(**access.dict())
    db.add(db_access)
    db.commit()
    db.refresh(db_access)
    return db_access

def get_access(db: Session, access_id: int):
    return db.query(Access).filter(Access.id == access_id).first()

def get_access_by_user(db: Session, user_id: int):
    return db.query(Access).filter(Access.user_id == user_id).all()

def update_access(db: Session, access_id: int, access_update: schemas.AccessUpdate):
    db_access = db.query(Access).filter(Access.id == access_id).first()
    if not db_access:
        return None
    for key, value in access_update.dict(exclude_unset=True).items():
        setattr(db_access, key, value)
    db.commit()
    db.refresh(db_access)
    return db_access

def delete_access(db: Session, access_id: int):
    db_access = db.query(Access).filter(Access.id == access_id).first()
    if not db_access:
        return None
    db.delete(db_access)
    db.commit()
    return db_access

# ACCESS_REMOVED CRUD

def create_access_removed(db: Session, access_removed: schemas.AccessRemovedCreate):
    db_access_removed = AccessRemoved(**access_removed.dict())
    db.add(db_access_removed)
    db.commit()
    db.refresh(db_access_removed)
    return db_access_removed

def get_access_removed(db: Session, access_removed_id: int):
    return db.query(AccessRemoved).filter(AccessRemoved.id == access_removed_id).first()

def get_access_removed_by_user(db: Session, user_id: int):
    return db.query(AccessRemoved).filter(AccessRemoved.user_id == user_id).all()

def update_access_removed(db: Session, access_removed_id: int, access_removed_update: schemas.AccessRemovedUpdate):
    db_access_removed = db.query(AccessRemoved).filter(AccessRemoved.id == access_removed_id).first()
    if not db_access_removed:
        return None
    for key, value in access_removed_update.dict(exclude_unset=True).items():
        setattr(db_access_removed, key, value)
    db.commit()
    db.refresh(db_access_removed)
    return db_access_removed

def delete_access_removed(db: Session, access_removed_id: int):
    db_access_removed = db.query(AccessRemoved).filter(AccessRemoved.id == access_removed_id).first()
    if not db_access_removed:
        return None
    db.delete(db_access_removed)
    db.commit()
    return db_access_removed

# DL_ACCESS CRUD

def create_dl_access(db: Session, dl_access: schemas.DLAccessCreate):
    db_dl_access = DLAccess(**dl_access.dict())
    db.add(db_dl_access)
    db.commit()
    db.refresh(db_dl_access)
    return db_dl_access

def get_dl_access(db: Session, dl_access_id: int):
    return db.query(DLAccess).filter(DLAccess.id == dl_access_id).first()

def update_dl_access(db: Session, dl_access_id: int, dl_access_update: schemas.DLAccessUpdate):
    db_dl_access = db.query(DLAccess).filter(DLAccess.id == dl_access_id).first()
    if not db_dl_access:
        return None
    for key, value in dl_access_update.dict(exclude_unset=True).items():
        setattr(db_dl_access, key, value)
    db.commit()
    db.refresh(db_dl_access)
    return db_dl_access

def delete_dl_access(db: Session, dl_access_id: int):
    db_dl_access = db.query(DLAccess).filter(DLAccess.id == dl_access_id).first()
    if not db_dl_access:
        return None
    db.delete(db_dl_access)
    db.commit()
    return db_dl_access

# DL_ACCESS_LOG CRUD
# DL_CODE_LOG CRUD
# DL_ENTITLEMENTS CRUD
# DL_FILES CRUD
# DL_GROUPS CRUD
# DL_LOG CRUD
# DL_USERS CRUD
# DRM_DISABLE CRUD
# EMERGENCY CRUD
# FORCE_REFRESH CRUD
# LIMITED_ACCESS CRUD
# LIVE_EVENTS CRUD
# LOGIN_LOG CRUD
# PACKAGES CRUD
# PACKAGE_CLICKS CRUD
# PACKAGE_GROUPS CRUD
# RECENTLY_AIRED CRUD
# RECENTLY_AIRED_CLICKS CRUD
# SUB_CATEGORIES CRUD
# USER_TOKENS CRUD
# VOTES CRUD
# VOTE_CATEGORIES CRUD
# VOTE_CONTESTANTS CRUD
# VOTE_DIVISIONS CRUD
# WAITLIST CRUD
# WATCH_LOG CRUD
# WATCH_LOG_PING CRUD

# For each table, use the same pattern as above:
# - create_{table}
# - get_{table}
# - update_{table}
# - delete_{table}

