

def makeAlbum(artist, album, genre, releaseDate, trackNum = ''):
	"""Builds dictionary describing music album"""
	
	albumInfo = {'Artist': artist, 'Album': album, 'Genre': genre, 'Release Data': releaseDate}
	if trackNum:
		albumInfo['Tracks'] = trackNum
	return albumInfo
	


nameAlbum = makeAlbum('wu-tang clan', 'enter the wu-tang', 'classic hip-hop', 'November 9, 1993', '13')
print(nameAlbum)

