from unittest.mock import  MagicMock

class UserMock:
    @staticmethod
    def get_mock():
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {"name": {"first": "Mocked", "last": "User"}, "gender": "female"}
            ]
        }
        return  mock_response