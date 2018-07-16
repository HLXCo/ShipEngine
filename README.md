# ShipEngine
An incredibly simple Python wrapper to interact with the ShipEngine API to track your package status

	# Create an account to get your API Key
	# https://app.shipengine.com/#/public/createaccount

	from ShipEngineAPI import ShipEngineAPI
	se = ShipEngineAPI('__your_api_key__')						# <--- Place your API Key Here
	result = se.trackPackage('__your_courier__', '__your_tracking_number__')	# <--- Replace with your values
	print(result)
