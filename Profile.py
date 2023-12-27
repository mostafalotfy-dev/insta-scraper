from threading import Thread
from time import sleep
from typing import List

import requests

from Models.Profile import Api, Data, User
from Models.Search import UserElement
from Request import Request
from Search import Search

from random import random


class Profile(Request):
    profiles: List[UserElement]

    def __init__(self, name: str):
        super().__init__()
        self.prefix = "api/v1/users/web_profile_info/?username="
        try:
            self.profiles = Search(name).users()
        except:
            self.profiles = Search(name).users()

    def get(self):
        for profile in self.profiles:
            self.headers["User-Agent"] = f"{random()}"
            self.headers["X-Csrftoken"] = f"{random()}"

            try:
                data = requests.get(self.host_name + self.prefix + profile["user"]["username"], headers=self.headers)
                res = data.json()
                user: dict = res["data"]["user"]
                yield Api(status=res["status"],
                          user_dict=user,
                          data=Data(
                              user=User(ai_agent_type=user["ai_agent_type"], profile_pic_url=user["profile_pic_url"],
                                        is_verified=user["is_verified"], group_metadata=user["group_metadata"]
                                        , is_supervised_user=user["is_supervised_user"]
                                        , is_supervision_enabled=user["is_supervision_enabled"]
                                        , is_supervised_by_viewer=user["is_supervised_by_viewer"],
                                        fb_profile_biolink=user["fb_profile_biolink"],
                                        profile_pic_url_hd=user["profile_pic_url_hd"],
                                        eimu_id=user["eimu_id"],
                                        bio_links=user["bio_links"],
                                        full_name=user["full_name"],
                                        has_clips=user["has_clips"],
                                        pronouns=user["pronouns"],
                                        username=user["username"],
                                        biography=user["biography"],
                                        has_guides=user["has_guides"],
                                        is_private=user["is_private"],
                                        edge_follow=user["edge_follow"],
                                        guardian_id=user["guardian_id"],
                                        has_channel=user["has_channel"],
                                        category_enum=user["category_enum"],
                                        category_name=user["category_name"],
                                        country_block=user["country_block"],
                                        external_url=user["external_url"],
                                        business_email=user["business_email"],
                                        follows_viewer=user["follows_viewer"],
                                        has_ar_effects=user["has_ar_effects"],
                                        blocked_by_viewer=user["blocked_by_viewer"],
                                        connected_fb_page=user["connected_fb_page"],
                                        edge_followed_by=user["edge_followed_by"],
                                        is_regulated_c18=user["is_regulated_c18"],
                                        transparency_label=user["transparency_label"],
                                        transparency_product=user["transparency_product"],
                                        followed_by_viewer=user["followed_by_viewer"],
                                        has_blocked_viewer=user["has_blocked_viewer"],
                                        is_embeds_disabled=user["is_embeds_disabled"],
                                        is_joined_recently=user["is_joined_recently"],
                                        has_requested_viewer=user["has_requested_viewer"],
                                        highlight_reel_count=user["highlight_reel_count"],
                                        restricted_by_viewer=user["restricted_by_viewer"],
                                        should_show_category=user["should_show_category"],
                                        is_business_account=user["is_business_account"],
                                        requested_by_viewer=user["requested_by_viewer"],
                                        business_address_json=user["business_address_json"],
                                        business_phone_number=user["business_phone_number"],
                                        overall_category_name=user["overall_category_name"],
                                        business_category_name=user["business_category_name"],
                                        biography_with_entities=user["biography_with_entities"],
                                        business_contact_method=user["business_contact_method"],
                                        external_url_linkshimmed=user["external_url_linkshimmed"],
                                        is_professional_account=user["is_professional_account"],
                                        is_verified_by_mv4_b=user["is_verified_by_mv4b"],
                                        is_guardian_of_viewer=user["is_guardian_of_viewer"],
                                        edge_mutual_followed_by=user["edge_mutual_followed_by"],
                                        show_account_transparency_details=user["show_account_transparency_details"],
                                        should_show_public_contacts=user["should_show_public_contacts"],
                                        pinned_channels_list_count=user["pinned_channels_list_count"],
                                        edge_owner_to_timeline_media=user["edge_owner_to_timeline_media"],
                                        hide_like_and_view_counts=user["hide_like_and_view_counts"],
                                        id=user["id"],
                                        fbid=user["fbid"],
                                        )))

            except:
                sleep(1)
                self.get()


