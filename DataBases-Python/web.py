#!/usr/bin/env python3

from requests.auth import HTTPDigestAuth
import requests
import json

print(requests.__version__)
print(requests.__copyright__)


def breakLine():
    space = "                "
    print(space)


breakLine()

r = requests.get('http://github.com')
print(r.url)
breakLine()

# The Requests library also comes with a built-in JSON decoder,
# just in case you have to deal with JSON data
url = 'https://jsonplaceholder.typicode.com/todos/1'
print(url)
breakLine()

# Lets send in HTTP methods
response = requests.get(url)    # To execute get request
print(response.status_code)     # To print http response code
print(response.text)  # it actually returns a JSON
breakLine()

# Lets send in a HTTP POST
data = {'title': 'Python Requests',
        'body': 'Requests are awesome', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data)
print(response.status_code)
breakLine()

print(response.text)
breakLine()


print(response.content)           # To print response bytes
print(response.text)              # To print unicode response string
jsonRes = response.json()         # To get response dictionary as JSON
breakLine()

print(jsonRes)
# output: Python Requests : Requests are awesome
breakLine()

print(jsonRes['title'], jsonRes['body'], sep=' : ')
breakLine()

data = {'title': 'Pyton Requests', 'body': 'Requests are qwesome', 'userId': 1}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts', data, stream=True)
print(response.raw.read(30))     # output: b'{\n  "title": "Python Requests"'
breakLine()


# We can read the headers response
resp = requests.head("http://www.google.com")
print("This is the Header Response", resp)
breakLine()

print(resp.status_code, resp.text, resp.headers)
breakLine()


# --------------------------------------------
# Basic Auth: This transfers the authentication details as base64 encoding
# ext as bytes), meaning there is no encryption and security.
# It is suitable for HTTPs or SSL/TSL enabled connections
# where security is inbuilt.

# Open github API to test authentication
requests.get('https://api.github.com/user',
             auth=HTTPBasicAuth('badilladrian', 'Franco2!2!'))

# or shortcut method
requests.get('https://api.github.com/user', auth=('user', 'pass'))

breakLine()
# Digest Auth: This transfers the credentials in an encrypted form by
# applying a hash function on credentials, HTTP method, nonce
# (one-time number, provided by server), and the requested URI.
# Hence, it is more secured while making HTTP calls.

response = requests.get('https://postman-echo.com/digest-auth',
                        auth=HTTPDigestAuth('postman', 'password'))

# Headers
# A header contains information about the client (type of browser), server,
# accepted response type, IP address, etc. Headers can be customized
# for the source browser (user-agent) and content-type. They can be viewed using headers property as:
headers = {'user-agent': 'customize header string',
           'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(url, headers=headers)   # modify request headers
breakLine()
print(response.headers)  # print response headers
# output: application/json; charset=utf-8
breakLine()
print(response.headers['Content-Type'])
breakLine()

# Cookies
# Cookies are small pieces of data stored on the client (browser) side and are often used to maintain a
# login session or to store user IDs. Both the client and server can send cookies.
# Use the cookies property to send and access cookies.
cookie = {'username': 'Pavneet'}
response = requests.get(
    'https://postman-echo.com/cookies/set', cookies=cookie)   # send cookie
thisCookie = response.cookies
breakLine()

print(thisCookie)
breakLine()

print(response.text)    # output: {"cookies":{"username":"Pavneet"}}
breakLine()
