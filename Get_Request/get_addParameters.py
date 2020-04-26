import requests

param = {'name':'naresh','id':'123'}

response = requests.get('https://httpbin.org/get',params=param)
print(response.text)