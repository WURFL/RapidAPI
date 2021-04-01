import json
import os
import http.client

try:
    rapidapi_key = os.environ['RAPIDAPI_KEY']
    rapidapi_host = os.environ['RAPIDAPI_HOST']
except KeyError as ke:
    print('Error: you must set RAPIDAPI_KEY and RAPIDAPI_HOST environment variables to use this code sample')
    exit(1)

# read json requests from file
try:
    requests_file = open('../requests.json', 'r')
    request_lines = requests_file.readlines()
except FileNotFoundError as e:
    print('Error, requests file not found: ' + str(e))
    exit(1)

# each line contains a set of HTTP headers taken from real requests a saved in json format
for line in request_lines:
    conn = http.client.HTTPSConnection(rapidapi_host)
    json_string = line.replace("'", "\"")
    # we get the headers as a dictionary
    headers = json.loads(json_string)
    # Create the payload to send to our request.
    # This payload selects only three capabilities (1 static and two virtual), you can select all the exposed
    # capabilities by removing the two requested* arrays as show in the commented line below
    post_body = {"lookup_headers": headers, "requested_caps": ["is_tablet"], "requested_vcaps": ["complete_device_name",
                                                                                                 "form_factor"]}
    # use this line if you want to get all capabilities exposed by the API
    # post_body = {"lookup_headers": headers }
    payload = json.dumps(post_body)

    # set the headers for our request. Be aware that these headers are different from the headers of the request
    # used to  build the POST body
    headers = {
        'x-rapidapi-host': rapidapi_host,
        'x-rapidapi-key': rapidapi_key,
        'content-type': "application/json"
    }

    try:
        conn.request("POST", "/v2/lookuprequest/json", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        print(json.dumps(data, indent=4, sort_keys=True))
    except Exception as e:
        print('Something went wrong: ' + str(e))
        exit(1)

print('RapidApi WURFL Detection script end')
