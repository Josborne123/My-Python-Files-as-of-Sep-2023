words = {
		'consider': 'deem to be',
 		'minute': 'infinitely or immeasureably small', 
 		'accord': 'concurrence of opinion', 
 		'evident': 'clearly revealed to the mind or the senses or judgment',
		'practice': 'a customary way of operation or behaviour',	
		'conduct': 'direct the course of; manage or control',
		'engage': "consume all of one's attention or time",
		'obtain': 'come into possession of'
		}

# .items() allows you to print out the key-value pairs		
for word, definition in words.items():
	print(f"{word.title()} means {definition}")