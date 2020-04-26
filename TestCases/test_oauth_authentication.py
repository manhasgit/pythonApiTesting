import requests
import jsonpath
import json

def test_oauth_details():

    token_url = 'http://www.thetestingworldapi.com/Token'
    data = {'grant_type':'password','username':'admin','password':''}
    response = requests.post(token_url,data)
    token_value = jsonpath.jsonpath(response.json(),'access_token')
    auth = {'Autorization': 'bearer '+token_value[0]}

    api_url = 'http://www.thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(api_url, headers= auth)
    print(response)