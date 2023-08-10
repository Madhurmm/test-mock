import json

import unittest
from unittest.mock import MagicMock, patch
from requests import Session
import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from dummy_package.dummy_module import DummyClass


class TestDummyRequest(unittest.TestCase):

	@patch.object(Session, 'get')
	def test_dummy(self, mock_requests):
		expected_string = """{
	  "userId": 1,
	  "id": 1,
	  "title": "delectus aut autem",
	  "completed": false
		}"""

		expected = json.loads(expected_string)

		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.json.return_value = expected

		mock_requests.return_value = mock_response
		res = DummyClass().get_request('https://jsonplaceholder.typicode.com/todos/2')

		assert expected == res
