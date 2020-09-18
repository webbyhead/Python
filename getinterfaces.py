
# Python script to query Cisco switch running XE IOS

# Taken from https://www.youtube.com/watch?v=DAajWlVcskw&list=PLhfrWIlLOoKPc2RecyiM_A9nf3fUU3e6g&index=30



import requests
# requests library for REST API queries


# Allow self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET request - same request for getting the list of interfaces
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

# Set yang+json as the data formats
# Need both Accept and Content-Type for a POST
headers = {'Content-Type': 'application/yang-data+json',
'Accept': 'application/yang-data+json'}

# Run GET
response = requests.get(url, auth=(USER, PASS),
			headers=headers, verify=False)

print('Response Text: ' + response.text)
print('Status Code: ' + str(response.status_code))






