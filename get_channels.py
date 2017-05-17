import requests
import json

url = 'http://192.168.47.231:8050/MCP'

channels_list = requests.get(url)

channels_list_parsed = json.loads(channels_list.text)

# print channel list with details
for channel in channels_list_parsed:
	print (channel)
	channel_details = requests.get(url+'/id')
	channel_details_parsed = json.loads(channel_details.text)
	print (json.dumps(channel_details_parsed, indent=4, sort_keys=True))