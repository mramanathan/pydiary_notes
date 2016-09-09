# codeing: utf-8

#!/usr/bin/env/python

from urllib2 import urlopen
from json import load



# Resource id varies, for pincode data it is hardcoded
## number of records limited to 10
### output format is default set to JSON
dataurl = 'https://data.gov.in/api/datastore/resource.json?resource_id='
print("Generic url : {}".format(dataurl))

# your key could be different from mine, so you should use 
## the key supplied to you at https://data.gov.in
keyfile = '/home/raman/odg_api_key'

def main():

	"""  Example code to extract 10 records using pincode API

	available at https://data.gov.in

	"""

	key = open(keyfile, 'r')
	userkey = key.read()

	resource_id = "0a076478-3fd3-4e2c-b2d2-581876f56d77" + "&"
	limit = "limit=" + "50" + "&" 
	key = "api-key="
	url  = dataurl + resource_id + limit + key + userkey.split('\n')[-2]

	# final url should be:
	# 'https://data.gov.in/api/datastore/resource.json?resource_id=0a076478-3fd3-4e2c-b2d2-581876f56d77&limit=10&api-key=YOUR_KEY_FROM_data.gov.in'

	response = urlopen(url)
	json_obj = load(response)

	for k,v in json_obj.iteritems():
		if "records" in k:
			# Because this code demonstrates retrieving pincode
			# we fetch the pincode and exit the loop
			pincode = v
			break

	for i in range(len(pincode)):
		this_record = pincode[i]
		if this_record['regionname'] == "Hyderabad":
			print("{} region has:".format(this_record['regionname']))
			print("=" * 2 + " Record {0} has items : {1}\n".format(i, this_record))


if __name__ == "__main__":
	main()
