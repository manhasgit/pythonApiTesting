import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"
@pytest.fixture()
def setup():
    global file
    file = open('//Users//nareshmanhas//Desktop//hello//CreateJson.json', 'r')



@pytest.mark.smoke()
def test_create_user(setup):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)

    print(response.headers.get('Set-Cookie'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

@pytest.mark.sanity()
def test_other_user(setup):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)

    assert response.status_code == 201





