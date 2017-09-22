

rivers = {
	'nile river': 'egypt', 
	'colorado river': 'united states of america',
	'mississippi river': 'united states of america', 
	'thames river': 'england', 
	'yangzte river': 'china'}

for k, v in sorted(rivers.items()):
	print("\nThe " + k.title() + " is located in " + v.title())
print("\n")	

for k in sorted(rivers.keys()):
	print("\n" + k.title())
print("\n")	

for v in sorted(set(rivers.values())):
	print("\n" + v.title())
print("\n")	
