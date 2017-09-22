

favoritePlaces = {
					'shannon':['bali', 'j tree'], 
					'melissa':['yosemite', 'grand canyon', 'berlin'],
					'sam':['adirondacks'],
					'joshua':['tel aviv', 'cario', 'amsterdam'],
					'alex':['barcelona', 'french alps']
					}
					
for names, places in favoritePlaces.items():
	
	if len(places) > 1: 
		print(names.title())
		for place in places:
			print(place.title())
		
		print("\n")

	else: 
		print("Test" + names.title())
		print("\n")
