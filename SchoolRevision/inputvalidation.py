name = str(input("Please enter your name: "))
year = int(input("Please enter the year you were born: "))

while year < 1910 or year > 2022:
    print("Invalid")
    year = int(input("Please enter the year you were born again: "))

print(name)
print(year)