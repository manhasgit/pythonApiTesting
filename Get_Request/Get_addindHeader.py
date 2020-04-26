import requests

headerdata = {'name':'naresh','id':'123'}

response = requests.get('https://httpbin.org/get',headers = headerdata)
print(response.text)