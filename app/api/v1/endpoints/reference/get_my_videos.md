# `/my-videos` Endpoint

## Purpose

The `/my-videos` endpoint returns all video access records that the currently authenticated user has, formatted as a `DatabaseObjectWrapper` for front-end consumption.

## How It Works

1. The endpoint authenticates the user and retrieves their user ID.
2. It queries the `access` table for all access records belonging to the user.
   - **Note:** The actual backend uses a `purchases` table to determine access, checking both category (`cat_id`) and video (`video_id`) purchases. If your implementation only uses an `access` table, ensure it is synchronized with the logic in `purchases` and `live_events` as described in `pvcom_readme.md`.
3. For each access record, only the necessary fields are extracted and formatted into a child object with `metaTags` and `value`.
   - **Note:** The backend typically fetches video details from the `live_events` table (title, thumbnail, etc.) for each accessible video, not just from the access record itself.
4. The endpoint returns a `DatabaseObjectWrapper` containing a `children` array of these objects.

## Response

- Returns a `DatabaseObjectWrapper` with a `children` array.
- Each child contains:
  - `metaTags`: An object with `displayTitle`, `subtitle`, `date`, and `thumbnailURL`.
  - `value`: The Mux playback ID or video identifier.
- If the user has no access records, returns an empty `children` array.

## Example Usage

```http
GET /api/v1/endpoints/my-videos
Authorization: Bearer <your_token>
```

## Example Response

```json
{
  "children": [
    {
      "metaTags": {
        "displayTitle": "Miss Michigan",
        "subtitle": "Live from Port Huron, Michigan",
        "date": "August 9, 2025",
        "thumbnailURL": "dummy_miss_michigan"
      },
      "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
    }
    // ...more children...
  ]
}
```

## Notes

- The endpoint requires authentication.
- The returned data structure is optimized for front-end use and does not expose the full `Access` schema.
- **Potential Inaccuracy:** The actual backend logic (see `pvcom_readme.md`) determines access by checking the `purchases` table for both category and video purchases, then fetches video details from `live_events`. If your `/my-videos` endpoint only queries an `access` table, it may not fully reflect the user's entitlements as implemented in production PHP code.
- **Recommendation:** Ensure your endpoint logic matches the PHP flow:
  - Check both category and video purchases.
  - For each accessible video, fetch details from `live_events`.
  - Generate signed thumbnail URLs as described in `pvcom_readme.md`.

---

## What is an `Access` record?

An `Access` record represents a user's entitlement to view a specific video. Each record in the `access` table links a user to a video they can access, and may also reference a category and the purchase that granted access.

The main fields in an `Access` record are:

- `id`: Unique identifier for the access record.
- `user_id`: The ID of the user who has access.
- `category_id`: (Optional) The category/group this access is associated with.
- `video_id`: (Optional) The video ID the user can access (often a Mux playback ID).
- `grant_time`: The time (as a Unix timestamp) when access was granted.
- `purchase_id`: The ID of the purchase that granted this access.

This record is used to determine which videos a user is allowed to view or stream.

---

## How to Match the PHP Flow

To ensure your `/my-videos` endpoint matches the production PHP logic, follow these stages:

### 1. Determine User Entitlements

- Query the `purchases` table for the current user.
- For each purchase:
  - If `cat_id` is set, the user is entitled to all videos in that category.
  - If `video_id` is set, the user is entitled to that specific video.

### 2. Resolve Accessible Videos

- For each category entitlement, query the `live_events` table for all videos in that category.
- For each video entitlement, query `live_events` for that specific video.
- Collect all unique video records the user can access.

### 3. Fetch Video Metadata

- For each accessible video, retrieve:
  - Title (`name`)
  - Subtitle (e.g., `location` or other relevant field)
  - Date (`start`, `end`, and `timezone`)
  - Thumbnail reference (`thumb` or similar)
  - Mux playback ID (`embed2`)

### 4. Generate Signed Thumbnail URLs

- For each video, generate a signed thumbnail URL using the equivalent of the PHP `muxThumbnail` function.
  - This typically involves creating a JWT for the thumbnail and constructing the Mux image URL.

### 5. Format the Response

- For each video, construct a child object with:
  - `metaTags`: `displayTitle`, `subtitle`, `date`, `thumbnailURL`
  - `value`: Mux playback ID or video identifier
- Return a `DatabaseObjectWrapper` with a `children` array of these objects.

### 6. Security

- Ensure only authenticated users can access this endpoint.
- Do not expose sensitive fields or internal IDs.

---

**Summary Table**

| Stage | What to Do |
|-------|------------|
| 1     | Query `purchases` for user entitlements (categories/videos) |
| 2     | Resolve all accessible videos from `live_events` |
| 3     | Fetch metadata for each video |
| 4     | Generate signed thumbnail URLs |
| 5     | Format and return the response as described above |
| 6     | Enforce authentication and data privacy |

---

**Tip:**  
If you currently use only the `access` table, ensure it is kept in sync with the logic above, or refactor to use the `purchases` and `live_events` tables directly for accurate results.

---
