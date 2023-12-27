from random import random

import requests


from Request import Request


class Search(Request):
    def __init__(self, name: str):
        super().__init__()

        self.suffix = "api/graphql"

        self.body = (
                'av=17841458538991223&__d=www&__user=0&__a=1&__req=1h&__hs=19718.HYP:instagram_web_pkg.2.1..0.1&dpr=1&__ccg=UNKNOWN&__rev=1010595764&__s=2hed2q:hr378e:52fg4h&__hsi=7317264039299915723&__dyn=7xeUjG1mxu1syUbFp60DU98nwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO2O1Vw8G1nzUO0n24oaEd86a3a1YwBgao6C0Mo2iyovw8OfK0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azqwt8dUaob82cwMwrUdUbGwmk1xwmo6O1FwlE6PhA6fxy4UjxK&__csr=gD1NEp4hkAlOiEAhOVfnmiO5bC8V92kHqVtGFbXBh8GXCUTijy9HWlu9lKEyiF58Uih5CHJ1iaG_gDiCHyUDlrynzk8GcLjy44QUoxu8yp8SFE01cxei1RCQ05s2w1u207r-it218vg3RzoO7VU9X9g1jpE13i07JwcG0woAU3BwcZ0oo0M-3DgfK5pFIE5W00FP8&__comet_req=7&fb_dtsg=NAcMdAxO0UAHhxaZX1PsIWZcRx__tp5syIwLfryNLA-CcRGtFPHc00w:17864863018060157:1703682222&jazoest=26310&lsd=10f6Ax5C_qLumChIc3MSba&__spin_r=1010595764&__spin_b=trunk&__spin_t=1703683296&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisSearchBoxRefetchableQuery&variables={"data":{"context":"blended","include_reel":"true","query":"'+name+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}&server_timestamps=true&doc_id=6901177919928333')
        self.res = requests.post(f"{self.host_name}{self.suffix}", headers=self.headers, data=self.body).json()


    def api(self):
        return self.res["data"]["xdt_api__v1__fbsearch__topsearch_connection"]

    def users(self):
        return self.api()["users"]

    def hashtags(self):
        return self.api()["hashtags"]
