
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