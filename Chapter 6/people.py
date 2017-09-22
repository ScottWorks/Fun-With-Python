

personInfo1 =  {'firstName': 'Karl', 'lastName':'Lopez', 'State': 'New York', 
				'Driver ID': '0148 4644 1214'}

personInfo2 =  {'firstName': 'Danielle', 'lastName':'Smith', 'State': 'California', 
				'Driver ID': '2393 1239 3231'}

personInfo3 =  {'firstName': 'Alex', 'lastName':'Douglas', 'State': 'California', 
				'Driver ID': '2122 3469 3671'}


people = [personInfo1, personInfo2, personInfo3]

for person in people: 
	print(person['firstName'])
	print(person['lastName'])
	print(person['State'])
	print(person['Driver ID'])
	print("\n")
