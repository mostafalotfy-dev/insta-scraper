from enum import Enum
from typing import List, Any, Optional


class ContentType(Enum):
    COMMENT = "comment"


class Status(Enum):
    ACTIVE = "Active"


class FanClubInfo:
    fan_club_id: None
    fan_club_name: None
    is_fan_club_referral_eligible: None
    fan_consideration_page_revamp_eligiblity: None
    is_fan_club_gifting_eligible: None
    subscriber_count: None
    connected_member_count: None
    autosave_to_exclusive_highlight: None
    has_enough_subscribers_for_ssc: None

    def __init__(self, fan_club_id: None, fan_club_name: None, is_fan_club_referral_eligible: None, fan_consideration_page_revamp_eligiblity: None, is_fan_club_gifting_eligible: None, subscriber_count: None, connected_member_count: None, autosave_to_exclusive_highlight: None, has_enough_subscribers_for_ssc: None) -> None:
        self.fan_club_id = fan_club_id
        self.fan_club_name = fan_club_name
        self.is_fan_club_referral_eligible = is_fan_club_referral_eligible
        self.fan_consideration_page_revamp_eligiblity = fan_consideration_page_revamp_eligiblity
        self.is_fan_club_gifting_eligible = is_fan_club_gifting_eligible
        self.subscriber_count = subscriber_count
        self.connected_member_count = connected_member_count
        self.autosave_to_exclusive_highlight = autosave_to_exclusive_highlight
        self.has_enough_subscribers_for_ssc = has_enough_subscribers_for_ssc


class OwnerFriendshipStatus:
    following: bool
    is_bestie: bool
    is_restricted: bool
    is_feed_favorite: bool

    def __init__(self, following: bool, is_bestie: bool, is_restricted: bool, is_feed_favorite: bool) -> None:
        self.following = following
        self.is_bestie = is_bestie
        self.is_restricted = is_restricted
        self.is_feed_favorite = is_feed_favorite


class FullName(Enum):
    AHMED_HELMY = "Ahmed Helmy"
    A_BTALKS = "#ABtalks"


class HDProfilePicURLInfo:
    url: str
    width: int
    height: int

    def __init__(self, url: str, width: int, height: int) -> None:
        self.url = url
        self.width = width
        self.height = height


class ProfilePicID(Enum):
    THE_3032814614563212531_21855183607 = "3032814614563212531_21855183607"
    THE_3220833382307741349_754400498 = "3220833382307741349_754400498"


class Username(Enum):
    ABTALKS = "abtalks"
    AHMEDHELMY = "ahmedhelmy"


class Owner:
    fbid_v2: str
    feed_post_reshare_disabled: bool
    full_name: FullName
    id: str
    is_private: bool
    is_unpublished: bool
    pk: str
    pk_id: str
    show_account_transparency_details: bool
    strong_id: str
    third_party_downloads_enabled: int
    username: Username
    account_badges: List[Any]
    fan_club_info: FanClubInfo
    friendship_status: OwnerFriendshipStatus
    has_anonymous_profile_picture: bool
    hd_profile_pic_url_info: HDProfilePicURLInfo
    hd_profile_pic_versions: List[HDProfilePicURLInfo]
    is_favorite: bool
    is_verified: bool
    profile_pic_id: ProfilePicID
    profile_pic_url: str
    transparency_product_enabled: bool

    def __init__(self, fbid_v2: str, feed_post_reshare_disabled: bool, full_name: FullName, id: str, is_private: bool, is_unpublished: bool, pk: str, pk_id: str, show_account_transparency_details: bool, strong_id: str, third_party_downloads_enabled: int, username: Username, account_badges: List[Any], fan_club_info: FanClubInfo, friendship_status: OwnerFriendshipStatus, has_anonymous_profile_picture: bool, hd_profile_pic_url_info: HDProfilePicURLInfo, hd_profile_pic_versions: List[HDProfilePicURLInfo], is_favorite: bool, is_verified: bool, profile_pic_id: ProfilePicID, profile_pic_url: str, transparency_product_enabled: bool) -> None:
        self.fbid_v2 = fbid_v2
        self.feed_post_reshare_disabled = feed_post_reshare_disabled
        self.full_name = full_name
        self.id = id
        self.is_private = is_private
        self.is_unpublished = is_unpublished
        self.pk = pk
        self.pk_id = pk_id
        self.show_account_transparency_details = show_account_transparency_details
        self.strong_id = strong_id
        self.third_party_downloads_enabled = third_party_downloads_enabled
        self.username = username
        self.account_badges = account_badges
        self.fan_club_info = fan_club_info
        self.friendship_status = friendship_status
        self.has_anonymous_profile_picture = has_anonymous_profile_picture
        self.hd_profile_pic_url_info = hd_profile_pic_url_info
        self.hd_profile_pic_versions = hd_profile_pic_versions
        self.is_favorite = is_favorite
        self.is_verified = is_verified
        self.profile_pic_id = profile_pic_id
        self.profile_pic_url = profile_pic_url
        self.transparency_product_enabled = transparency_product_enabled


class Caption:
    pk: str
    user_id: str
    user: Owner
    type: int
    text: str
    did_report_as_spam: bool
    created_at: int
    created_at_utc: int
    content_type: ContentType
    status: Status
    bit_flags: int
    share_enabled: bool
    is_ranked_comment: bool
    is_covered: bool
    private_reply_status: int
    media_id: str
    has_translation: Optional[bool]

    def __init__(self, pk: str, user_id: str, user: Owner, type: int, text: str, did_report_as_spam: bool, created_at: int, created_at_utc: int, content_type: ContentType, status: Status, bit_flags: int, share_enabled: bool, is_ranked_comment: bool, is_covered: bool, private_reply_status: int, media_id: str, has_translation: Optional[bool]) -> None:
        self.pk = pk
        self.user_id = user_id
        self.user = user
        self.type = type
        self.text = text
        self.did_report_as_spam = did_report_as_spam
        self.created_at = created_at
        self.created_at_utc = created_at_utc
        self.content_type = content_type
        self.status = status
        self.bit_flags = bit_flags
        self.share_enabled = share_enabled
        self.is_ranked_comment = is_ranked_comment
        self.is_covered = is_covered
        self.private_reply_status = private_reply_status
        self.media_id = media_id
        self.has_translation = has_translation


