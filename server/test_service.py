import requests
import unittest
import server
from server import createSocket
from server import ADDR
from unittest import mock
from unittest.mock import patch
from server import startServer
from server import bindSocket

class TestServer(unittest.TestCase):
    @patch('server.createSocket')
    @patch('server.bindSocket')
    def test_startServer(self,create_socket,bind_socket):
        socket_server_mock = mock.Mock()
        create_socket.return_value = socket_server_mock # this returns socketServer
        startServer()
        bind_socket.assert_called_once(socket_server_mock,ADDR)

    
    def test_getAPI(self,mock_http_get):
        pass   