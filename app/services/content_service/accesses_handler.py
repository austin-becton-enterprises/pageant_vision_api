from typing import List, Tuple
from app.services.database_service import DatabaseService as database

def accesses_for(user_id: int) -> Tuple[List[str], List[str]]:
    all_accesses = database.get_accesses_for_user(user_id)
    video_access_ids = [access.video_id for access in all_accesses if access.video_id is not None]
    category_access_ids = [access.category_id for access in all_accesses if access.category_id is not None]
    return video_access_ids, category_access_ids