class ClipsDeliveryParameters:
    pass

    def __init__(self, ) -> None:
        pass


class AchievementsInfo:
    show_achievements: bool
    num_earned_achievements: None

    def __init__(self, show_achievements: bool, num_earned_achievements: None) -> None:
        self.show_achievements = show_achievements
        self.num_earned_achievements = num_earned_achievements


class AudioReattributionInfo:
    should_allow_restore: bool

    def __init__(self, should_allow_restore: bool) -> None:
        self.should_allow_restore = should_allow_restore


class AdditionalAudioInfo:
    additional_audio_username: None
    audio_reattribution_info: AudioReattributionInfo

    def __init__(self, additional_audio_username: None, audio_reattribution_info: AudioReattributionInfo) -> None:
        self.additional_audio_username = additional_audio_username
        self.audio_reattribution_info = audio_reattribution_info


class AudioRankingInfo:
    best_audio_cluster_id: str

    def __init__(self, best_audio_cluster_id: str) -> None:
        self.best_audio_cluster_id = best_audio_cluster_id


class AudioType(Enum):
    LICENSED_MUSIC = "licensed_music"
    ORIGINAL_SOUNDS = "original_sounds"


class BrandedContentTagInfo:
    can_add_tag: bool

    def __init__(self, can_add_tag: bool) -> None:
        self.can_add_tag = can_add_tag


class ProductType(Enum):
    CLIPS = "clips"
    FEED = "feed"


class ContentAppreciationInfo:
    enabled: bool
    entry_point_container: None

    def __init__(self, enabled: bool, entry_point_container: None) -> None:
        self.enabled = enabled
        self.entry_point_container = entry_point_container


class MashupInfo:
    mashups_allowed: bool
    can_toggle_mashups_allowed: bool
    has_been_mashed_up: bool
    is_light_weight_check: bool
    formatted_mashups_count: None
    original_media: None
    privacy_filtered_mashups_media_count: None
    non_privacy_filtered_mashups_media_count: Optional[int]
    mashup_type: None
    is_creator_requesting_mashup: bool
    has_nonmimicable_additional_audio: bool
    is_pivot_page_available: bool

    def __init__(self, mashups_allowed: bool, can_toggle_mashups_allowed: bool, has_been_mashed_up: bool, is_light_weight_check: bool, formatted_mashups_count: None, original_media: None, privacy_filtered_mashups_media_count: None, non_privacy_filtered_mashups_media_count: Optional[int], mashup_type: None, is_creator_requesting_mashup: bool, has_nonmimicable_additional_audio: bool, is_pivot_page_available: bool) -> None:
        self.mashups_allowed = mashups_allowed
        self.can_toggle_mashups_allowed = can_toggle_mashups_allowed
        self.has_been_mashed_up = has_been_mashed_up
        self.is_light_weight_check = is_light_weight_check
        self.formatted_mashups_count = formatted_mashups_count
        self.original_media = original_media
        self.privacy_filtered_mashups_media_count = privacy_filtered_mashups_media_count
        self.non_privacy_filtered_mashups_media_count = non_privacy_filtered_mashups_media_count
        self.mashup_type = mashup_type
        self.is_creator_requesting_mashup = is_creator_requesting_mashup
        self.has_nonmimicable_additional_audio = has_nonmimicable_additional_audio
        self.is_pivot_page_available = is_pivot_page_available


class MusicAssetInfo:
    audio_asset_id: str
    audio_cluster_id: str
    id: str
    title: str
    sanitized_title: None
    subtitle: str
    display_artist: str
    artist_id: str
    is_explicit: bool
    cover_artwork_uri: str
    cover_artwork_thumbnail_uri: str
    progressive_download_url: str
    reactive_audio_download_url: None
    fast_start_progressive_download_url: str
    web_30_s_preview_download_url: str
    highlight_start_times_in_ms: List[int]
    dash_manifest: None
    has_lyrics: bool
    duration_in_ms: int
    dark_message: None
    allows_saving: bool
    ig_username: str
    is_eligible_for_audio_effects: bool

    def __init__(self, audio_asset_id: str, audio_cluster_id: str, id: str, title: str, sanitized_title: None, subtitle: str, display_artist: str, artist_id: str, is_explicit: bool, cover_artwork_uri: str, cover_artwork_thumbnail_uri: str, progressive_download_url: str, reactive_audio_download_url: None, fast_start_progressive_download_url: str, web_30_s_preview_download_url: str, highlight_start_times_in_ms: List[int], dash_manifest: None, has_lyrics: bool, duration_in_ms: int, dark_message: None, allows_saving: bool, ig_username: str, is_eligible_for_audio_effects: bool) -> None:
        self.audio_asset_id = audio_asset_id
        self.audio_cluster_id = audio_cluster_id
        self.id = id
        self.title = title
        self.sanitized_title = sanitized_title
        self.subtitle = subtitle
        self.display_artist = display_artist
        self.artist_id = artist_id
        self.is_explicit = is_explicit
        self.cover_artwork_uri = cover_artwork_uri
        self.cover_artwork_thumbnail_uri = cover_artwork_thumbnail_uri
        self.progressive_download_url = progressive_download_url
        self.reactive_audio_download_url = reactive_audio_download_url
        self.fast_start_progressive_download_url = fast_start_progressive_download_url
        self.web_30_s_preview_download_url = web_30_s_preview_download_url
        self.highlight_start_times_in_ms = highlight_start_times_in_ms
        self.dash_manifest = dash_manifest
        self.has_lyrics = has_lyrics
        self.duration_in_ms = duration_in_ms
        self.dark_message = dark_message
        self.allows_saving = allows_saving
        self.ig_username = ig_username
        self.is_eligible_for_audio_effects = is_eligible_for_audio_effects


