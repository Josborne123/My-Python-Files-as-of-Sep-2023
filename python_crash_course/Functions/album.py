def make_album(title, artist, songs=None):
	title_artist = {'title': title, 'artist': artist}
	
	if songs:
		title_artist['songs'] = songs

	return title_artist

t_a = make_album("John is Amazing!", 'John Osborne')	
print(t_a)

t_a = make_album("Grumpy", 'james osborne', 8)
print(t_a)

t_a = make_album('Lamp', 'Dj Kenneth Osborne', 330)
print(t_a)