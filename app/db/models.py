from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    group_cost = Column(String(8))
    startdate = Column(String(255))
    pvtv_cat = Column(Integer)
    num_contestants = Column(Integer)
    net_percentage = Column(String(5))
    dir_split = Column(String(5))
    logo = Column(String(255))
    group_only = Column(String(8))
    background_image = Column(String(255))
    location = Column(String(255))
    accesses = relationship("Access", back_populates="category", cascade="all, delete")
    access_removed = relationship("AccessRemoved", back_populates="category", cascade="all, delete")
    sub_categories = relationship("SubCategory", back_populates="category", cascade="all, delete")

class Access(Base):
    __tablename__ = 'access'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(String(50))  # varchar(50), nullable
    video_id = Column(String(50))     # varchar(50), nullable
    grant_time = Column(DateTime, nullable=False)  # SQL: timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
    purchase_id = Column(Integer, ForeignKey('purchases.id'), nullable=False)
    user = relationship("User", back_populates="accesses")
    category = relationship("Category", back_populates="accesses")
    purchase = relationship("Purchase", back_populates="accesses")

class AccessRemoved(Base):
    __tablename__ = 'access_removed'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(String(255), nullable=False)
    video_id = Column(String(255), nullable=False)
    grant_time = Column(String(255), nullable=False)  # varchar(255) NOT NULL
    purchase_id = Column(Integer, ForeignKey('purchases.id'), nullable=False)
    remove_time = Column(String(255), nullable=False)  # varchar(255) NOT NULL
    remove_reason = Column(String(255), nullable=False)
    user = relationship("User", back_populates="access_removed")
    category = relationship("Category", back_populates="access_removed")
    purchase = relationship("Purchase", back_populates="access_removed")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(155), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    verified = Column(Integer, nullable=False, default=0)
    token = Column(String(155))
    pwtoken = Column(String(155))
    pwtokenexpire = Column(String(25))
    admin = Column(Integer, nullable=False, default=0)
    allaccess_exp = Column(Integer)
    register_time = Column(Integer, nullable=False)
    stripe_customer_id = Column(String(255))
    pvtv_stripe_customer_id = Column(String(255))
    pvtv_sub_expire = Column(String(255))
    pvtv_db_user_id = Column(String(255))
    session_version = Column(Integer, nullable=False, default=0)
    accesses = relationship("Access", back_populates="user", cascade="all, delete")
    access_removed = relationship("AccessRemoved", back_populates="user", cascade="all, delete")
    purchases = relationship("Purchase", back_populates="user", cascade="all, delete")

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(String(55), nullable=False)
    time = Column(Integer, nullable=False)
    stripe_purchase_session_id = Column(String(255), nullable=False)
    amount = Column(String(10), nullable=False)
    cat_id = Column(String(5), nullable=False)
    video_id = Column(String(5), nullable=False)
    stripe_customer_link = Column(String(255), nullable=False)
    charge_id = Column(String(255), nullable=False, unique=True)
    invoice_id = Column(String(255), nullable=False)
    discount_applied = Column(String(255))
    discount_id = Column(String(40))
    user = relationship("User", back_populates="purchases")
    accesses = relationship("Access", back_populates="purchase", cascade="all, delete")
    access_removed = relationship("AccessRemoved", back_populates="purchase", cascade="all, delete")

class DLAccess(Base):
    __tablename__ = 'dl_access'
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, nullable=False)
    token = Column(Integer, nullable=False)
    expiry = Column(String(255), nullable=False)

class DLAccessLog(Base):
    __tablename__ = 'dl_access_log'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)
    useragent = Column(Text, nullable=False)

class DLCodeLog(Base):
    __tablename__ = 'dl_code_log'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    ip = Column(String(255))
    useragent = Column(Text)
    token = Column(Integer)
    email = Column(String(255))
    type = Column(String(255))
    time = Column(Integer)

class DLEntitlement(Base):
    __tablename__ = 'dl_entitlements'
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, nullable=False)
    uid = Column(Integer, nullable=False)

class DLFile(Base):
    __tablename__ = 'dl_files'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    group_id = Column(Integer, nullable=False)
    bucket_id = Column(String(255), nullable=False)
    b2_file_id = Column(Text, nullable=False)
    bucket_name = Column(String(255), nullable=False)
    size = Column(String(255), nullable=False)

class DLGroup(Base):
    __tablename__ = 'dl_groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    bucket_id = Column(String(255), nullable=False)
    bucket_name = Column(String(255), nullable=False)
    status = Column(String(1), nullable=False, default='1')

class DLLog(Base):
    __tablename__ = 'dl_log'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    file_id = Column(Integer, nullable=False)
    entitlement_id = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)  # timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
    ip = Column(String(255), nullable=False)
    useragent = Column(Text, nullable=False)
    url = Column(Text, nullable=False)

class DLUser(Base):
    __tablename__ = 'dl_users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
    group_id = Column(Integer, nullable=False)
    file_expire = Column(Integer)
    access_expire = Column(Integer)
    reminder_sent = Column(String(255))

class DRMDisable(Base):
    __tablename__ = 'drm_disable'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)
    reason = Column(String(255))
    time = Column(Integer)

class Emergency(Base):
    __tablename__ = 'emergency'
    id = Column(Integer, primary_key=True, index=True)
    vid_id = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    time = Column(Integer, nullable=False)

