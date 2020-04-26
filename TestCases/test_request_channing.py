import requests
import jsonpath
import json

def test_add_new_student():

    global id
    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Add_Request.json','r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():

    api_url = 'http://www.thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    response = requests.get(api_url)
    print(response.text)
