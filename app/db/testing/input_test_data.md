# Test Data Requirements for Staging Database

## 1. Tables to Populate

- **users**
- **live_events** (videos)
- **categories**
- **purchases**

## 2. Minimum Dummy Data Needed

### users
- At least 2 users (for testing ownership and access)
  - Fields: id, email, password (not password_hash), first_name, last_name, register_time, etc.

### categories
- At least 2 categories
  - Fields: id, name, group_cost, startdate, etc.

### live_events
- At least 3 videos, each assigned to a category
  - Fields: id, name, category (category_id), start, end, timezone, location, embed, embed2, etc.

### purchases
- At least 2 purchases per user:
  - One purchase for a category (cat_id)
  - One purchase for a specific video (video_id)
  - Fields: id, user_id, cat_id, video_id, time, stripe_purchase_session_id, amount, etc.

## 3. Relationships

- Each video (`live_events`) should belong to a category (`category` is a foreign key to categories.id).
- Each purchase references a user (`user_id`), and either a category (`cat_id`) or a video (`video_id`).

## 4. CRUD Operations Needed

- Insert users
- Insert categories
- Insert videos (live_events)
- Insert purchases

## 5. Answers to Outstanding Questions

- **Required fields:**  
  - Most fields marked as `nullable=False` in models are required.  
  - For users: `email` (unique), `password`, `first_name`, `last_name`, `register_time` are required.
  - For categories: `name` is required.
  - For live_events: `name`, `start`, `end`, `category`, `cost`, `location` are required.
  - For purchases: `user_id`, `email`, `time`, `stripe_purchase_session_id`, `amount`, `cat_id`, `video_id`, `stripe_customer_link`, `charge_id`, `invoice_id` are required.

- **Foreign key constraints:**  
  - `live_events.category` → `categories.id`
  - `purchases.user_id` → `users.id`
  - `purchases.cat_id` and `purchases.video_id` are stored as strings, not strict foreign keys, but should match valid category/video IDs.

- **Unique fields:**  
  - `users.email` is unique.
  - `purchases.charge_id` is unique.

- **Clearing data:**  
  - Decide if you want to clear (truncate) tables before inserting test data, or just add to existing data.  
  - For repeatable tests, truncating is recommended.

## 6. Additional Notes

- All IDs are auto-incremented integers.
- Use realistic but non-sensitive dummy data for emails, names, etc.
- If you need to populate related tables (e.g., access, access_removed), add those as needed for your tests.

---
**Ready for script implementation.**
