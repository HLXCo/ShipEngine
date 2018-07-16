import requests
import json

class ShipEngineAPI():
	def __init__(self, key):
		self.API_KEY = key
		self.API_ENDPOINT = 'https://api.shipengine.com/v1/tracking'
		self.__author__ = "Sergio Molanes"
		self.__copyright__ = "Copyright 2018, HLX Studios"
		self.__license__ = "GPL 3.0"
		self.__version__ = "1.0"
		self.__maintainer__ = "Sergio Molanes"
		self.__email__ = "sergio@hlx.co"
		self.__status__ = "Production"

	def trackPackage(self, carrier_code, tracking_number):
		headers = {
			'Content-type': 'application/json',
			'api-key': self.API_KEY,
		}
		params = (
			('carrier_code', carrier_code),
			('tracking_number', tracking_number),
			)
		response = requests.get(self.API_ENDPOINT, headers=headers, params=params)
		return json.loads(response.text)
