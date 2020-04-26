import requests
import jsonpath
import json

def test_add_new_data():
    global response

    API_URL = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Add_Request.json','r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = 'http://www.thetestingworldapi.com/api/technicalskills'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Add_Technical_details.json','r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    address_api_url = 'http://www.thetestingworldapi.com/api/addresses/'
    file = open('//Users//nareshmanhas//Desktop//hello//API//Add_address.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(address_api_url, request_json)
    print(response.text)

    final_details = 'http://www.thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response = requests.get(final_details)
    print(response.text)

