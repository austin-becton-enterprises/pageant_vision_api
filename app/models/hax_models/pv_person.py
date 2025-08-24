from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper
from fastapi import Request
from models import AuthRequest
from db.models import User

META_TAG_KEY_TOKEN = "token"
META_TAG_KEY_EMAIL = "email"
META_TAG_KEY_VERIFIED = "verified"
META_TAG_VALUE_VERIFIED = META_TAG_KEY_VERIFIED
META_TAG_KEY_USER_ID = "id"

class PVPerson:
    
    data: DatabaseObjectWrapper

    def __init__(self, data: DatabaseObjectWrapper):
        self.data = data
    
    @staticmethod
    def fromUserModel(user_model: User) -> ('PVPerson' | None):
        if user_model is None:
            return None
        verified_status = META_TAG_VALUE_VERIFIED if user_model.verified else None
        data_wrapper = DatabaseObjectWrapper(jsonDict={})
        data_wrapper.set_or_append(incoming_meta_tags={
            META_TAG_KEY_TOKEN: user_model.token,
            META_TAG_KEY_EMAIL: user_model.email,
            META_TAG_KEY_VERIFIED: verified_status
        })
        return PVPerson(data=data_wrapper)

    def token(self, set_new: str=None) -> str:
        if set_new is not None:
            self.data.set_or_append(incoming_meta_tags={META_TAG_KEY_TOKEN: set_new})
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_TOKEN)
    
    def is_verified(self) -> bool:
        tag_value = self.data.specificMetaTagValue(forKey=META_TAG_KEY_VERIFIED) 
        return tag_value is not None and tag_value == META_TAG_VALUE_VERIFIED
    
    def email(self) -> str:
        return self.data.specificMetaTagValue(forKey=META_TAG_KEY_EMAIL)
    
    def user_id(self) -> str:
        int_version = self.data.specificMetaTag(forKey=META_TAG_KEY_USER_ID)
        return str(int_version)
    
    
    