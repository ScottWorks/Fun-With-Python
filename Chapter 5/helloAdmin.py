

users = ['noobpwner', 'fucktheadmin', 'ricksanchez', 'donutpet', 'saucebaus']
admins = ['admin1', 'waffleflavor']
currentUsers = ['ricksanchez', 'noobpwner', 'fucktheadmin']
currentAdmins = ['admin1', 'waffleflavor', 'skunkfunk']

for currentUser in currentUsers:
	if currentUser in users:
		print("Hello " + currentUser + ", thank you or logging in again.")
for currentAdmin in currentAdmins:
	if currentAdmin in admins:
		print("Hello " + currentAdmin + ", would you like to see a status report?")
