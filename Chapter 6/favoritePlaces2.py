

favoritePlaces = {
					'shannon':{'country':'usa', 'park':'joshua tree national park', 'trail':'sands point'}, 
					'melissa':{'country':'usa', 'park':'yosemite national park', 'trail':'half dome trail'},
					'sam':{'country':'usa', 'park':'adirondack park', 'trail':'whiteface-esther trail'},
					}

for name, trailInfo in sorted(favoritePlaces.items()):
	print(name.title())
	country = trailInfo['country']
	park = trailInfo['park']
	trail = trailInfo['trail']
	
	print(country.title())
	print(park.title())
	print(trail.title())
	print('\n')