class AudioMutingInfo:
    mute_audio: bool
    mute_reason_str: str
    allow_audio_editing: bool
    show_muted_audio_toast: bool

    def __init__(self, mute_audio: bool, mute_reason_str: str, allow_audio_editing: bool, show_muted_audio_toast: bool) -> None:
        self.mute_audio = mute_audio
        self.mute_reason_str = mute_reason_str
        self.allow_audio_editing = allow_audio_editing
        self.show_muted_audio_toast = show_muted_audio_toast


class FacepileTopLikerFriendshipStatus:
    following: bool
    followed_by: bool
    blocking: bool
    muting: bool
    is_private: bool
    incoming_request: bool
    outgoing_request: bool
    is_bestie: bool
    is_restricted: bool
    is_feed_favorite: bool

    def __init__(self, following: bool, followed_by: bool, blocking: bool, muting: bool, is_private: bool, incoming_request: bool, outgoing_request: bool, is_bestie: bool, is_restricted: bool, is_feed_favorite: bool) -> None:
        self.following = following
        self.followed_by = followed_by
        self.blocking = blocking
        self.muting = muting
        self.is_private = is_private
        self.incoming_request = incoming_request
        self.outgoing_request = outgoing_request
        self.is_bestie = is_bestie
        self.is_restricted = is_restricted
        self.is_feed_favorite = is_feed_favorite


class FacepileTopLiker:
    pk: str
    pk_id: str
    username: str
    full_name: str
    is_private: bool
    strong_id: str
    is_verified: bool
    profile_pic_id: Optional[str]
    profile_pic_url: str
    fbid_v2: Optional[str]
    friendship_status: Optional[FacepileTopLikerFriendshipStatus]

    def __init__(self, pk: str, pk_id: str, username: str, full_name: str, is_private: bool, strong_id: str, is_verified: bool, profile_pic_id: Optional[str], profile_pic_url: str, fbid_v2: Optional[str], friendship_status: Optional[FacepileTopLikerFriendshipStatus]) -> None:
        self.pk = pk
        self.pk_id = pk_id
        self.username = username
        self.full_name = full_name
        self.is_private = is_private
        self.strong_id = strong_id
        self.is_verified = is_verified
        self.profile_pic_id = profile_pic_id
        self.profile_pic_url = profile_pic_url
        self.fbid_v2 = fbid_v2
        self.friendship_status = friendship_status


class MusicConsumptionInfo:
    ig_artist: FacepileTopLiker
    placeholder_profile_pic_url: str
    should_mute_audio: bool
    should_mute_audio_reason: str
    should_mute_audio_reason_type: None
    is_bookmarked: bool
    overlap_duration_in_ms: int
    audio_asset_start_time_in_ms: int
    allow_media_creation_with_music: bool
    is_trending_in_clips: bool
    trend_rank: None
    formatted_clips_media_count: None
    display_labels: None
    should_allow_music_editing: bool
    derived_content_id: None
    audio_filter_infos: List[Any]
    audio_muting_info: AudioMutingInfo
    contains_lyrics: None

    def __init__(self, ig_artist: FacepileTopLiker, placeholder_profile_pic_url: str, should_mute_audio: bool, should_mute_audio_reason: str, should_mute_audio_reason_type: None, is_bookmarked: bool, overlap_duration_in_ms: int, audio_asset_start_time_in_ms: int, allow_media_creation_with_music: bool, is_trending_in_clips: bool, trend_rank: None, formatted_clips_media_count: None, display_labels: None, should_allow_music_editing: bool, derived_content_id: None, audio_filter_infos: List[Any], audio_muting_info: AudioMutingInfo, contains_lyrics: None) -> None:
        self.ig_artist = ig_artist
        self.placeholder_profile_pic_url = placeholder_profile_pic_url
        self.should_mute_audio = should_mute_audio
        self.should_mute_audio_reason = should_mute_audio_reason
        self.should_mute_audio_reason_type = should_mute_audio_reason_type
        self.is_bookmarked = is_bookmarked
        self.overlap_duration_in_ms = overlap_duration_in_ms
        self.audio_asset_start_time_in_ms = audio_asset_start_time_in_ms
        self.allow_media_creation_with_music = allow_media_creation_with_music
        self.is_trending_in_clips = is_trending_in_clips
        self.trend_rank = trend_rank
        self.formatted_clips_media_count = formatted_clips_media_count
        self.display_labels = display_labels
        self.should_allow_music_editing = should_allow_music_editing
        self.derived_content_id = derived_content_id
        self.audio_filter_infos = audio_filter_infos
        self.audio_muting_info = audio_muting_info
        self.contains_lyrics = contains_lyrics


class MusicInfo:
    music_asset_info: MusicAssetInfo
    music_consumption_info: MusicConsumptionInfo
    music_canonical_id: None

    def __init__(self, music_asset_info: MusicAssetInfo, music_consumption_info: MusicConsumptionInfo, music_canonical_id: None) -> None:
        self.music_asset_info = music_asset_info
        self.music_consumption_info = music_consumption_info
        self.music_canonical_id = music_canonical_id


class ConsumptionInfo:
    is_bookmarked: bool
    should_mute_audio_reason: str
    is_trending_in_clips: bool
    should_mute_audio_reason_type: None
    display_media_id: None

    def __init__(self, is_bookmarked: bool, should_mute_audio_reason: str, is_trending_in_clips: bool, should_mute_audio_reason_type: None, display_media_id: None) -> None:
        self.is_bookmarked = is_bookmarked
        self.should_mute_audio_reason = should_mute_audio_reason
        self.is_trending_in_clips = is_trending_in_clips
        self.should_mute_audio_reason_type = should_mute_audio_reason_type
        self.display_media_id = display_media_id


class OriginalAudioSubtype(Enum):
    DEFAULT = "default"


