# ShipEngine
An incredibly simple Python wrapper to interact with the ShipEngine API to track your package status



    from ShipEngineAPI import ShipEngineAPI
    
    # Create an account to get your API Key
    # https://app.shipengine.com/#/public/createaccount
    
    API_KEY = '__api_key__' # <--- Place your API Key Here
    se = ShipEngineAPI(API_KEY)
    result = se.trackPackage('__your_courier__', '__your_tracking__number__')	# <--- Replace with your values
    print(result)
