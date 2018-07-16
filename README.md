# ShipEngine
An incredibly simple Python wrapper to interact with the ShipEngine API to track your package status

	from ShipEngineAPI import ShipEngineAPI

	# Create an account to get your API Key
	# https://app.shipengine.com/#/public/createaccount

	__author__ = "Sergio Molanes"
	__copyright__ = "Copyright 2018, HLX Studios"
	__license__ = "GPL 3.0"
	__version__ = "1.0"
	__maintainer__ = "Sergio Molanes"
	__email__ = "sergio@hlx.co"
	__status__ = "Production"


	API_KEY = '__your_api_key__' # <--- Place your API Key Here
	se = ShipEngineAPI(API_KEY)
	result = se.trackPackage('__your_courier__', '__your_tracking_number__')	# <--- Replace with your values
	print(result)
