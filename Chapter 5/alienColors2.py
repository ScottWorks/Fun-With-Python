

alienColors = ['yellow', 'red', 'green']
points = 0

for alienColor in alienColors:
	if alienColor == 'green':
		points = points + 5 
	elif alienColor == 'yellow':
		points = points + 10
	elif alienColor == 'red':
		points = points + 15
print("Player Points: " + str(points))			
