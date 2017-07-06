import requests
import json
URL = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"

r = requests.get(URL, verify = False)

json_dict = r.json() # a standard python dictionary
print(json.dumps(json_dict, indent=3)) # to pretty-print with 3 spaces of indentation