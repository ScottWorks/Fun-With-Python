

numInput = input("Please enter a number... ")
quest = input("Is " + numInput + " a multiple of 10?\n1) Yes \n2) No\n")

numInput = int(numInput)
quest = int(quest)

if numInput % 10 == 0 and quest == 1 or numInput % 10 != 0 and quest == 2:
	print("Correct!")
else:
	print("Incorrect!")
