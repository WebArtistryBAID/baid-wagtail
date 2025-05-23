import base64
import os

from social_core.backends.oauth import BaseOAuth2


class OneLoginOAuth2(BaseOAuth2):
    name = "onelogin"
    ID_KEY = "seiueId"
    AUTHORIZATION_URL = os.environ["ONELOGIN_HOST"] + "/oauth2/authorize"
    ACCESS_TOKEN_URL = os.environ["ONELOGIN_HOST"] + "/oauth2/token"
    USER_DATA_URL = os.environ["ONELOGIN_HOST"] + "/api/v1/me"
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = "POST"
    EXTRA_DATA = [("seiueId", "id"), ("expires_in", "expires")]

    def auth_headers(self):
        client_id = self.setting('KEY')
        client_secret = self.setting('SECRET')
        token = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
        return {'Authorization': f'Basic {token}'}

    def get_user_details(self, response):
        return {
            "id": response.get("seiueId"),
            "username": response.get("pinyin")
        }

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(self.USER_DATA_URL, headers={
            "Authorization": f"Bearer {access_token}"
        })
