from typing import Optional
from pydantic import BaseModel, EmailStr

# Users table models
class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    verified: int = 0
    token: Optional[str] = None
    pwtoken: Optional[str] = None
    pwtokenexpire: Optional[str] = None
    admin: int = 0
    allaccess_exp: Optional[int] = None
    register_time: int
    stripe_customer_id: Optional[str] = None
    pvtv_stripe_customer_id: Optional[str] = None
    pvtv_sub_expire: Optional[str] = None
    pvtv_db_user_id: Optional[str] = None
    session_version: int = 0

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Purchases table models
class PurchaseBase(BaseModel):
    user_id: int
    email: EmailStr
    time: int
    stripe_purchase_session_id: str
    amount: str
    cat_id: str
    video_id: str
    stripe_customer_link: str
    charge_id: str
    invoice_id: str
    discount_applied: Optional[str] = None
    discount_id: Optional[str] = None

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True

# Categories table models
class CategoryBase(BaseModel):
    name: str
    group_cost: Optional[str] = None
    startdate: Optional[str] = None
    pvtv_cat: Optional[int] = None
    num_contestants: Optional[int] = None
    net_percentage: Optional[str] = None
    dir_split: Optional[str] = None
    logo: Optional[str] = None
    group_only: Optional[str] = None
    background_image: Optional[str] = None
    location: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Access table models
class AccessBase(BaseModel):
    user_id: int
    category_id: Optional[str] = None
    video_id: Optional[str] = None
    grant_time: int  # Integer (Unix timestamp)
    purchase_id: int

class AccessCreate(AccessBase):
    pass

class Access(AccessBase):
    id: int

    class Config:
        orm_mode = True

# AccessRemoved table models
class AccessRemovedBase(BaseModel):
    user_id: int
    category_id: str
    video_id: str
    grant_time: int  # Integer (Unix timestamp)
    purchase_id: int
    remove_time: int  # Integer (Unix timestamp)
    remove_reason: str

class AccessRemovedCreate(AccessRemovedBase):
    pass

class AccessRemoved(AccessRemovedBase):
    id: int

    class Config:
        orm_mode = True

# DL Access
class DLAccessBase(BaseModel):
    uid: int
    token: int
    expiry: str

class DLAccessCreate(DLAccessBase):
    pass

class DLAccess(DLAccessBase):
    id: int
    class Config:
        orm_mode = True

# DL Access Log
class DLAccessLogBase(BaseModel):
    user_id: str
    ip: str
    url: str
    useragent: str

class DLAccessLogCreate(DLAccessLogBase):
    pass

class DLAccessLog(DLAccessLogBase):
    id: int
    class Config:
        orm_mode = True

# DL Code Log
class DLCodeLogBase(BaseModel):
    user_id: Optional[int] = None
    ip: Optional[str] = None
    useragent: Optional[str] = None
    token: Optional[int] = None
    email: Optional[str] = None
    type: Optional[str] = None
    time: Optional[int] = None

class DLCodeLogCreate(DLCodeLogBase):
    pass

class DLCodeLog(DLCodeLogBase):
    id: int
    class Config:
        orm_mode = True

# DL Entitlements
class DLEntitlementBase(BaseModel):
    file_id: int
    uid: int

class DLEntitlementCreate(DLEntitlementBase):
    pass

class DLEntitlement(DLEntitlementBase):
    id: int
    class Config:
        orm_mode = True

# DL Files
class DLFileBase(BaseModel):
    filename: str
    group_id: int
    bucket_id: str
    b2_file_id: str
    bucket_name: str
    size: str

class DLFileCreate(DLFileBase):
    pass

class DLFile(DLFileBase):
    id: int
    class Config:
        orm_mode = True

# DL Groups
class DLGroupBase(BaseModel):
    name: str
    bucket_id: str
    bucket_name: str
    status: str

class DLGroupCreate(DLGroupBase):
    pass

class DLGroup(DLGroupBase):
    id: int
    class Config:
        orm_mode = True

# DL Log
class DLLogBase(BaseModel):
    user_id: int
    file_id: int
    entitlement_id: int
    time: Optional[str] = None
    ip: str
    useragent: str
    url: str

class DLLogCreate(DLLogBase):
    pass

class DLLog(DLLogBase):
    id: int
    class Config:
        orm_mode = True

# DL Users
class DLUserBase(BaseModel):
    email: str
    group_id: int
    file_expire: Optional[int] = None
    access_expire: Optional[int] = None
    reminder_sent: Optional[str] = None

class DLUserCreate(DLUserBase):
    pass

class DLUser(DLUserBase):
    id: int
    class Config:
        orm_mode = True

# DRM Disable
class DRMDisableBase(BaseModel):
    user_id: int
    video_id: int
    reason: Optional[str] = None
    time: Optional[int] = None

class DRMDisableCreate(DRMDisableBase):
    pass

class DRMDisable(DRMDisableBase):
    id: int
    class Config:
        orm_mode = True

# Emergency
class EmergencyBase(BaseModel):
    vid_id: int
    text: str
    time: int  # already int

class EmergencyCreate(EmergencyBase):
    pass

class Emergency(EmergencyBase):
    id: int
    class Config:
        orm_mode = True

# Force Refresh
class ForceRefreshBase(BaseModel):
    vid_id: str
    user_id: str
    time: str

class ForceRefreshCreate(ForceRefreshBase):
    pass

class ForceRefresh(ForceRefreshBase):
    id: int
    class Config:
        orm_mode = True

# Limited Access
class LimitedAccessBase(BaseModel):
    token: str
    expiration: str
    expires_on: Optional[int] = None
    ip: Optional[str] = None
    content: str
    note: Optional[str] = None
    tv: str = "false"