class OriginalAudioTitle(Enum):
    AHMED_HELMY_TRAILER = "Ahmed Helmy Trailer"
    HUMAN_BEHIND_THE_TITLE_AHMED_HELMY = "Human Behind The Title: Ahmed Helmy"
    ORIGINAL_AUDIO = "Original audio"


class OriginalSoundInfo:
    audio_asset_id: str
    music_canonical_id: None
    progressive_download_url: str
    dash_manifest: str
    ig_artist: FacepileTopLiker
    should_mute_audio: bool
    original_media_id: str
    hide_remixing: bool
    duration_in_ms: int
    time_created: int
    original_audio_title: OriginalAudioTitle
    consumption_info: ConsumptionInfo
    allow_creator_to_rename: bool
    can_remix_be_shared_to_fb: bool
    can_remix_be_shared_to_fb_expansion: bool
    formatted_clips_media_count: None
    audio_parts: List[Any]
    is_explicit: bool
    original_audio_subtype: OriginalAudioSubtype
    is_audio_automatically_attributed: bool
    is_reuse_disabled: bool
    is_xpost_from_fb: bool
    xpost_fb_creator_info: None
    is_original_audio_download_eligible: bool
    trend_rank: None
    audio_filter_infos: List[Any]
    oa_owner_is_music_artist: bool
    is_eligible_for_audio_effects: bool

    def __init__(self, audio_asset_id: str, music_canonical_id: None, progressive_download_url: str, dash_manifest: str, ig_artist: FacepileTopLiker, should_mute_audio: bool, original_media_id: str, hide_remixing: bool, duration_in_ms: int, time_created: int, original_audio_title: OriginalAudioTitle, consumption_info: ConsumptionInfo, allow_creator_to_rename: bool, can_remix_be_shared_to_fb: bool, can_remix_be_shared_to_fb_expansion: bool, formatted_clips_media_count: None, audio_parts: List[Any], is_explicit: bool, original_audio_subtype: OriginalAudioSubtype, is_audio_automatically_attributed: bool, is_reuse_disabled: bool, is_xpost_from_fb: bool, xpost_fb_creator_info: None, is_original_audio_download_eligible: bool, trend_rank: None, audio_filter_infos: List[Any], oa_owner_is_music_artist: bool, is_eligible_for_audio_effects: bool) -> None:
        self.audio_asset_id = audio_asset_id
        self.music_canonical_id = music_canonical_id
        self.progressive_download_url = progressive_download_url
        self.dash_manifest = dash_manifest
        self.ig_artist = ig_artist
        self.should_mute_audio = should_mute_audio
        self.original_media_id = original_media_id
        self.hide_remixing = hide_remixing
        self.duration_in_ms = duration_in_ms
        self.time_created = time_created
        self.original_audio_title = original_audio_title
        self.consumption_info = consumption_info
        self.allow_creator_to_rename = allow_creator_to_rename
        self.can_remix_be_shared_to_fb = can_remix_be_shared_to_fb
        self.can_remix_be_shared_to_fb_expansion = can_remix_be_shared_to_fb_expansion
        self.formatted_clips_media_count = formatted_clips_media_count
        self.audio_parts = audio_parts
        self.is_explicit = is_explicit
        self.original_audio_subtype = original_audio_subtype
        self.is_audio_automatically_attributed = is_audio_automatically_attributed
        self.is_reuse_disabled = is_reuse_disabled
        self.is_xpost_from_fb = is_xpost_from_fb
        self.xpost_fb_creator_info = xpost_fb_creator_info
        self.is_original_audio_download_eligible = is_original_audio_download_eligible
        self.trend_rank = trend_rank
        self.audio_filter_infos = audio_filter_infos
        self.oa_owner_is_music_artist = oa_owner_is_music_artist
        self.is_eligible_for_audio_effects = is_eligible_for_audio_effects


class Color:
    count: int
    hex_rgba_color: str

    def __init__(self, count: int, hex_rgba_color: str) -> None:
        self.count = count
        self.hex_rgba_color = hex_rgba_color


class ReusableTextInfo:
    id: str
    text: str
    start_time_ms: float
    end_time_ms: float
    width: float
    height: float
    offset_x: float
    offset_y: float
    z_index: int
    rotation_degree: float
    scale: float
    alignment: str
    colors: List[Color]
    text_format_type: str
    font_size: float
    text_emphasis_mode: str
    is_animated: int

    def __init__(self, id: str, text: str, start_time_ms: float, end_time_ms: float, width: float, height: float, offset_x: float, offset_y: float, z_index: int, rotation_degree: float, scale: float, alignment: str, colors: List[Color], text_format_type: str, font_size: float, text_emphasis_mode: str, is_animated: int) -> None:
        self.id = id
        self.text = text
        self.start_time_ms = start_time_ms
        self.end_time_ms = end_time_ms
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.z_index = z_index
        self.rotation_degree = rotation_degree
        self.scale = scale
        self.alignment = alignment
        self.colors = colors
        self.text_format_type = text_format_type
        self.font_size = font_size
        self.text_emphasis_mode = text_emphasis_mode
        self.is_animated = is_animated


