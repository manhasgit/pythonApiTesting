import requests
import jsonpath
import json

def test_add_student_details():
    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Student_add.json','r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_update_student_details():
    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails/177138'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Student_add.json','r')
    json_request = json.loads(file.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

def test_delete_student_details():
    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails/177138'
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_details():
    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails/177138'
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 177138




