from unittest.mock import patch

from api_test.api_mock.user_mock import UserMock
from api_test.clients.user_client import UserClient


class TestApiRequests:

    @patch('requests.get')
    def test_get_request(self, mock_get):
        mock_get.return_value = UserMock.get_mock()
        client = UserClient()
        response = client.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        user_data = response.json()["results"][0]
        assert user_data["gender"] == "female"
        assert user_data["name"]["first"] == "Mocked"

    def test_post_request(self):
        client = UserClient()
        param = {
            "gender": "female",
            "first": "Lili",
            "userId": 1
        }
        res = client.post("https://randomuser.me", param)
        assert res.status_code == 200

