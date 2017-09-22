

users = ['noobpwner', 'fucktheadmin', 'ricksanchez', 'Donutpet', 'saucebaus']
admins = ['admin1', 'waffleflavor']

currentUsers = ['ricksanchez', 'noobpwner', 'fucktheadmin']
currentAdmins = ['admin1', 'waffleflavor', 'skunkfunk']

newUsers = ['noobpwner', 'skanker', 'DONUTPET', 'mortysanchez', 'billnye']

if currentUsers == []:
	print("No users signed in!")

if currentAdmins == []:
	print("No admins signed in!")

if newUsers:
	for newUser in newUsers:
		if newUser.lower() in users:
			print("Username exists, please enter a new username...")
		elif newUser.upper() in users:
			print("Username exists, please enter a new username...")		
		elif newUser.title() in users:
			print("Username exists, please enter a new username...")
		else: 
			print("Username selection successful...")

for currentUser in currentUsers:
	if currentUser in users:
		print("Hello " + currentUser + ", thank you or logging in again.")

for currentAdmin in currentAdmins:
	if currentAdmin in admins:
		print("Hello " + currentAdmin + ", would you like to see a status report?")
