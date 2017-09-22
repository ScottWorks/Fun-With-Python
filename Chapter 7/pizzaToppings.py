

prompt = "\n Please enter your pizza topping selection:"
prompt += "\n Enter 'quit' to end the program."
message = ""

listToppings = []

while True:
	message = input(prompt)
	listToppings.insert(0, message)
	print(listToppings)

	if message == 'quit':
		print("Your pizza shall include: \n" + str(listToppings))
		break
		
