from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper
from app.db.models import LiveEvent
from app.services.jwt_service import JWTService as token_service
# Metatag keys
META_TAG_KEY_DISPLAY_TITLE = "displayTitle"
META_TAG_KEY_SUBTITLE = "subtitle"
META_TAG_KEY_DATE = "date"
META_TAG_KEY_THUMBNAIL_URL = "thumbnailURL"
META_TAG_KEY_BACKGROUND_IMAGE_URL = "backgroundImageURL"
META_TAG_KEY_ID = "id"
METATAG_KEYNAME_UITYPE = 'uiType'
METATAG_VALUE_LISTOFITEMS = 'listOfItems'
METATAG_VLAUE_GROUPED_LIST = 'groupedList'

class MediaOptionCard:
    def __init__(self, data: DatabaseObjectWrapper):
        self.data = data

    def display_title(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_DISPLAY_TITLE)

    def subtitle(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_SUBTITLE)

    def date(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_DATE)

    def thumbnail_url(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_THUMBNAIL_URL)
    
    def background_image_url(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_BACKGROUND_IMAGE_URL)

    def id(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_ID)

class MediaOptionCardFactory:
    
    @staticmethod
    def wrap_lists(list_of_card_lists: list) -> DatabaseObjectWrapper:
        """
        pass in a list of DatabaseObjectWrapper instances, each one holding children which items/cards
        """
        wrapper = DatabaseObjectWrapper(jsonDict={})
        wrapper.set_or_append(incoming_meta_tags={
            METATAG_KEYNAME_UITYPE: METATAG_VLAUE_GROUPED_LIST
        })
        all_children = []
        for card_list in list_of_card_lists:
            all_children.append(card_list)
        wrapper.overwrite(incoming_children=all_children)
        return wrapper
    
    @staticmethod
    def embed_in_list(card_list: list, title: str) -> DatabaseObjectWrapper:
        wrapper = DatabaseObjectWrapper(jsonDict={})
        wrapper.set_or_append(incoming_meta_tags={
            META_TAG_KEY_DISPLAY_TITLE: title,
            METATAG_KEYNAME_UITYPE: METATAG_VALUE_LISTOFITEMS
        })
        wrapper.overwrite(incoming_children=[card.data for card in card_list])
        return wrapper
    
    @staticmethod
    async def from_live_event(live_event: LiveEvent) -> "MediaOptionCard":
        if live_event.thumb is None or live_event.thumb == "":
             live_event.thumb = "https://files.pageantvision.com/logos/ncusathumb1.jpg"
        data_wrapper = DatabaseObjectWrapper(jsonDict={})
        data_wrapper.set_or_append(incoming_meta_tags={
            META_TAG_KEY_ID: str(getattr(live_event, "id", "")),
            META_TAG_KEY_DISPLAY_TITLE: str(getattr(live_event, "name", "")),
            META_TAG_KEY_SUBTITLE: str(getattr(live_event, "location", "")),
            META_TAG_KEY_DATE: str(getattr(live_event, "start", "")),
            META_TAG_KEY_BACKGROUND_IMAGE_URL: str(getattr(live_event, "thumb", "https://files.pageantvision.com/logos/ncusathumb1.jpg")),
        })
        #live_event.muxStreamID = "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        video_id = live_event.muxStreamID
        if video_id is not None and video_id != "":
            data_wrapper.overwrite(incoming_value=live_event.muxStreamID)
        return MediaOptionCard(data=data_wrapper)

    @staticmethod
    def from_category(category) -> "MediaOptionCard":
        if category.background_image is None or category.background_image == "":
             category.background_image = "https://files.pageantvision.com/logos/ncusathumb1.jpg"
        data_wrapper = DatabaseObjectWrapper(jsonDict={})
        data_wrapper.set_or_append(incoming_meta_tags={
            META_TAG_KEY_ID: str(getattr(category, "id", "")),
            META_TAG_KEY_DISPLAY_TITLE: str(getattr(category, "name", "")),
            META_TAG_KEY_SUBTITLE: str(getattr(category, "location", "")),
            META_TAG_KEY_DATE: str(getattr(category, "startdate", "")),
            #META_TAG_KEY_THUMBNAIL_URL: str(getattr(category, "background_image", "https://files.pageantvision.com/logos/ncusathumb1.jpg")),
            META_TAG_KEY_BACKGROUND_IMAGE_URL: str(getattr(category, "background_image", "https://files.pageantvision.com/logos/ncusathumb1.jpg")),
        })
        return MediaOptionCard(data=data_wrapper)
