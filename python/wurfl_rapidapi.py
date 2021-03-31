import json
import os
import http.client

try:
    rapidapi_key = os.environ['RAPIDAPI_KEY']
    rapidapi_host = os.environ['RAPIDAPI_HOST']
except KeyError as ke:
    print('Error: you must set RAPIDAPI_KEY and RAPIDAPI_HOST environment variables to use this code sample')
    exit(1)

conn = http.client.HTTPSConnection(rapidapi_host)

# This payload selects only three capabilities (1 static and two virtual), you can select all the exposed capabilities
# by removing the two requested* arrays (also remember to remove the comma after the curly brace,
# or you'll get an error 500
payload = '''
{
  "lookup_headers": {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; ASUS_Z017D Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/539.36",
	"content-Type": "application/json",
    "x-requested-with":"XMLHttpRequest"
  },
  "requested_caps": ["is_tablet"],
  "requested_vcaps": ["complete_device_name", "form_factor"]     
}
'''

headers = {
    'x-rapidapi-host': rapidapi_host,
    'x-rapidapi-key': rapidapi_key,
    'content-type': "application/json"
}

conn.request("POST", "/v2/lookuprequest/json", payload, headers)

res = conn.getresponse()
data = json.loads(res.read())
print(json.dumps(data, indent=4, sort_keys=True))
