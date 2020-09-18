
# Python script to create interface on Cisco switch running XE IOS

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


# JSON Payload - using \ to continue the line in python
payload = '\
{\
	"ietf-interfaces:interface": {\
		"name": "Loopback1234",\
		"description": "Added with RESTCONF by AndreT",\
		"type": "iana-if-type:softwareLoopback",\
		"enabled": true,\
		"ietf-ip:ipv4": {\
		"address": [\
			{\
				"ip": "1.2.3.4",\
				"netmask": "255.255.255.255"\
			}\
				]\
			}\
	}\
}'



# Set yang+json as the data formats
headers = {'Content-Type': 'application/yang-data+json',
'Accept': 'application/yang-data+json'}


# Actual post request
response = requests.request ('POST', url , auth=(USER, PASS), 
				headers=headers, data = payload, 
				verify=False)


# Print results

print('Response Test: ' + response.text)
print('Status Code: ' + str(response.status_code))


