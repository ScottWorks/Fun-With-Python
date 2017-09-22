

def makeAlbum(album, artist, genre, trackNum):
	"""Builds dictionary describing music album"""
	#albumDetails = album + artist + genre + trackNum
	#return albumDetails
	
while True:
	print("\n" + "Please enter the following album information, enter 'q' to quit at anytime: ")
		
	albumName = input("Album Title: ")
	if albumName == 'q': 
		break

	artistName = input("Artist: ")
	if artistName == 'q': 
		break

	genreType = input("Genre: ")
	if genreType == 'q': 
		break
	
	trackNumInt = input("Number of Tracks: ")
	if trackNumInt == 'q': 
		break
			
	albumInfo = {'Artist': artistName, 'Album': albumName, 'Genre': genreType, 'Track Count': trackNumInt}
	print(albumInfo)



	

	
