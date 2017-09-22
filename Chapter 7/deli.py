

sandwichOrders = ["Ham and Cheese", "The Godfather", "Grilled Ruben", "Courdon Bleu"]
finishedOrders = []

while sandwichOrders: 
	 completedOrder = sandwichOrders.pop()
	 
	 print("Completed Order: " + completedOrder.title())
	 finishedOrders.append(completedOrder)
	 
print("\n The following orders have been completed: ")
for finishedOrder in finishedOrders: 
	print(finishedOrder.title())
