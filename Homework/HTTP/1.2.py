"""
import requests
# Make a Request

r = requests.get('http://httpbin.org/get')
print(r.text)
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/get"
}

r = requests.post('http://httpbin.org/post')
print(r.text)
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "0",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "json": null,
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/post"
}

# Passing Parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)
{
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/get?key1=value1&key2=value2"
}
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.text)
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "key": "value"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "json": null,
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/put"
}

import json
url = 'http://httpbin.org/post'
r = requests.post(url, data=json.dumps({'key':'value'}))
r = requests.post(url, json={'key':'value'})
print(r.text)
{


  "args": {},
  "data": "{\"key\": \"value\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "16",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "json": {
    "key": "value"
  },
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/post"
}

# POST a Multipart-Encoded File
url = 'http://httpbin.org/post'
files = {'file':
         ('test.txt',
          open('/Users/alexander/Desktop/test.txt',
               'rb'))}
r = requests.post(url, files=files)
print(r.text)
{
  "args": {},
  "data": "",
  "files": {
    "file": "test content\n"
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "157",
    "Content-Type": "multipart/form-data; boundary=a6d397e696144b588e9a4aa1cff723fb",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "json": null,
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/post"
}

# Headers
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
print(r.text)
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "my-app/0.0.1"
  },
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/get"
}

# Response Content
r = requests.get('http://httpbin.org/get')
print(type(r.text), r.text)
print(type(r.content), r.content)
print(type(r.json()), r.json())
<class 'str'> {
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1"
  },
  "origin": "185.136.79.217",
  "url": "http://httpbin.org/get"
}

<class 'bytes'> b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.18.1"\n  }, \n  "origin": "185.136.79.217", \n  "url": "http://httpbin.org/get"\n}\n'
<class 'dict'> {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.1'}, 'origin': '185.136.79.217', 'url': 'http://httpbin.org/get'}

# # Response Status Codes
print(r.status_code)
print(r.status_code == requests.codes.ok)
200
True
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()


# Response Headers
print(r.headers)
{'Connection': 'keep-alive', 'Server': 'meinheld/0.6.1', 'Date': 'Sun, 03 Dec 2017 08:46:02 GMT', 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'X-Powered-By': 'Flask', 'X-Processed-Time': '0.000767946243286', 'Content-Length': '267', 'Via': '1.1 vegur'}
# Redirection and History
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
https://github.com/
200
[<Response [301]>]
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)


301
[]
# Cookies

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
{
  "cookies": {
    "cookies_are": "working"
  }
}

# Session Objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)
<RequestsCookieJar[<Cookie sessioncookie=123456789 for httpbin.org/>]>
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}


s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.1",
    "X-Test": "true",
    "X-Test2": "true"
  }
} """