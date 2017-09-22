

cars = ['McLaren', 'Porsche', 'BMW', 'Audi']

# If Statement
for car in cars: 
	if car.lower() == 'audi':
		print(car.upper())
	else: 
		print(car.title())

# Equality
car = 'AUDI'
print(car.lower() == 'audi')

car = 'AUDI'
print(car == 'audi')

# Inequality
car = 'BMW'
print(car != 'bmw')

car = 'bmw'
print(car.upper() != 'BMW')

# Multiple Conditions
year = 2001 

print(year >= 2000 and year <= 2002)
print(year == 2001 or year <=2010)

print(year >= 2002 and year <= 1999)
print(year == 2000 or year <=1990)

# in List Check
print('BMW' in cars)
print('bmw' in cars)

# not in List Check
print('BMW' not in cars)
print('bmw' not in cars)
