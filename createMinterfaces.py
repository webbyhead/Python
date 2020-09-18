
# Python script to create many interfaces on Cisco switch running XE IOS

# Taken from https://www.youtube.com/watch?v=umsYXQGV4-g&list=PLhfrWIlLOoKPc2RecyiM_A9nf3fUU3e6g&index=31


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
headers = {'Content-Type': 'application/yang-data+json',
'Accept': 'application/yang-data+json'}

int_number = 50 

for x in range(int_number):
	ipaddr = '1.2.3.' + str(x)
	print('Creating loopback: ' + ipaddr)

	# JSON Payload - using \ to continue the line in python
	payload = '\
	{\
	"ietf-interfaces:interface": {\
		"name": "Loopback123' + str(x) + '",\
		"description": "Added with RESTCONF by AndreT",\
		"type": "iana-if-type:softwareLoopback",\
		"enabled": true,\
		"ietf-ip:ipv4": {\
		"address": [\
			{\
				"ip": "1.2.3.' + str(x) + '",\
				"netmask": "255.255.255.255"\
			}\
				]\
			}\
		}\
	}'


	# Actual post request
	response = requests.request ('POST', url , auth=(USER, PASS), 
				headers=headers, data = payload, 
				verify=False)


	# Print results

	print('Response Test: ' + response.text)
	print('Status Code: ' + str(response.status_code))


