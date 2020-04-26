import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

#read input json file

file = open('//Users//nareshmanhas//Desktop//hello//CreateJson.json','r')
json_input = file.read()
request_json = json.loads(json_input)


#make post request json input body
response = requests.put(url,request_json)


#validating response code
assert response.status_code == 200

#fetch header from response
print(response.headers.get('Set-Cookie'))

#parse response to json format

response_json = json.loads(response.text)


#pick id from json path

name = jsonpath.jsonpath(response_json,'name')
print(name[0])



