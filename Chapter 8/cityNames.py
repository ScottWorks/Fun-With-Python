

def cityCountry(city, country):
	"""Displays name of city and country (city, country)"""
	
	place = city + ', ' + country
	return place.title()

namePlace = cityCountry('cairo', 'egypt')
print(namePlace)

namePlace = cityCountry('reyjavik', 'iceland')
print(namePlace)

namePlace = cityCountry('patagonia', 'argentina')
print(namePlace)
