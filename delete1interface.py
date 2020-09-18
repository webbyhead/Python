
# Python script to delete an interface on Cisco switch running XE IOS

# Taken from https://www.youtube.com/watch?v=DAajWlVcskw&list=PLhfrWIlLOoKPc2RecyiM_A9nf3fUU3e6g&index=30



import requests
# requests library for REST API queries


# Allow self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'developer'
PASS = 'C1sco12345'


intname = "Loopback1234"

# URL for DELETE request - same request for getting the list of interfaces
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=" + intname


# JSON Payload - using \ to continue the line in python
payload = {}


# Set yang+json as the data formats
headers = { 'Accept': 'application/yang-data+json', }


# Actual post request
response = requests.request ('DELETE', url , auth=(USER, PASS), 
				headers=headers, data = payload, 
				verify=False)


# Print results

print('Response Test: ' + response.text)
print('Status Code: ' + str(response.status_code))


