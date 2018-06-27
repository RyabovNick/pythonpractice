# -*- coding: utf-8 -*-

import json
import urllib.request as urlib
#get
url = "http://46.21.249.29:8000/api/dict"
webUrl = urlib.urlopen(url)
data = webUrl.read()
print(data)
encoding = webUrl.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))
print(JSON_object)
for n in JSON_object:
    print(n['values'])
print(JSON_object[0]['id'])