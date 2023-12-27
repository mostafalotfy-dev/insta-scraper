from typing import Optional, List, Any


class HashtagHashtag:
    name: str
    media_count: int
    id: int

    def __init__(self, name: str, media_count: int, id: int) -> None:
        self.name = name
        self.media_count = media_count
        self.id = id


class HashtagElement:
    position: int
    hashtag: HashtagHashtag

    def __init__(self, position: int, hashtag: HashtagHashtag) -> None:
        self.position = position
        self.hashtag = hashtag


class UserUser:
    username: str
    is_verified: bool
    full_name: str
    search_social_context: Optional[str]
    unseen_count: Optional[int]
    pk: str
    live_broadcast_visibility: None
    live_broadcast_id: None
    latest_besties_reel_media: None
    latest_reel_media: int
    group_metadata: None
    seen: int
    profile_pic_url: str
    is_unpublished: None
    id: None

    def __init__(self, username: str, is_verified: bool, full_name: str, search_social_context: Optional[str], unseen_count: Optional[int], pk: str, live_broadcast_visibility: None, live_broadcast_id: None, latest_besties_reel_media: None, latest_reel_media: int, group_metadata: None, seen: int, profile_pic_url: str, is_unpublished: None, id: None) -> None:
        self.username = username
        self.is_verified = is_verified
        self.full_name = full_name
        self.search_social_context = search_social_context
        self.unseen_count = unseen_count
        self.pk = pk
        self.live_broadcast_visibility = live_broadcast_visibility
        self.live_broadcast_id = live_broadcast_id
        self.latest_besties_reel_media = latest_besties_reel_media
        self.latest_reel_media = latest_reel_media
        self.group_metadata = group_metadata
        self.seen = seen
        self.profile_pic_url = profile_pic_url
        self.is_unpublished = is_unpublished
        self.id = id


class UserElement:
    position: int
    user: UserUser

    def __init__(self, position: int, user: UserUser) -> None:
        self.position = position
        self.user = user


class XdtAPIV1FbsearchTopsearchConnection:
    see_more: None
    inform_module: None
    hashtags: List[HashtagElement]
    places: List[Any]
    users: List[UserElement]
    rank_token: str

    def __init__(self, see_more: None, inform_module: None, hashtags: List[HashtagElement], places: List[Any], users: List[UserElement], rank_token: str) -> None:
        self.see_more = see_more
        self.inform_module = inform_module
        self.hashtags = hashtags
        self.places = places
        self.users = users
        self.rank_token = rank_token


class Data:
    xdt_api_v1_fbsearch_topsearch_connection: XdtAPIV1FbsearchTopsearchConnection

    def __init__(self, xdt_api_v1_fbsearch_topsearch_connection: XdtAPIV1FbsearchTopsearchConnection) -> None:
        self.xdt_api_v1_fbsearch_topsearch_connection = xdt_api_v1_fbsearch_topsearch_connection


class Extensions:
    is_final: bool

    def __init__(self, is_final: bool) -> None:
        self.is_final = is_final


class Api:
    data: Data
    extensions: Extensions

    def __init__(self, data: Data, extensions: Extensions) -> None:
        self.data = data
        self.extensions = extensions


