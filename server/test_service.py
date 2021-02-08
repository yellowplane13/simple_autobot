import requests
import unittest
import server
import service
from service import callAPI
from service import talkToAPI
from server import createSocket
from server import ADDR
from unittest import mock
from unittest.mock import patch
from server import startServer
from server import bindSocket
import json

SUCCESS_STR = f"[SUCCESS] repo1 is a valid Repository"

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    print(args[0],"args[0]")
    if "repo1" in args[0]:
        return MockResponse({"watchers": "1234"}, 200)
    return MockResponse(None, 404)

class TestServer(unittest.TestCase):
    # test success
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_getAPI_success(self,mock_http_requests):
        print("inside test")
        stars,error_code = talkToAPI(['repo1'])
        print(stars,error_code)
        assert SUCCESS_STR==error_code[0]
        assert "1234"==stars['repo1']