class ClipsMetadata:
    music_info: Optional[MusicInfo]
    original_sound_info: Optional[OriginalSoundInfo]
    audio_type: AudioType
    music_canonical_id: str
    featured_label: None
    mashup_info: MashupInfo
    reusable_text_info: Optional[List[ReusableTextInfo]]
    reusable_text_attribute_string: Optional[str]
    nux_info: None
    viewer_interaction_settings: None
    branded_content_tag_info: BrandedContentTagInfo
    shopping_info: None
    additional_audio_info: AdditionalAudioInfo
    is_shared_to_fb: bool
    breaking_content_info: None
    challenge_info: None
    reels_on_the_rise_info: None
    breaking_creator_info: None
    asset_recommendation_info: None
    contextual_highlight_info: None
    clips_creation_entry_point: ProductType
    audio_ranking_info: AudioRankingInfo
    template_info: None
    is_fan_club_promo_video: bool
    disable_use_in_clips_client_cache: bool
    content_appreciation_info: ContentAppreciationInfo
    achievements_info: AchievementsInfo
    show_achievements: bool
    show_tips: None
    merchandising_pill_info: None
    is_public_chat_welcome_video: bool
    professional_clips_upsell_type: int
    external_media_info: None
    cutout_sticker_info: None

    def __init__(self, music_info: Optional[MusicInfo], original_sound_info: Optional[OriginalSoundInfo], audio_type: AudioType, music_canonical_id: str, featured_label: None, mashup_info: MashupInfo, reusable_text_info: Optional[List[ReusableTextInfo]], reusable_text_attribute_string: Optional[str], nux_info: None, viewer_interaction_settings: None, branded_content_tag_info: BrandedContentTagInfo, shopping_info: None, additional_audio_info: AdditionalAudioInfo, is_shared_to_fb: bool, breaking_content_info: None, challenge_info: None, reels_on_the_rise_info: None, breaking_creator_info: None, asset_recommendation_info: None, contextual_highlight_info: None, clips_creation_entry_point: ProductType, audio_ranking_info: AudioRankingInfo, template_info: None, is_fan_club_promo_video: bool, disable_use_in_clips_client_cache: bool, content_appreciation_info: ContentAppreciationInfo, achievements_info: AchievementsInfo, show_achievements: bool, show_tips: None, merchandising_pill_info: None, is_public_chat_welcome_video: bool, professional_clips_upsell_type: int, external_media_info: None, cutout_sticker_info: None) -> None:
        self.music_info = music_info
        self.original_sound_info = original_sound_info
        self.audio_type = audio_type
        self.music_canonical_id = music_canonical_id
        self.featured_label = featured_label
        self.mashup_info = mashup_info
        self.reusable_text_info = reusable_text_info
        self.reusable_text_attribute_string = reusable_text_attribute_string
        self.nux_info = nux_info
        self.viewer_interaction_settings = viewer_interaction_settings
        self.branded_content_tag_info = branded_content_tag_info
        self.shopping_info = shopping_info
        self.additional_audio_info = additional_audio_info
        self.is_shared_to_fb = is_shared_to_fb
        self.breaking_content_info = breaking_content_info
        self.challenge_info = challenge_info
        self.reels_on_the_rise_info = reels_on_the_rise_info
        self.breaking_creator_info = breaking_creator_info
        self.asset_recommendation_info = asset_recommendation_info
        self.contextual_highlight_info = contextual_highlight_info
        self.clips_creation_entry_point = clips_creation_entry_point
        self.audio_ranking_info = audio_ranking_info
        self.template_info = template_info
        self.is_fan_club_promo_video = is_fan_club_promo_video
        self.disable_use_in_clips_client_cache = disable_use_in_clips_client_cache
        self.content_appreciation_info = content_appreciation_info
        self.achievements_info = achievements_info
        self.show_achievements = show_achievements
        self.show_tips = show_tips
        self.merchandising_pill_info = merchandising_pill_info
        self.is_public_chat_welcome_video = is_public_chat_welcome_video
        self.professional_clips_upsell_type = professional_clips_upsell_type
        self.external_media_info = external_media_info
        self.cutout_sticker_info = cutout_sticker_info


class CommentInformTreatment:
    should_have_inform_treatment: bool
    text: str
    url: None
    action_type: None

    def __init__(self, should_have_inform_treatment: bool, text: str, url: None, action_type: None) -> None:
        self.should_have_inform_treatment = should_have_inform_treatment
        self.text = text
        self.url = url
        self.action_type = action_type


class Comment:
    pk: str
    user_id: str
    type: int
    did_report_as_spam: bool
    created_at: int
    created_at_utc: int
    content_type: ContentType
    status: Status
    bit_flags: int
    share_enabled: bool
    is_ranked_comment: bool
    media_id: str
    user: FacepileTopLiker
    text: str
    is_covered: bool
    has_translation: Optional[bool]
    parent_comment_id: Optional[str]
    replied_to_comment_id: Optional[str]
    reply_root_comment_id: Optional[str]

    def __init__(self, pk: str, user_id: str, type: int, did_report_as_spam: bool, created_at: int, created_at_utc: int, content_type: ContentType, status: Status, bit_flags: int, share_enabled: bool, is_ranked_comment: bool, media_id: str, user: FacepileTopLiker, text: str, is_covered: bool, has_translation: Optional[bool], parent_comment_id: Optional[str], replied_to_comment_id: Optional[str], reply_root_comment_id: Optional[str]) -> None:
        self.pk = pk
        self.user_id = user_id
        self.type = type
        self.did_report_as_spam = did_report_as_spam
        self.created_at = created_at
        self.created_at_utc = created_at_utc
        self.content_type = content_type
        self.status = status
        self.bit_flags = bit_flags
        self.share_enabled = share_enabled
        self.is_ranked_comment = is_ranked_comment
        self.media_id = media_id
        self.user = user
        self.text = text
        self.is_covered = is_covered
        self.has_translation = has_translation
        self.parent_comment_id = parent_comment_id
        self.replied_to_comment_id = replied_to_comment_id
        self.reply_root_comment_id = reply_root_comment_id


class CommercialityStatus(Enum):
    NOT_COMMERCIAL = "not_commercial"


class CreativeConfig:
    capture_type: str
    creation_tool_info: List[Any]
    effect_ids: Optional[List[int]]

    def __init__(self, capture_type: str, creation_tool_info: List[Any], effect_ids: Optional[List[int]]) -> None:
        self.capture_type = capture_type
        self.creation_tool_info = creation_tool_info
        self.effect_ids = effect_ids


class In:
    user: FacepileTopLiker
    position: List[float]
    start_time_in_video_in_sec: None
    duration_in_video_in_sec: None

    def __init__(self, user: FacepileTopLiker, position: List[float], start_time_in_video_in_sec: None, duration_in_video_in_sec: None) -> None:
        self.user = user
        self.position = position
        self.start_time_in_video_in_sec = start_time_in_video_in_sec
        self.duration_in_video_in_sec = duration_in_video_in_sec


