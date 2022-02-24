# Clubhouse.io: Delete all archived stories

import requests
import sys
import json

token = sys.argv[1]

try:
	data = {
		'name':'TEST STORY',
		'project_id': 13,
		'owner_ids':[]
	}
	print(token)
	r = requests.post('https://api.clubhouse.io/api/v3/stories', params={'token':token}, data=data)
	print(r)
except RequestException as err:
	print(err)
