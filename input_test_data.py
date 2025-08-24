import time
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.db import crud, schemas, models

def clear_tables(db: Session):
    # Optional: Uncomment to clear tables before inserting test data
    # db.query(models.Purchase).delete()
    # db.query(models.LiveEvent).delete()
    # db.query(models.Category).delete()
    # db.query(models.User).delete()
    # db.commit()
    pass

def insert_test_data():
    db = SessionLocal()
    try:
        clear_tables(db)

        # 1. Insert users
        users = [
            schemas.UserCreate(
                email="alice@example.com",
                password="testpass1",
                first_name="Alice",
                last_name="Anderson",
                register_time=int(time.time())
            ),
            schemas.UserCreate(
                email="bob@example.com",
                password="testpass2",
                first_name="Bob",
                last_name="Brown",
                register_time=int(time.time())
            ),
        ]
        user_objs = [crud.create_user(db, user) for user in users]

        # 2. Insert categories
        categories = [
            schemas.CategoryCreate(name="Pageant Finals", group_cost="20", startdate="2024-07-01"),
            schemas.CategoryCreate(name="Talent Show", group_cost="15", startdate="2024-07-02"),
        ]
        category_objs = [crud.create_category(db, cat) for cat in categories]

        # 3. Insert videos (live_events)
        videos = [
            schemas.LiveEventCreate(
                name="Finals Night",
                start="2024-07-10T19:00:00",
                end="2024-07-10T21:00:00",
                category=category_objs[0].id,
                cost="10",
                location="Main Hall",
                embed="mux_embed1",
                embed2="mux_playback1"
            ),
            schemas.LiveEventCreate(
                name="Talent Performances",
                start="2024-07-11T18:00:00",
                end="2024-07-11T20:00:00",
                category=category_objs[1].id,
                cost="8",
                location="Auditorium",
                embed="mux_embed2",
                embed2="mux_playback2"
            ),
            schemas.LiveEventCreate(
                name="Interview Round",
                start="2024-07-12T17:00:00",
                end="2024-07-12T19:00:00",
                category=category_objs[0].id,
                cost="5",
                location="Conference Room",
                embed="mux_embed3",
                embed2="mux_playback3"
            ),
        ]
        # Direct SQLAlchemy add for LiveEvent, since no CRUD provided
        video_objs = []
        for v in videos:
            obj = models.LiveEvent(**v.dict())
            db.add(obj)
            db.commit()
            db.refresh(obj)
            video_objs.append(obj)

        # 4. Insert purchases (one category and one video per user)
        purchases = [
            schemas.PurchaseCreate(
                user_id=user_objs[0].id,
                email=user_objs[0].email,
                time=int(time.time()),
                stripe_purchase_session_id="sess_001",
                amount="20",
                cat_id=str(category_objs[0].id),
                video_id="",
                stripe_customer_link="https://stripe.com/customer/alice",
                charge_id="ch_001",
                invoice_id="inv_001"
            ),
            schemas.PurchaseCreate(
                user_id=user_objs[0].id,
                email=user_objs[0].email,
                time=int(time.time()),
                stripe_purchase_session_id="sess_002",
                amount="10",
                cat_id="",
                video_id=str(video_objs[0].id),
                stripe_customer_link="https://stripe.com/customer/alice",
                charge_id="ch_002",
                invoice_id="inv_002"
            ),
            schemas.PurchaseCreate(
                user_id=user_objs[1].id,
                email=user_objs[1].email,
                time=int(time.time()),
                stripe_purchase_session_id="sess_003",
                amount="15",
                cat_id=str(category_objs[1].id),
                video_id="",
                stripe_customer_link="https://stripe.com/customer/bob",
                charge_id="ch_003",
                invoice_id="inv_003"
            ),
            schemas.PurchaseCreate(
                user_id=user_objs[1].id,
                email=user_objs[1].email,
                time=int(time.time()),
                stripe_purchase_session_id="sess_004",
                amount="8",
                cat_id="",
                video_id=str(video_objs[1].id),
                stripe_customer_link="https://stripe.com/customer/bob",
                charge_id="ch_004",
                invoice_id="inv_004"
            ),
        ]
        purchase_objs = [crud.create_purchase(db, p) for p in purchases]

        print(f"Inserted {len(user_objs)} users, {len(category_objs)} categories, {len(video_objs)} videos, {len(purchase_objs)} purchases.")

    finally:
        db.close()

if __name__ == "__main__":
    insert_test_data()





#session version tells us how user can be logged in at one place at a time
#checks to see if their session version is the same version

#browser returns a hash and that
#session version is incremented by 1

#verification (column name) should be 1

#check the login process

#ios pass a drm token 
#logging