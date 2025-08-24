# Test Data Requirements for Staging Database

## 1. Tables to Populate

- **users**
- **live_events** (videos)
- **categories**
- **purchases**

## 2. Minimum Dummy Data Needed

### users
- At least 2 users (for testing ownership and access)
  - Fields: id, email, password_hash, etc.

### categories
- At least 2 categories
  - Fields: id, name, description

### live_events
- At least 3 videos, each assigned to a category
  - Fields: id, name, category (category_id), start, end, timezone, location, embed, embed2, etc.

### purchases
- At least 2 purchases per user:
  - One purchase for a category (cat_id)
  - One purchase for a specific video (video_id)
  - Fields: id, user_id, cat_id, video_id, purchase_date, etc.

## 3. Relationships

- Each video (`live_events`) should belong to a category.
- Each purchase should reference either a category or a video, and a user.

## 4. CRUD Operations Needed

- Insert users
- Insert categories
- Insert videos (live_events)
- Insert purchases

## 5. Questions / Info Needed

- What are the required fields for each table? (Are there NOT NULL constraints or defaults?)
- Are there any foreign key constraints to be aware of?
- Are there any fields that must be unique (e.g., email)?
- Do you want to clear existing data before inserting test data, or just add to what's there?

Please provide:
- Table schemas or SQLAlchemy models for these tables (if available)
- Any required/unique fields not listed above
- Any additional tables that should be populated for your tests
