from typing import Optional

import requests



class BaseAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def get(self, endpoint: str, params: Optional[dict]=None ):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint: str,  data: Optional[dict]=None , json: Optional[dict]=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if json:
            return requests.post(url, json=json)
        else:
            return requests.post(url, data=data)

    def delete(self, endpoint: str):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url)
        return response