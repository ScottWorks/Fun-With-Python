

sandwichOrders = ["Royale with Cheese", "The Baconator", "Grilled Ruben", "Ham and Cheese", "Grilled Ruben" , "The Godfather", "Grilled Ruben", "Courdon Bleu"]
finishedOrders = [] 

while sandwichOrders: 
	 completedOrder = sandwichOrders.pop()
	 
	 if completedOrder == "Grilled Ruben":
		 print("The " + completedOrder + " is not longer available")
		 while 'Grilled Ruben' in sandwichOrders:
			 sandwichOrders.remove('Grilled Ruben')
	 else:
		 print("Completed Order: " + completedOrder.title())
		 finishedOrders.append(completedOrder)
	 
print("\n The following orders have been completed: ")
for finishedOrder in finishedOrders: 
	print(finishedOrder.title())
