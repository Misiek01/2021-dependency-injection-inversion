
from config_vcr import vcr
import requests


@vcr.use_cassette()
def test_example_status_code_200():
    response = requests.get("https://www.python.org")
    assert response.status_code == 200
    assert b'Python is a programming language' in response.content
