import requests, json

response = requests.get('https://api.jikan.moe/v3/anime/21')
result = json.loads(response.text)

for i in result:
	if len(str(result[i])) > 50:
		continue
	print("%s: %s" % (i, result[i]))