class LimitedAccessCreate(LimitedAccessBase):
    pass

class LimitedAccess(LimitedAccessBase):
    id: int
    class Config:
        orm_mode = True

# Live Events
class LiveEventBase(BaseModel):
    name: str
    embed: Optional[str] = None
    embed2: Optional[str] = None
    embed3: Optional[str] = None
    forceShow: Optional[int] = 2
    start: str
    end: str
    category: int
    cost: str
    location: str
    timezone: Optional[str] = None
    pvtv: Optional[str] = None
    stream_key: Optional[str] = None
    stream_key2: Optional[str] = None
    muxStreamID: Optional[str] = None
    vote_category: Optional[int] = None
    vote_end: Optional[int] = None
    viewable_date: int = 1
    drm: int = 0
    replay: Optional[str] = None
    sub_category: int = 0
    thumb: Optional[str] = None

class LiveEventCreate(LiveEventBase):
    pass

class LiveEvent(LiveEventBase):
    id: int
    class Config:
        orm_mode = True

# Login Log
class LoginLogBase(BaseModel):
    username: str
    ip: str
    time: int  # already int
    success: str
    user_token: Optional[str] = None

class LoginLogCreate(LoginLogBase):
    pass

class LoginLog(LoginLogBase):
    id: int
    class Config:
        orm_mode = True

# Packages
class PackageBase(BaseModel):
    package: str
    package_group: int
    price: int
    subtext: str
    subtextstyle: str
    square_link: str
    point1: Optional[str] = None
    point2: Optional[str] = None
    point3: Optional[str] = None
    point4: Optional[str] = None
    button: Optional[str] = None
    available: int = 1
    image: Optional[str] = None

class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    id: int
    class Config:
        orm_mode = True

# Package Clicks
class PackageClickBase(BaseModel):
    link_id: int
    ip: str
    time: Optional[int] = None  # changed from Optional[str] to Optional[int]
    referrer: Optional[str] = None
    browser: str

class PackageClickCreate(PackageClickBase):
    pass

class PackageClick(PackageClickBase):
    id: int
    class Config:
        orm_mode = True

# Package Groups
class PackageGroupBase(BaseModel):
    pageant_cat_id: int
    promo: Optional[str] = None
    promo_end: Optional[int] = None
    expire: Optional[int] = None
    delivery_timeframe: str
    license: str

class PackageGroupCreate(PackageGroupBase):
    pass

class PackageGroup(PackageGroupBase):
    id: int
    class Config:
        orm_mode = True

# Recently Aired
class RecentlyAiredBase(BaseModel):
    name: str
    link: str
    date: str
    location: str

class RecentlyAiredCreate(RecentlyAiredBase):
    pass

class RecentlyAired(RecentlyAiredBase):
    id: int
    class Config:
        orm_mode = True

# Recently Aired Clicks
class RecentlyAiredClickBase(BaseModel):
    link_id: int
    ip: str
    date: int  # changed from str to int
    referrer: Optional[str] = None
    browser: Optional[str] = None

class RecentlyAiredClickCreate(RecentlyAiredClickBase):
    pass

class RecentlyAiredClick(RecentlyAiredClickBase):
    id: int
    class Config:
        orm_mode = True

# Sub Categories
class SubCategoryBase(BaseModel):
    name: str
    cat_id: int

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategory(SubCategoryBase):
    id: int
    class Config:
        orm_mode = True

# User Tokens
class UserTokenBase(BaseModel):
    token: str
    user_id: int
    set_time: int
    user_agent: str
    ip_address: str

class UserTokenCreate(UserTokenBase):
    pass

class UserToken(UserTokenBase):
    id: int
    class Config:
        orm_mode = True

# Votes
class VoteBase(BaseModel):
    user_id: int
    video_id: int
    contestant_id: int
    ip_address: str
    user_agent: str
    time: int

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int
    class Config:
        orm_mode = True

# Vote Categories
class VoteCategoryBase(BaseModel):
    name: str
    disabled: int = 0

class VoteCategoryCreate(VoteCategoryBase):
    pass

class VoteCategory(VoteCategoryBase):
    id: int
    class Config:
        orm_mode = True

# Vote Contestants
class VoteContestantBase(BaseModel):
    cat_id: str
    name: str
    title: str
    division: str

class VoteContestantCreate(VoteContestantBase):
    pass

class VoteContestant(VoteContestantBase):
    id: int
    class Config:
        orm_mode = True

# Vote Divisions
class VoteDivisionBase(BaseModel):
    cat_id: int
    name: str

class VoteDivisionCreate(VoteDivisionBase):
    pass

class VoteDivision(VoteDivisionBase):
    id: int
    class Config:
        orm_mode = True

# Waitlist
class WaitlistBase(BaseModel):
    package_id: str
    email: str
    time: int  # already int
    ip: str

class WaitlistCreate(WaitlistBase):
    pass

class Waitlist(WaitlistBase):
    id: int
    class Config:
        orm_mode = True

# Watch Log
class WatchLogBase(BaseModel):
    vid_id: str
    user_id: int
    time: int  # already int
    ip: str
    useragent: str
    user_token: Optional[str] = None

class WatchLogCreate(WatchLogBase):
    pass

class WatchLog(WatchLogBase):
    id: int
    class Config:
        orm_mode = True

# Watch Log Ping
class WatchLogPingBase(BaseModel):
    vid_id: str
    user_id: int
    time: int  # already int
    ip: str
    useragent: str
    user_token: Optional[str] = None

class WatchLogPingCreate(WatchLogPingBase):
    pass

class WatchLogPing(WatchLogPingBase):
    id: int
    class Config:
        orm_mode = True


