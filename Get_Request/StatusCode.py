import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

print(response.status_code)

assert response.status_code == 200

#to fetch the response headers
print(response.headers)

#fetch specfic header response
print(response.headers.get('Date'))
print(response.headers.get('Content-Type'))

#how to fetch cookies
print(response.cookies)

#fetch encoding

print(response.encoding)

#Elasped time

print(response.elapsed)