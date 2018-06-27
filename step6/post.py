# -*- coding: utf-8 -*-

import json
import urllib.request as urlib
#post
url = "http://46.21.249.29:8000/api/dict"
newValue = {"word" : "Дождик", "values" : ["шёл", "пошёл", "зашёл", "нашёл"] }
params = json.dumps(newValue).encode('utf-8')
req = urlib.Request(url, data=params,
    headers={'content-type': 'application/json'})
response = urlib.urlopen(req)
print(response.read().decode('utf-8'))