# ShipEngine
An incredibly simple Python wrapper to interact with the ShipEngine API to track your package status

	# Create an account to get your API Key
	# https://app.shipengine.com/#/public/createaccount

	from ShipEngineAPI import ShipEngineAPI
	API_KEY = '__your_api_key__' # <--- Place your API Key Here
	se = ShipEngineAPI(API_KEY)
	result = se.trackPackage('__your_courier__', '__your_tracking_number__')	# <--- Replace with your values
	print(result)
