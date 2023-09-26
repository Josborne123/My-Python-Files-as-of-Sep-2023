def make_album(title, artist, songs=None):
	title_artist = {'title': title, 'artist': artist}
	
	if songs:
		title_artist['songs'] = songs

	return title_artist

print("Enter 'q' at anytime to quit the program")

while True:
	title = input("Enter album title: ")
	if title == 'q':
		break
	artist = input("Enter artist: ")
	if artist == 'q':
		break

	print(make_album(title, artist))
