students = int(input("How many students are there in the test data: "))

longestName = ''
for index in range(students):
    name = input('Enter your name: ')
    if len(name) > len(longestName):
        longestName = name

print('The longest name is ' + str(longestName) + " at a length of " + str(len(longestName)) + " characters")
