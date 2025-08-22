
# Video Listing and Mux JWT Playback Flow

This document describes how the backend provides the frontend with a list of videos (with thumbnails, titles, etc.), and how, after a user selects a video, the backend returns the necessary playback credentials (including a signed Mux JWT) for secure video playback.

---

## 1. Listing Videos for the User

### a. Determining Accessible Videos

- The backend checks the user's purchases (from the `purchases` table) to determine which videos or packages (categories) the user has access to.
- For each purchase:
  - If `cat_id` is set, the user has access to all videos in that category.
  - If `video_id` is set, the user has access to that specific video.

### b. Fetching Video Details

- For each accessible video, the backend queries the `live_events` table to get:
  - `id` (video ID)
  - `name` (title)
  - `start`, `end`, `timezone`
  - `cost`
  - `embed`, `embed2` (Mux playback IDs)
  - Other metadata as needed

- Functions involved:
  - `listVidsInCat($catid)` — returns JSON array of videos in a category
  - `ppvName($id)`, `catName($id)` — get video or category names

### c. Generating Thumbnails

- For each video, the backend generates a signed thumbnail URL using:
  - `muxThumbnail($vidID, $drm, $width, $height)`
- This function creates a JWT for the thumbnail and returns a signed Mux image URL.

### d. Sending Data to the Frontend

- The backend returns a list of videos (with IDs, titles, thumbnail URLs, etc.) as JSON or renders them in HTML for the user to browse.

---

## 2. User Selects a Video

When a user selects a video to play:

### a. Frontend Sends Request

- The frontend sends the selected video ID to the backend (e.g., via AJAX or page navigation).

### b. Backend Access Check

- The backend verifies the user has access to the requested video using:
  - `userHasAccess($video_id, $cat_id, $user_id)`
- If access is granted, proceed to generate playback credentials.

---

## 3. Generating Playback Credentials (JWT, IDs)

### a. Fetching Mux Playback ID

- The backend retrieves the Mux playback ID for the video from the `embed2` field in `live_events` (via `ppvEmbed2($video_id)`).

### b. Generating Signed JWTs

- The backend generates one or more JWTs for playback, thumbnails, DRM, etc., using functions such as:
  - `muxPlayer($playback_id, $end_time, $video_name, $user_id)`
  - `muxPlayerDRM(...)` (if DRM is required)
  - `muxPlayback(...)` (for on-demand)
- These functions use the Firebase JWT library to sign tokens with the appropriate claims:
  - `sub` (playback ID)
  - `aud` (audience: "v" for video, "t" for thumbnail, etc.)
  - `exp` (expiration)
  - `kid` (Mux key ID)
  - `playback_restriction_id` (for DRM)
  - Other claims as needed

### c. Returning Playback Data

- The backend returns to the frontend:
  - The Mux playback ID
  - The signed JWT(s) for playback and thumbnails
  - Any additional metadata (title, etc.)

- This can be done by:
  - Embedding the tokens in the HTML (if server-rendered)
  - Returning a JSON response (if using AJAX/API)

---

## 4. Frontend Playback

- The frontend initializes the `<mux-player>` element with the playback ID and JWT(s) received from the backend.
- Example:
  ```html
  <mux-player
    playback-id="..."
    playback-token="..."
    thumbnail-token="..."
    drm-token="..." <!-- if DRM is used -->
    title="..."
    metadata-video-title="..."
    metadata-viewer-user-id="..."
  ></mux-player>
  ```

---

## 5. Security Notes

- JWTs are short-lived and signed with a private key (never exposed to the client).
- Only users with valid access receive playback tokens.
- DRM tokens are used for additional content protection when required.

---

## Summary of Key Functions

- **Video Listing:** `listVidsInCat`, `muxThumbnail`
- **Access Check:** `userHasAccess`
- **Playback Credentials:** `muxPlayer`, `muxPlayerDRM`, `muxPlayback`, etc.
- **Database Tables:** `purchases`, `live_events`, `users`

---

## Example Flow

1. User logs in.
2. Frontend requests list of accessible videos.
3. Backend returns video list with thumbnail URLs.
4. User selects a video.
5. Frontend requests playback credentials for that video.
6. Backend checks access, generates JWT(s), and returns playback ID and tokens.
7. Frontend initializes Mux player with received credentials.

