

def makeShirt(text, size='Large'):
	"""Display shirt size and text to be displayed on shirt"""
	print("\n" + "Your shirt size is: " + size)
	print("Your shirt shall say: " + text)

makeShirt('Dump Trump')
makeShirt('Dump Trump', 'Medium')
makeShirt(size = 'Medium', text = 'Dump Trump')
