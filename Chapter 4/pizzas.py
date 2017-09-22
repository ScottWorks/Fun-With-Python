

toppings = ['pepperoni', 'onions', 'pepper', 'anchovies', 'extra cheese']

print(len(toppings))

print(sorted(toppings))

toppings.reverse()
print(toppings) 

toppings.sort() 
print(toppings) 

toppings.sort(reverse = True) 
print(toppings)

for topping in toppings:
	print("I would like to order a(n) " + topping + " pizza, please.")
print("That will be all")
