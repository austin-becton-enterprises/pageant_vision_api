from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper
from ...db.models import Access

META_TAG_KEY_VIDEO_ID = "video_id"
META_TAG_KEY_CAT_ID = "cat_id"

class PVAccess:
    data: DatabaseObjectWrapper

    def __init__(self, data: DatabaseObjectWrapper):
        self.data = data

    @staticmethod
    def fromAccessModel(access_model: Access) -> "PVAccess | None":
        if access_model is None:
            return None
        data_wrapper = DatabaseObjectWrapper(jsonDict={})
        data_wrapper.set_or_append(incoming_meta_tags={
            META_TAG_KEY_VIDEO_ID: access_model.video_id,
            META_TAG_KEY_CAT_ID: access_model.category_id  # <-- changed from cat_id to category_id
        })
        return PVAccess(data=data_wrapper)

    def video_id(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_VIDEO_ID)

    def cat_id(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_CAT_ID)
