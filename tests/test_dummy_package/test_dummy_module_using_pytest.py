import json
from unittest.mock import MagicMock

import pytest
from requests import Session
import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from dummy_package.dummy_module import DummyClass


@pytest.fixture
def mock_session(mocker):
	mock_session = mocker.patch.object(Session, 'get', autospec=True)
	return mock_session


@pytest.mark.usefixtures('mock_session')
def test_dummy(mock_session):
	expected_string = """{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
	}"""

	mock_response = MagicMock()
	mock_response.status_code = 200
	mock_response.json.return_value = json.loads(expected_string)

	expected = json.loads(expected_string)
	mock_session.return_value = mock_response

	print(mock_session)
	res = DummyClass().get_request('https://jsonplaceholder.typicode.com/todos/2')
	assert expected == res