class Tags:
    tags_in: List[In]

    def __init__(self, tags_in: List[In]) -> None:
        self.tags_in = tags_in


class HighlightsInfo:
    added_to: List[Any]

    def __init__(self, added_to: List[Any]) -> None:
        self.added_to = added_to


class AdditionalCandidates:
    igtv_first_frame: HDProfilePicURLInfo
    first_frame: HDProfilePicURLInfo
    smart_frame: None

    def __init__(self, igtv_first_frame: HDProfilePicURLInfo, first_frame: HDProfilePicURLInfo, smart_frame: None) -> None:
        self.igtv_first_frame = igtv_first_frame
        self.first_frame = first_frame
        self.smart_frame = smart_frame


class Default:
    video_length: float
    thumbnail_width: int
    thumbnail_height: int
    thumbnail_duration: float
    sprite_urls: List[str]
    thumbnails_per_row: int
    total_thumbnail_num_per_sprite: int
    max_thumbnails_per_sprite: int
    sprite_width: int
    sprite_height: int
    rendered_width: int
    file_size_kb: int

    def __init__(self, video_length: float, thumbnail_width: int, thumbnail_height: int, thumbnail_duration: float, sprite_urls: List[str], thumbnails_per_row: int, total_thumbnail_num_per_sprite: int, max_thumbnails_per_sprite: int, sprite_width: int, sprite_height: int, rendered_width: int, file_size_kb: int) -> None:
        self.video_length = video_length
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        self.thumbnail_duration = thumbnail_duration
        self.sprite_urls = sprite_urls
        self.thumbnails_per_row = thumbnails_per_row
        self.total_thumbnail_num_per_sprite = total_thumbnail_num_per_sprite
        self.max_thumbnails_per_sprite = max_thumbnails_per_sprite
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.rendered_width = rendered_width
        self.file_size_kb = file_size_kb


class ScrubberSpritesheetInfoCandidates:
    default: Default

    def __init__(self, default: Default) -> None:
        self.default = default


class ImageVersions2:
    candidates: List[HDProfilePicURLInfo]
    additional_candidates: AdditionalCandidates
    smart_thumbnail_enabled: bool
    scrubber_spritesheet_info_candidates: Optional[ScrubberSpritesheetInfoCandidates]

    def __init__(self, candidates: List[HDProfilePicURLInfo], additional_candidates: AdditionalCandidates, smart_thumbnail_enabled: bool, scrubber_spritesheet_info_candidates: Optional[ScrubberSpritesheetInfoCandidates]) -> None:
        self.candidates = candidates
        self.additional_candidates = additional_candidates
        self.smart_thumbnail_enabled = smart_thumbnail_enabled
        self.scrubber_spritesheet_info_candidates = scrubber_spritesheet_info_candidates


class IntegrityReviewDecision(Enum):
    PENDING = "pending"


class Location:
    pk: str
    short_name: str
    facebook_places_id: str
    external_source: str
    name: str
    address: str
    city: str
    has_viewer_saved: bool
    lng: float
    lat: float
    is_eligible_for_guides: bool

    def __init__(self, pk: str, short_name: str, facebook_places_id: str, external_source: str, name: str, address: str, city: str, has_viewer_saved: bool, lng: float, lat: float, is_eligible_for_guides: bool) -> None:
        self.pk = pk
        self.short_name = short_name
        self.facebook_places_id = facebook_places_id
        self.external_source = external_source
        self.name = name
        self.address = address
        self.city = city
        self.has_viewer_saved = has_viewer_saved
        self.lng = lng
        self.lat = lat
        self.is_eligible_for_guides = is_eligible_for_guides


class LoggingInfoToken(Enum):
    GC_BK_OW_ZM_N2_ZH_NTU1_YTY0_OT_MX_OGY4_M_TG5_ZJ_YX_MW_IZ_NJ_RJ_ZAA = "GCBkOWZmN2ZhNTU1YTY0OTMxOGY4MTg5ZjYxMWIzNjRjZAA="


class GiftCountVisibility(Enum):
    ENABLED = "enabled"


class MediaGiftingState(Enum):
    NOT_APPLICABLE = "not_applicable"


class MediaAppreciationSettings:
    media_gifting_state: MediaGiftingState
    gift_count_visibility: GiftCountVisibility

    def __init__(self, media_gifting_state: MediaGiftingState, gift_count_visibility: GiftCountVisibility) -> None:
        self.media_gifting_state = media_gifting_state
        self.gift_count_visibility = gift_count_visibility


class SquareCrop:
    crop_left: float
    crop_right: float
    crop_top: float
    crop_bottom: float

    def __init__(self, crop_left: float, crop_right: float, crop_top: float, crop_bottom: float) -> None:
        self.crop_left = crop_left
        self.crop_right = crop_right
        self.crop_top = crop_top
        self.crop_bottom = crop_bottom


class MediaCroppingInfo:
    square_crop: SquareCrop

    def __init__(self, square_crop: SquareCrop) -> None:
        self.square_crop = square_crop


class OpenCarouselSubmissionState(Enum):
    CLOSED = "closed"


class SharingFrictionInfo:
    should_have_sharing_friction: bool
    bloks_app_url: None
    sharing_friction_payload: None

    def __init__(self, should_have_sharing_friction: bool, bloks_app_url: None, sharing_friction_payload: None) -> None:
        self.should_have_sharing_friction = should_have_sharing_friction
        self.bloks_app_url = bloks_app_url
        self.sharing_friction_payload = sharing_friction_payload


class VideoCodec(Enum):
    AVC1_64001_E = "avc1.64001e"
    AVC1_64001_F = "avc1.64001f"


class VideoVersion:
    type: int
    width: int
    height: int
    url: str
    id: str

    def __init__(self, type: int, width: int, height: int, url: str, id: str) -> None:
        self.type = type
        self.width = width
        self.height = height
        self.url = url
        self.id = id


