from typing import List

import requests
#
# from Models.Media import Api, PagingInfo, Item, Media, Owner, HDProfilePicURLInfo, ProfilePicID, FanClubInfo, Comment, \
#     FacepileTopLiker, ClipsMetadata, MusicInfo, MusicConsumptionInfo
# from Profile import Profile
from Request import Request


class Clips(Request):
    ids: List[int]

    def __init__(self):
        super().__init__()
        self.prefix = "api/v1/clips/user/"

    def ids(self):
        return self.ids

    def get(self, ids: [int]):

        body: dict = {
            "page_size": "1000",
            "target_user_id": str(ids),
            "include_feed_video": "true",
        }
        data = requests.post(self.host_name + self.prefix, data=body, headers=self.headers)

        try:
            self.res = data.json()

            for item in self.res["items"]:
                yield item
        except:
            print(f"status {data.status_code}")
            self.get(ids)
        # yield Api(status=self.res["status"],
        #           paging_info=PagingInfo(max_id=self.res["paging_info"]["max_id"],
        #                                  more_available=self.res["paging_info"]["more_available"])
        #           ,
        #           items=[Item(media=Media(taken_at=self.res["taken_at"], id=self.res["id"],
        #                                   media_type=self.res["media_type"]
        #                                   ,
        #                                   user=Owner(id=media["user"]["id"], is_private=media["user"]["is_private"],
        #                                              is_verified=media["user"]["is_verified"],
        #                                              full_name=media["user"]["full_name"],
        #                                              username=media["user"]["user_name"],
        #                                              profile_pic_url=media["user"]["profile_pic_url"]
        #                                              , show_account_transparency_details=media["user"][
        #                                           "show_account_transparency_details"]
        #                                              , is_unpublished=media["user"]["is_unpublished"]
        #                                              , pk=media["user"]["pk"]
        #                                              , account_badges=media["user"]["account_badges"]
        #                                              , hd_profile_pic_url_info=HDProfilePicURLInfo(
        #                                           url=media["user"]["url"]
        #                                           , width=media["user"][
        #                                               "width"]
        #                                           , height=media["user"][
        #                                               "height"])
        #                                              ,
        #
        #                                              fan_club_info=FanClubInfo(
        #                                                  fan_club_name=media["fan_club_info"]["fan_club_name"]
        #                                                  , fan_club_id=media["fan_club_info"]["fan_club_id"]
        #                                                  , is_fan_club_gifting_eligible=media["fan_club_info"][
        #                                                      "fan_club_info"]
        #                                                  , is_fan_club_referral_eligible=media["fan_club_info"][
        #                                                      "is_fan_club_referral_eligible"]
        #                                                  , fan_consideration_page_revamp_eligiblity=
        #                                                  media["fan_club_info"][
        #                                                      "fan_consideration_page_revamp_eligiblity"]
        #                                                  , has_enough_subscribers_for_ssc=media["fan_club_info"][
        #                                                      "has_enough_subscribers_for_ssc"],
        #                                                  subscriber_count=media["fan_club_info"]["subscriber_count"]
        #                                                  , connected_member_count=media["fan_club_info"][
        #                                                      "connected_member_count"]
        #                                                  , autosave_to_exclusive_highlight=media["fan_club_info"][
        #                                                      "autosave_to_exclusive_highlight"])
        #                                              , hd_profile_pic_versions=[
        #                                           HDProfilePicURLInfo(url=pic["url"], height=pic["width"],
        #                                                               width=pic["height"]) for pic in
        #                                           media["fan_club_info"]["hd_profile_pic_versions"]]
        #                                              , has_anonymous_profile_picture=media["fan_club_info"][
        #                                           "has_anonymous_profile_picture"],
        #                                              fbid_v2=media["fan_club_info"]["fbid_v2"],
        #                                              strong_id=media["fan_club_info"]["strong_id"],
        #                                              pk_id=media["fan_club_info"]["pk_id"],
        #                                              is_favorite=media["fan_club_info"]["is_favorite"],
        #                                              transparency_product_enabled=media["fan_club_info"][
        #                                                  "transparency_product_enabled"],
        #                                              third_party_downloads_enabled=media["fan_club_info"][
        #                                                  "third_party_downloads_enabled"],
        #                                              friendship_status=media["fan_club_info"]["friendship_status"],
        #                                              feed_post_reshare_disabled=media["fan_club_info"][
        #                                                  "friendship_status"]),
        #                                   strong_id=media["strong_id"], pk=media["pk"],
        #                                   highlights_info=media["highlights_info"],
        #                                   media_cropping_info=media["media_cropping_info"],
        #                                   logging_info_token=media["logging_info_token"],
        #                                   ig_media_sharing_disabled=media["ig_media_sharing_disabled"],
        #                                   sharing_friction_info=media["sharing_friction_info"],
        #                                   is_post_live_clips_media=media["is_post_live_clips_media"],
        #                                   media_appreciation_settings=media["media_appreciation_settings"],
        #                                   original_media_has_visual_reply_media=media[
        #                                       "original_media_has_visual_reply_media"],
        #                                   has_audio=media["has_audio"], has_liked=media["has_liked"],
        #                                   has_privately_liked=media["has_privately_liked"],
        #                                   has_shared_to_fb=media["has_shared_to_fb"],
        #                                   fb_like_count=media["fb_like_count"], like_count=media["like_count"],
        #                                   play_count=media["play_count"], fb_play_count=media["fb_play_count"],
        #                                   comment_count=media["comment_count"],
        #                                   comments=[Comment(pk=comment["pk"], status=comment["status"],
        #                                                     is_ranked_comment=comment["is_ranked_comment"],
        #                                                     parent_comment_id=comment["parent_comment_id"],
        #                                                     user=FacepileTopLiker(pk=comment["user"]["pk"],
        #                                                                           friendship_status=comment["user"][
        #                                                                               "friendship_status"],
        #                                                                           strong_id=comment["user"][
        #                                                                               "strong_id"],
        #                                                                           profile_pic_id=comment["user"][
        #                                                                               "profile_pic_id"],
        #                                                                           profile_pic_url=comment[
        #                                                                               "profile_pic_url"],
        #                                                                           fbid_v2=comment["fbid_v2"],
        #                                                                           pk_id=comment["pk_id"],
        #                                                                           full_name=comment["full_name"],
        #                                                                           is_private=comment["is_private"],
        #                                                                           is_verified=comment[
        #                                                                               "is_verified"],
        #                                                                           username=comment["username"]),
        #                                                     replied_to_comment_id=comment["replied_to_comment_id"],
        #                                                     reply_root_comment_id=comment["reply_root_comment_id"],
        #                                                     media_id=comment["media_id"],
        #                                                     user_id=comment["user_id"],
        #                                                     bit_flags=comment["bit_flags"],
        #                                                     created_at=comment["created_at"],
        #                                                     created_at_utc=comment["created_at_utc"],
        #                                                     is_covered=comment["is_covered"],
        #                                                     content_type=comment["content_type"],
        #                                                     type=comment["type"],
        #                                                     did_report_as_spam=comment["did_report_as_spam"],
        #                                                     share_enabled=comment["share_enabled"],
        #                                                     has_translation=comment["has_translation"],
        #                                                     text=comment["text"])
        #                                             for comment in
        #                                             media["comments"]], preview_comments=[
        #                   Comment(replied_to_comment_id=comment["replied_to_comment_id"],
        #                           is_ranked_comment=comment["is_ranked_comment"], media_id=comment["media_id"],
        #                           reply_root_comment_id=comment["reply_root_comment_id"],
        #                           has_translation=comment["has_translation"],
        #                           share_enabled=comment["share_enabled"],
        #                           did_report_as_spam=comment["did_report_as_spam"],
        #                           is_covered=comment["is_covered"], user_id=comment["user_id"],
        #                           text=comment["text"], bit_flags=comment["bit_flags"],
        #                           created_at=comment["created_at"], created_at_utc=comment["created_at_utc"],
        #                           content_type=comment["content_type"], type=comment["type"], user=comment["user"],
        #                           status=comment["status"], pk=comment["pk"],
        #                           parent_comment_id=comment["parent_comment_id"]) for comment in
        #                   media["preview_comments"]], has_more_comments=media["has_more_comments"],
        #                                   comment_inform_treatment=media["comment_inform_treatment"],
        #                                   comment_likes_enabled=media["comment_likes_enabled"],
        #                                   comment_threading_enabled=media["comment_threading_enabled"],
        #                                   is_comments_gif_composer_enabled=media[
        #                                       "is_comments_gif_composer_enabled"],
        #                                   enable_media_notes_production=media["enable_media_notes_production"],
        #                                   enable_waist=media["enable_waist"],
        #                                   explore_hide_comments=media["explore_hide_comments"],
        #                                   can_view_more_preview_comments=media["can_view_more_preview_comments"],
        #                                   hide_view_all_comment_entrypoint=media[
        #                                       "hide_view_all_comment_entrypoint"],
        #                                   max_num_visible_preview_comments=media[
        #                                       "max_num_visible_preview_comments"],
        #                                   is_reshare_of_text_post_app_media_in_ig=media[
        #                                       "is_reshare_of_text_post_app_media_in_ig"],
        #                                   profile_grid_control_enabled=media["profile_grid_control_enabled"],
        #                                   next_max_id=media["next_max_id"],
        #                                   view_state_item_type=media["view_state_item_type"],
        #                                   is_in_profile_grid=media["is_in_profile_grid"],
        #                                   product_type=media["product_type"],
        #                                   product_suggestions=media["product_suggestions"],
        #                                   featured_products=media["featured_products"],
        #                                   is_organic_product_tagging_eligible=media[
        #                                       "is_organic_product_tagging_eligible"],
        #                                   is_dash_eligible=media["is_dash_eligible"],
        #                                   fb_user_tags=media["fb_user_tags"],
        #                                   clips_tab_pinned_user_ids=media["clips_tab_pinned_user_ids"],
        #                                   clips_metadata=ClipsMetadata(
        #                                       external_media_info=media["clips_metadata"]["external_media_info"],
        #                                       music_info=[MusicInfo(music_consumption_info=MusicConsumptionInfo(
        #                                           is_trending_in_clips=media["music_info"]["is_trending_in_clips"],formatted_clips_media_count=media["music_info"]["formatted_clips_media_count"],allow_media_creation_with_music=media["music_info"][""]))])))
        #                  for
        #                  media in
        #                  self.res["items"]["media"]])
