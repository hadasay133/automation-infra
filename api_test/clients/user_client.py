from typing import Optional

from api_test.clients.base_client import BaseAPIClient


class UserClient (BaseAPIClient) :
    def __init__(self):
        super().__init__('https://randomuser.me')
    def get_random_user(self, endpoint: str, params: Optional[dict]=None ):
        return self.get(endpoint,params= params)

    def post_random_user(self, endpoint: str,  data: Optional[dict]=None , json: Optional[dict]=None):
        return self.post(endpoint, data=data,json=json)