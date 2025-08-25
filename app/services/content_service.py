from app.services.database_service import DatabaseService

class ContentService:
    @staticmethod
    def mux_thumbnail_url(mux_playback_id: str) -> str:
        # Stub: Replace with real JWT signing logic for Mux
        return f"https://image.mux.com/{mux_playback_id}/thumbnail.jpg?token=SIGNED_JWT"

    @staticmethod
    def get_my_videos(user_id: int):
        purchases = DatabaseService.get_purchases_for_user(user_id)
        print("get my videos called")
        category_ids = set()
        video_ids = set()
        for purchase in purchases:
            if purchase.cat_id:
                category_ids.add(purchase.cat_id)
            if purchase.video_id:
                video_ids.add(purchase.video_id)

        videos = []
        videos += DatabaseService.get_videos_by_category_ids(category_ids)
        videos += DatabaseService.get_videos_by_video_ids(video_ids)

        # Remove duplicates by id
        seen = set()
        unique_videos = []
        for v in videos:
            if v.id not in seen:
                unique_videos.append(v)
                seen.add(v.id)
                
        children = []
        for v in unique_videos:
            meta = {
                "displayTitle": v.name,
                "subtitle": v.location,
                "date": {
                    "start": v.start,
                    "end": v.end,
                    "timezone": v.timezone
                },
                "thumbnailURL": ContentService.mux_thumbnail_url(v.embed2) if v.embed2 else None
            }
            children.append({
                "metaTags": meta,
                "value": v.embed2 or v.id
            })

        return {"children": children}
