

activated = True

while activated: 
	ageCalc = input("\nPlease enter the age of each ticket holder: \n")
	ageCalc = int(ageCalc)
		
	if ageCalc < 1:
		print("Invalid entry, please try again...")
	
	elif ageCalc < 3:
		price = 0
		print("\n" + "$" + str(price))
	
	elif ageCalc >= 3 and ageCalc <= 12: 
		price = 10
		print("\n" + "$" + str(price))
	
	elif ageCalc > 12: 
		price = 15
		print("\n" + "$" + str(price))
	
	
		
		 
