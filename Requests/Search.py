import json

import certifi
import requests

from Request import Request
from Utils.JsonReader import get_by_name, read_json


# fetch every thing using the instagram.json file
class Search(Request):

    def __init__(self, name: str):
        super().__init__()
        items = read_json("Requests/instagram.json")
        insta_file = get_by_name(items["item"], "search")
        headers = self.collect_headers(insta_file["header"])
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["X-Csrftoken"] = items["variable"][1]["value"]  # csrf variable

        self.response = requests.post(insta_file["url"]["raw"], headers=headers,
                                      data='av=17841458538991223&__d=www&__user=0&__a=1&__req=1q&__hs=19722.HYP:instagram_web_pkg.2.1..0.1&dpr=1&__ccg=UNKNOWN&__rev=1010616023&__s=356nc2:q9tjv5:zzrizo&__hsi=7318786434661464314&__dyn=7xeUjG1mxu1syUbFp60DU98nwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO2O1Vw8G1nzUO0n24oaEd86a3a1YwBgao6C0Mo2iyovw8OfK0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azqwt8dUaob82cwMwrUdUbGwmk1xwmo6O1FwlE6PhA6fxy4UjxK&__csr=gX6MjimI9jlb_W2R6b_j8GRZaSp_miAEOiGoxTiryqFbGcHDzienpBAhbhVrRFp9kdB-e-mmaiBgOHhT8t39biAyWHHiGWxy8zUxxKqULxGudAKjw04P5Ag7yS05qq805N80sIg3vwm8djxsgt2p60zk08ww2m82gBkEcUS0A44E1qofkmt2pE0xu1cxbwg9U14802Cpw&__comet_req=7&fb_dtsg=NAcNZgNUcR6P-xD4KXXPmtKoO-6b8r0J-hpjqK2XXH5ZqZDXMegwSIw:17843708194158284:1703955039&jazoest=26150&lsd=g6eEY2DvBFbvyQmT4FkEG_&__spin_r=1010616023&__spin_b=trunk&__spin_t=1704037756&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisSearchBoxRefetchableQuery&variables={"data":{"context":"blended","include_reel":"true","query":"'+name+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}&server_timestamps=true&doc_id=6901177919928333')


    def api(self) -> dict:
        return self.response.json()["data"]["xdt_api__v1__fbsearch__topsearch_connection"]
