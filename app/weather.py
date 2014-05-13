import requests
import json

class WeatherParser:

	API_KEY = 'y3b2hzpe4s8cepvcdfahyepz'
	API_URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx'

	def download(location):
		parameters = {'q': location, 'format': 'json', 'sensor': 'false', 'num_of_days': '1', 'key': WeatherParser.API_KEY}
		result = requests.post(WeatherParser.API_URL, params=parameters)
		resultdict = json.loads(result.content.decode("utf-8"))
		return resultdict['data']