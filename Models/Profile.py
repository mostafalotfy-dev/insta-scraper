from typing import List, Any


class BioLink:
    title: str
    lynx_url: str
    url: str
    link_type: str

    def __init__(self, title: str, lynx_url: str, url: str, link_type: str) -> None:
        self.title = title
        self.lynx_url = lynx_url
        self.url = url
        self.link_type = link_type


class BiographyWithEntities:
    raw_text: str
    entities: List[Any]

    def __init__(self, raw_text: str, entities: List[Any]) -> None:
        self.raw_text = raw_text
        self.entities = entities


class EdgeFollow:
    count: int

    def __init__(self, count: int) -> None:
        self.count = count


class Node:
    username: str

    def __init__(self, username: str) -> None:
        self.username = username


class Edge:
    node: Node

    def __init__(self, node: Node) -> None:
        self.node = node


class EdgeMutualFollowedBy:
    count: int
    edges: List[Edge]

    def __init__(self, count: int, edges: List[Edge]) -> None:
        self.count = count
        self.edges = edges


class PageInfo:
    has_next_page: bool
    end_cursor: str

    def __init__(self, has_next_page: bool, end_cursor: str) -> None:
        self.has_next_page = has_next_page
        self.end_cursor = end_cursor


class EdgeOwnerToTimelineMedia:
    count: int
    page_info: PageInfo
    edges: List[Any]

    def __init__(self, count: int, page_info: PageInfo, edges: List[Any]) -> None:
        self.count = count
        self.page_info = page_info
        self.edges = edges


class FbProfileBiolink:
    url: str
    name: str

    def __init__(self, url: str, name: str) -> None:
        self.url = url
        self.name = name


