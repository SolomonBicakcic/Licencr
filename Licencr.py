import requests
def checkLicense(app):
	verify = "https://raw.githubusercontent.com/SolomonBicakcic/Licencr/master/" + str(app)
	try:
		r = requests.get(verify)
		if r.status_code is 200:
			return True
		else:
			return False
	except:
		return False