class ForceRefresh(Base):
    __tablename__ = 'force_refresh'
    id = Column(Integer, primary_key=True, index=True)
    vid_id = Column(String(255), nullable=False)
    user_id = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)

class LimitedAccess(Base):
    __tablename__ = 'limited_access'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(55), nullable=False)
    expiration = Column(String(10), nullable=False)
    expires_on = Column(Integer)
    ip = Column(String(255))
    content = Column(Text, nullable=False)
    note = Column(Text)
    tv = Column(String(15), nullable=False, default='false')

class LiveEvent(Base):
    __tablename__ = 'live_events'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    embed = Column(Text)
    embed2 = Column(String(255))
    embed3 = Column(String(255))
    forceShow = Column(Integer, default=2)
    start = Column(String(55), nullable=False)
    end = Column(String(55), nullable=False)
    category = Column(Integer, nullable=False)
    cost = Column(String(10), nullable=False)
    location = Column(String(55), nullable=False)
    timezone = Column(String(55))
    pvtv = Column(String(255))
    stream_key = Column(String(255))
    stream_key2 = Column(String(255))
    muxStreamID = Column(String(255))
    vote_category = Column(Integer)
    vote_end = Column(Integer)
    viewable_date = Column(Integer, nullable=False, default=1)
    drm = Column(Integer, nullable=False, default=0)
    replay = Column(String(8))
    sub_category = Column(Integer, nullable=False, default=0)
    thumb = Column(String(255))

class LoginLog(Base):
    __tablename__ = 'login_log'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    time = Column(Integer, nullable=False)
    success = Column(String(100), nullable=False)
    user_token = Column(String(255))

class Package(Base):
    __tablename__ = 'packages'
    id = Column(Integer, primary_key=True, index=True)
    package = Column(String(55), nullable=False)
    package_group = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    subtext = Column(Text, nullable=False)
    subtextstyle = Column(String(55), nullable=False)
    square_link = Column(String(255), nullable=False)
    point1 = Column(String(255))
    point2 = Column(String(255))
    point3 = Column(String(255))
    point4 = Column(String(255))
    button = Column(String(55))
    available = Column(Integer, nullable=False, default=1)
    image = Column(String(255))

class PackageClick(Base):
    __tablename__ = 'package_clicks'
    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, nullable=False)
    ip = Column(String(255), nullable=False)
    time = Column(String(255))  # varchar(255) DEFAULT NULL
    referrer = Column(String(255))
    browser = Column(String(255), nullable=False)

class PackageGroup(Base):
    __tablename__ = 'package_groups'
    id = Column(Integer, primary_key=True, index=True)
    pageant_cat_id = Column(Integer, nullable=False)
    promo = Column(Text)
    promo_end = Column(Integer)
    expire = Column(Integer)
    delivery_timeframe = Column(String(255), nullable=False, default='Files will be delivered (or shipped, if applicable) within approximately 2-8 weeks of finals or ordering (whichever is latest). Please ensure your personal information entered at time of ordering is correct to avoid delays.')
    license = Column(String(255), nullable=False, default='All video files are licensed for personal use only. Please see our full license terms at <a href="https://pageant.vision/license" class="text-decoration-underline text-light" target="_blank">pageant.vision/license</a>.')

class RecentlyAired(Base):
    __tablename__ = 'recently_aired'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)

class RecentlyAiredClick(Base):
    __tablename__ = 'recently_aired_clicks'
    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, nullable=False)
    ip = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    referrer = Column(String(255))
    browser = Column(Text)

class SubCategory(Base):
    __tablename__ = 'sub_categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    cat_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="sub_categories")

class UserToken(Base):
    __tablename__ = 'user_tokens'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)
    set_time = Column(Integer, nullable=False)
    user_agent = Column(Text, nullable=False)
    ip_address = Column(String(255), nullable=False)

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)
    contestant_id = Column(Integer, nullable=False)
    ip_address = Column(String(255), nullable=False)
    user_agent = Column(Text, nullable=False)
    time = Column(Integer, nullable=False)

class VoteCategory(Base):
    __tablename__ = 'vote_categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    disabled = Column(Integer, nullable=False, default=0)

class VoteContestant(Base):
    __tablename__ = 'vote_contestants'
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    division = Column(String(255), nullable=False)

class VoteDivision(Base):
    __tablename__ = 'vote_divisions'
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)

class Waitlist(Base):
    __tablename__ = 'waitlist'
    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(String(25), nullable=False)
    email = Column(String(255), nullable=False)
    time = Column(Integer, nullable=False)
    ip = Column(String(255), nullable=False)

class WatchLog(Base):
    __tablename__ = 'watch_log'
    id = Column(Integer, primary_key=True, index=True)
    vid_id = Column(String(55), nullable=False)
    user_id = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    ip = Column(String(255), nullable=False)
    useragent = Column(Text, nullable=False)
    user_token = Column(String(255))

class WatchLogPing(Base):
    __tablename__ = 'watch_log_ping'
    id = Column(Integer, primary_key=True, index=True)
    vid_id = Column(String(55), nullable=False)
    user_id = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    ip = Column(String(255), nullable=False)
    useragent = Column(Text, nullable=False)
    user_token = Column(String(255))