class User:
    ai_agent_type: None
    biography: str
    bio_links: List[BioLink]
    fb_profile_biolink: FbProfileBiolink
    biography_with_entities: BiographyWithEntities
    blocked_by_viewer: bool
    restricted_by_viewer: bool
    country_block: bool
    eimu_id: str
    external_url: str
    external_url_linkshimmed: str
    edge_followed_by: EdgeFollow
    fbid: str
    followed_by_viewer: bool
    edge_follow: EdgeFollow
    follows_viewer: bool
    full_name: str
    group_metadata: None
    has_ar_effects: bool
    has_clips: bool
    has_guides: bool
    has_channel: bool
    has_blocked_viewer: bool
    highlight_reel_count: int
    has_requested_viewer: bool
    hide_like_and_view_counts: bool
    id: int
    is_business_account: bool
    is_professional_account: bool
    is_supervision_enabled: bool
    is_guardian_of_viewer: bool
    is_supervised_by_viewer: bool
    is_supervised_user: bool
    is_embeds_disabled: bool
    is_joined_recently: bool
    guardian_id: None
    business_address_json: None
    business_contact_method: str
    business_email: None
    business_phone_number: None
    business_category_name: None
    overall_category_name: None
    category_enum: None
    category_name: str
    is_private: bool
    is_verified: bool
    is_verified_by_mv4_b: bool
    is_regulated_c18: bool
    edge_mutual_followed_by: EdgeMutualFollowedBy
    pinned_channels_list_count: int
    profile_pic_url: str
    profile_pic_url_hd: str
    requested_by_viewer: bool
    should_show_category: bool
    should_show_public_contacts: bool
    show_account_transparency_details: bool
    transparency_label: None
    transparency_product: None
    username: str
    connected_fb_page: None
    pronouns: List[Any]
    edge_owner_to_timeline_media: EdgeOwnerToTimelineMedia

    def __init__(self, ai_agent_type: None, biography: str, bio_links: List[BioLink],
                 fb_profile_biolink: FbProfileBiolink, biography_with_entities: BiographyWithEntities,
                 blocked_by_viewer: bool, restricted_by_viewer: bool, country_block: bool, eimu_id: str,
                 external_url: str, external_url_linkshimmed: str, edge_followed_by: EdgeFollow, fbid: str,
                 followed_by_viewer: bool, edge_follow: EdgeFollow, follows_viewer: bool, full_name: str,
                 group_metadata: None, has_ar_effects: bool, has_clips: bool, has_guides: bool, has_channel: bool,
                 has_blocked_viewer: bool, highlight_reel_count: int, has_requested_viewer: bool,
                 hide_like_and_view_counts: bool, id: int, is_business_account: bool, is_professional_account: bool,
                 is_supervision_enabled: bool, is_guardian_of_viewer: bool, is_supervised_by_viewer: bool,
                 is_supervised_user: bool, is_embeds_disabled: bool, is_joined_recently: bool, guardian_id: None,
                 business_address_json: None, business_contact_method: str, business_email: None,
                 business_phone_number: None, business_category_name: None, overall_category_name: None,
                 category_enum: None, category_name: str, is_private: bool, is_verified: bool,
                 is_verified_by_mv4_b: bool, is_regulated_c18: bool, edge_mutual_followed_by: EdgeMutualFollowedBy,
                 pinned_channels_list_count: int, profile_pic_url: str, profile_pic_url_hd: str,
                 requested_by_viewer: bool, should_show_category: bool, should_show_public_contacts: bool,
                 show_account_transparency_details: bool, transparency_label: None, transparency_product: None,
                 username: str, connected_fb_page: None, pronouns: List[Any],
                 edge_owner_to_timeline_media: EdgeOwnerToTimelineMedia) -> None:
        self.ai_agent_type = ai_agent_type
        self.biography = biography
        self.bio_links = bio_links
        self.fb_profile_biolink = fb_profile_biolink
        self.biography_with_entities = biography_with_entities
        self.blocked_by_viewer = blocked_by_viewer
        self.restricted_by_viewer = restricted_by_viewer
        self.country_block = country_block
        self.eimu_id = eimu_id
        self.external_url = external_url
        self.external_url_linkshimmed = external_url_linkshimmed
        self.edge_followed_by = edge_followed_by
        self.fbid = fbid
        self.followed_by_viewer = followed_by_viewer
        self.edge_follow = edge_follow
        self.follows_viewer = follows_viewer
        self.full_name = full_name
        self.group_metadata = group_metadata
        self.has_ar_effects = has_ar_effects
        self.has_clips = has_clips
        self.has_guides = has_guides
        self.has_channel = has_channel
        self.has_blocked_viewer = has_blocked_viewer
        self.highlight_reel_count = highlight_reel_count
        self.has_requested_viewer = has_requested_viewer
        self.hide_like_and_view_counts = hide_like_and_view_counts
        self.id = id
        self.is_business_account = is_business_account
        self.is_professional_account = is_professional_account
        self.is_supervision_enabled = is_supervision_enabled
        self.is_guardian_of_viewer = is_guardian_of_viewer
        self.is_supervised_by_viewer = is_supervised_by_viewer
        self.is_supervised_user = is_supervised_user
        self.is_embeds_disabled = is_embeds_disabled
        self.is_joined_recently = is_joined_recently
        self.guardian_id = guardian_id
        self.business_address_json = business_address_json
        self.business_contact_method = business_contact_method
        self.business_email = business_email
        self.business_phone_number = business_phone_number
        self.business_category_name = business_category_name
        self.overall_category_name = overall_category_name
        self.category_enum = category_enum
        self.category_name = category_name
        self.is_private = is_private
        self.is_verified = is_verified
        self.is_verified_by_mv4_b = is_verified_by_mv4_b
        self.is_regulated_c18 = is_regulated_c18
        self.edge_mutual_followed_by = edge_mutual_followed_by
        self.pinned_channels_list_count = pinned_channels_list_count
        self.profile_pic_url = profile_pic_url
        self.profile_pic_url_hd = profile_pic_url_hd
        self.requested_by_viewer = requested_by_viewer
        self.should_show_category = should_show_category
        self.should_show_public_contacts = should_show_public_contacts
        self.show_account_transparency_details = show_account_transparency_details
        self.transparency_label = transparency_label
        self.transparency_product = transparency_product
        self.username = username
        self.connected_fb_page = connected_fb_page
        self.pronouns = pronouns
        self.edge_owner_to_timeline_media = edge_owner_to_timeline_media


class Data:
    user: User

    def __init__(self, user: User) -> None:
        self.user = user


class Api:
    data: Data
    status: str
    userDictionary: dict

    def __init__(self, user_dict: dict, data: Data, status: str) -> None:
        self.data = data
        self.status = status
        self.userDictionary = user_dict
