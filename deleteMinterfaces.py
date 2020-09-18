
# Python script to create many interfaces on Cisco switch running XE IOS

# https://youtu.be/umsYXQGV4-g?list=PLhfrWIlLOoKPc2RecyiM_A9nf3fUU3e6g&t=351


import requests
# requests library for REST API queries


# Allow self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'developer'
PASS = 'C1sco12345'




payload = {}

# Set yang+json as the data formats
headers = { 'Accept': 'application/yang-data+json'}

int_number = 50 

for x in range(int_number):
	intname = 'Loopback123' + str(x)
	print('Deleting loopback: ' + intname)

	# URL for GET request - same request for getting the list of interfaces
	url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=" + intname

	# Actual post request
	response = requests.request ('DELETE', url , auth=(USER, PASS), 
				headers=headers, data = payload, 
				verify=False)


	# Print results

	print('Response Test: ' + response.text)
	print('Status Code: ' + str(response.status_code))


