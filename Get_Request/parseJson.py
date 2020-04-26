#import json

#odics = '{"k1":"val1","k2":"val2"}'

#json_request = json.loads(odics)

#print(json_request["k1"])

import requests
import jsonpath
import json

add_api_url = 'http://www.thetestingworldapi.com/Help/Api/POST-api-addresses'
file = open('//Users//nareshmanhas//Desktop//hello//API//Add_address.json', 'r')
request_json = json.loads(file.read())
#request_json['stId'] = id[0]
response = requests.post(add_api_url, request_json)
print(response)
