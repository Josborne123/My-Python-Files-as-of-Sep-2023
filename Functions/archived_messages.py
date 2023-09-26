def send_messages(text_messages):
	while text_messages:
		text = text_messages.pop()
		print(text)
		sent_messages.append(text)




sent_messages = []

text_messages = ['Hello Mum', 'whats for tea', 'can you pick me up from the train station please', "I'm at hilfoot"]

# [:] - Creates a copy of the text_messages list and then uses that so it keeps the original list intact.
send_messages(text_messages[:])

print("\n")

print(sent_messages)
print(text_messages)