class Media:
    taken_at: int
    pk: str
    id: str
    device_timestamp: int
    client_cache_key: str
    filter_type: int
    caption_is_edited: bool
    like_and_view_counts_disabled: bool
    strong_id: str
    is_reshare_of_text_post_app_media_in_ig: bool
    is_post_live_clips_media: bool
    deleted_reason: int
    integrity_review_decision: IntegrityReviewDecision
    has_shared_to_fb: int
    is_unified_video: bool
    should_request_ads: bool
    is_visual_reply_commenter_notice_enabled: bool
    commerciality_status: CommercialityStatus
    explore_hide_comments: bool
    has_delayed_metadata: bool
    view_state_item_type: int
    logging_info_token: LoggingInfoToken
    clips_delivery_parameters: ClipsDeliveryParameters
    mezql_token: str
    shop_routing_user_id: None
    can_see_insights_as_brand: bool
    is_organic_product_tagging_eligible: bool
    fb_like_count: Optional[int]
    has_liked: bool
    has_privately_liked: bool
    like_count: int
    facepile_top_likers: List[FacepileTopLiker]
    top_likers: List[str]
    media_type: int
    code: str
    can_viewer_reshare: bool
    caption: Optional[Caption]
    clips_tab_pinned_user_ids: List[Any]
    comment_inform_treatment: CommentInformTreatment
    sharing_friction_info: SharingFrictionInfo
    play_count: int
    fb_play_count: Optional[int]
    media_appreciation_settings: MediaAppreciationSettings
    original_media_has_visual_reply_media: bool
    fb_user_tags: Tags
    invited_coauthor_producers: List[Any]
    can_viewer_save: bool
    is_in_profile_grid: bool
    profile_grid_control_enabled: bool
    featured_products: List[Any]
    is_comments_gif_composer_enabled: bool
    highlights_info: HighlightsInfo
    media_cropping_info: MediaCroppingInfo
    product_suggestions: List[Any]
    user: Owner
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    is_artist_pick: bool
    enable_media_notes_production: bool
    product_type: ProductType
    is_paid_partnership: bool
    music_metadata: None
    social_context: List[Any]
    organic_tracking_token: str
    is_third_party_downloads_eligible: bool
    ig_media_sharing_disabled: bool
    open_carousel_submission_state: OpenCarouselSubmissionState
    is_open_to_public_submission: bool
    comment_likes_enabled: bool
    comment_threading_enabled: bool
    max_num_visible_preview_comments: int
    has_more_comments: bool
    next_max_id: str
    preview_comments: List[Comment]
    comments: List[Comment]
    comment_count: int
    can_view_more_preview_comments: bool
    hide_view_all_comment_entrypoint: bool
    is_auto_created: bool
    is_cutout_sticker_allowed: bool
    enable_waist: bool
    owner: Owner
    is_dash_eligible: int
    video_dash_manifest: str
    video_codec: VideoCodec
    number_of_qualities: int
    video_versions: List[VideoVersion]
    video_duration: float
    has_audio: bool
    clips_metadata: ClipsMetadata
    usertags: Optional[Tags]
    photo_of_you: Optional[bool]
    coauthor_producers: Optional[List[FacepileTopLiker]]
    location: Optional[Location]
    commerce_integrity_review_decision: Optional[str]
    crosspost: Optional[List[str]]
    lng: Optional[float]
    lat: Optional[float]
    video_subtitles_confidence: Optional[float]
    creative_config: Optional[CreativeConfig]

    def __init__(self, taken_at: int, pk: str, id: str, device_timestamp: int, client_cache_key: str, filter_type: int, caption_is_edited: bool, like_and_view_counts_disabled: bool, strong_id: str, is_reshare_of_text_post_app_media_in_ig: bool, is_post_live_clips_media: bool, deleted_reason: int, integrity_review_decision: IntegrityReviewDecision, has_shared_to_fb: int, is_unified_video: bool, should_request_ads: bool, is_visual_reply_commenter_notice_enabled: bool, commerciality_status: CommercialityStatus, explore_hide_comments: bool, has_delayed_metadata: bool, view_state_item_type: int, logging_info_token: LoggingInfoToken, clips_delivery_parameters: ClipsDeliveryParameters, mezql_token: str, shop_routing_user_id: None, can_see_insights_as_brand: bool, is_organic_product_tagging_eligible: bool, fb_like_count: Optional[int], has_liked: bool, has_privately_liked: bool, like_count: int, facepile_top_likers: List[FacepileTopLiker], top_likers: List[str], media_type: int, code: str, can_viewer_reshare: bool, caption: Optional[Caption], clips_tab_pinned_user_ids: List[Any], comment_inform_treatment: CommentInformTreatment, sharing_friction_info: SharingFrictionInfo, play_count: int, fb_play_count: Optional[int], media_appreciation_settings: MediaAppreciationSettings, original_media_has_visual_reply_media: bool, fb_user_tags: Tags, invited_coauthor_producers: List[Any], can_viewer_save: bool, is_in_profile_grid: bool, profile_grid_control_enabled: bool, featured_products: List[Any], is_comments_gif_composer_enabled: bool, highlights_info: HighlightsInfo, media_cropping_info: MediaCroppingInfo, product_suggestions: List[Any], user: Owner, image_versions2: ImageVersions2, original_width: int, original_height: int, is_artist_pick: bool, enable_media_notes_production: bool, product_type: ProductType, is_paid_partnership: bool, music_metadata: None, social_context: List[Any], organic_tracking_token: str, is_third_party_downloads_eligible: bool, ig_media_sharing_disabled: bool, open_carousel_submission_state: OpenCarouselSubmissionState, is_open_to_public_submission: bool, comment_likes_enabled: bool, comment_threading_enabled: bool, max_num_visible_preview_comments: int, has_more_comments: bool, next_max_id: str, preview_comments: List[Comment], comments: List[Comment], comment_count: int, can_view_more_preview_comments: bool, hide_view_all_comment_entrypoint: bool, is_auto_created: bool, is_cutout_sticker_allowed: bool, enable_waist: bool, owner: Owner, is_dash_eligible: int, video_dash_manifest: str, video_codec: VideoCodec, number_of_qualities: int, video_versions: List[VideoVersion], video_duration: float, has_audio: bool, clips_metadata: ClipsMetadata, usertags: Optional[Tags], photo_of_you: Optional[bool], coauthor_producers: Optional[List[FacepileTopLiker]], location: Optional[Location], commerce_integrity_review_decision: Optional[str], crosspost: Optional[List[str]], lng: Optional[float], lat: Optional[float], video_subtitles_confidence: Optional[float], creative_config: Optional[CreativeConfig]) -> None:
        self.taken_at = taken_at
        self.pk = pk
        self.id = id
        self.device_timestamp = device_timestamp
        self.client_cache_key = client_cache_key
        self.filter_type = filter_type
        self.caption_is_edited = caption_is_edited
        self.like_and_view_counts_disabled = like_and_view_counts_disabled
        self.strong_id = strong_id
        self.is_reshare_of_text_post_app_media_in_ig = is_reshare_of_text_post_app_media_in_ig
        self.is_post_live_clips_media = is_post_live_clips_media
        self.deleted_reason = deleted_reason
        self.integrity_review_decision = integrity_review_decision
        self.has_shared_to_fb = has_shared_to_fb
        self.is_unified_video = is_unified_video
        self.should_request_ads = should_request_ads
        self.is_visual_reply_commenter_notice_enabled = is_visual_reply_commenter_notice_enabled
        self.commerciality_status = commerciality_status
        self.explore_hide_comments = explore_hide_comments
        self.has_delayed_metadata = has_delayed_metadata
        self.view_state_item_type = view_state_item_type
        self.logging_info_token = logging_info_token
        self.clips_delivery_parameters = clips_delivery_parameters
        self.mezql_token = mezql_token
        self.shop_routing_user_id = shop_routing_user_id
        self.can_see_insights_as_brand = can_see_insights_as_brand
        self.is_organic_product_tagging_eligible = is_organic_product_tagging_eligible
        self.fb_like_count = fb_like_count
        self.has_liked = has_liked
        self.has_privately_liked = has_privately_liked
        self.like_count = like_count
        self.facepile_top_likers = facepile_top_likers
        self.top_likers = top_likers
        self.media_type = media_type
        self.code = code
        self.can_viewer_reshare = can_viewer_reshare
        self.caption = caption
        self.clips_tab_pinned_user_ids = clips_tab_pinned_user_ids
        self.comment_inform_treatment = comment_inform_treatment
        self.sharing_friction_info = sharing_friction_info
        self.play_count = play_count
        self.fb_play_count = fb_play_count
        self.media_appreciation_settings = media_appreciation_settings
        self.original_media_has_visual_reply_media = original_media_has_visual_reply_media
        self.fb_user_tags = fb_user_tags
        self.invited_coauthor_producers = invited_coauthor_producers
        self.can_viewer_save = can_viewer_save
        self.is_in_profile_grid = is_in_profile_grid
        self.profile_grid_control_enabled = profile_grid_control_enabled
        self.featured_products = featured_products
        self.is_comments_gif_composer_enabled = is_comments_gif_composer_enabled
        self.highlights_info = highlights_info
        self.media_cropping_info = media_cropping_info
        self.product_suggestions = product_suggestions
        self.user = user
        self.image_versions2 = image_versions2
        self.original_width = original_width
        self.original_height = original_height
        self.is_artist_pick = is_artist_pick
        self.enable_media_notes_production = enable_media_notes_production
        self.product_type = product_type
        self.is_paid_partnership = is_paid_partnership
        self.music_metadata = music_metadata
        self.social_context = social_context
        self.organic_tracking_token = organic_tracking_token
        self.is_third_party_downloads_eligible = is_third_party_downloads_eligible
        self.ig_media_sharing_disabled = ig_media_sharing_disabled
        self.open_carousel_submission_state = open_carousel_submission_state
        self.is_open_to_public_submission = is_open_to_public_submission
        self.comment_likes_enabled = comment_likes_enabled
        self.comment_threading_enabled = comment_threading_enabled
        self.max_num_visible_preview_comments = max_num_visible_preview_comments
        self.has_more_comments = has_more_comments
        self.next_max_id = next_max_id
        self.preview_comments = preview_comments
        self.comments = comments
        self.comment_count = comment_count
        self.can_view_more_preview_comments = can_view_more_preview_comments
        self.hide_view_all_comment_entrypoint = hide_view_all_comment_entrypoint
        self.is_auto_created = is_auto_created
        self.is_cutout_sticker_allowed = is_cutout_sticker_allowed
        self.enable_waist = enable_waist
        self.owner = owner
        self.is_dash_eligible = is_dash_eligible
        self.video_dash_manifest = video_dash_manifest
        self.video_codec = video_codec
        self.number_of_qualities = number_of_qualities
        self.video_versions = video_versions
        self.video_duration = video_duration
        self.has_audio = has_audio
        self.clips_metadata = clips_metadata
        self.usertags = usertags
        self.photo_of_you = photo_of_you
        self.coauthor_producers = coauthor_producers
        self.location = location
        self.commerce_integrity_review_decision = commerce_integrity_review_decision
        self.crosspost = crosspost
        self.lng = lng
        self.lat = lat
        self.video_subtitles_confidence = video_subtitles_confidence
        self.creative_config = creative_config


class Item:
    media: Media

    def __init__(self, media: Media) -> None:
        self.media = media


class PagingInfo:
    max_id: str
    more_available: bool

    def __init__(self, max_id: str, more_available: bool) -> None:
        self.max_id = max_id
        self.more_available = more_available


class Api:
    items: List[Item]
    paging_info: PagingInfo
    status: str

    def __init__(self, items: List[Item], paging_info: PagingInfo, status: str) -> None:
        self.items = items
        self.paging_info = paging_info
        self.status = status
