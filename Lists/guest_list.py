invite_dinner = ['tom hardy', 'charlie day', 'alan forsyth', 'jeroen hertzberger']
print(invite_dinner)

print(f"Hello {invite_dinner[0].title()}, would you like to come to my dinner party")
print(f"Hello {invite_dinner[1].title()}, would you like to come to my dinner party")
print(f"Hello {invite_dinner[2].title()}, would you like to come to my dinner party")
print(f"Hello {invite_dinner[3].title()}, would you like to come to my dinner party")

print(f"\nUnfortunately {invite_dinner[2].title()} can't make it to dinner tonight")

del invite_dinner[2]
invite_dinner.insert(0, 'fiona osborne')
print(f"Hello {invite_dinner[0].title()}, would you like to come to my dinner party tommorow night")

print(f"Greetings {invite_dinner[1].title()}, I am just checking to see if you can still make my party tommorow")
print(f"Greetings {invite_dinner[2].title()}, I am just checking to see if you can still make my party tommorow")
print(f"Greetings {invite_dinner[3].title()}, I am just checking to see if you can still make my party tommorow")

print(f"\nHi {invite_dinner[0]} just saying that I found a bigger dinner table so i will be inviting more people to my dinner")
print(f"Hi {invite_dinner[1]} just saying that I found a bigger dinner table so i will be inviting more people to my dinner")
print(f"Hi {invite_dinner[2]} just saying that I found a bigger dinner table so i will be inviting more people to my dinner")
print(f"Hi {invite_dinner[3]} just saying that I found a bigger dinner table so i will be inviting more people to my dinner")

invite_dinner.insert(0, 'Kenneth Osborne')
invite_dinner.insert(4, 'James Osborne')
invite_dinner.append('John Osborne')
print(invite_dinner)

print(f"\nHello {invite_dinner[0].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[1].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[2].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[3].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[4].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[5].title()}, I am inviting you to my dinner party")
print(f"Hello {invite_dinner[6].title()}, I am inviting you to my dinner party")

print("\nSorry everybody I can now only make room for two people")
print(invite_dinner)

kenneth = invite_dinner.pop(0)
print(f"\nSorry {kenneth} I don't have room for you at my table anymore")
print(invite_dinner)

james = invite_dinner.pop(3)
print(f"Sorry {james} you can't come to my party anymore")

john = invite_dinner.pop()
print(f"Sorry {john} you can't come to my party anymore")

jeroen = invite_dinner.pop(3)
print(f"Sorry {jeroen} you can't come to my party anymore")

fiona = invite_dinner.pop(0)
print(f"Sorry {fiona} you can't come to my party anymore")

print(f"\n Well Done {invite_dinner[0]} you can still come to my party")
print(f"\n Well Done {invite_dinner[1]} you can still come to my party")

del invite_dinner[0]
del invite_dinner[0]

print(invite_dinner)

print(len(invite_dinner))