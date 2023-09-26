class Users:
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0
	def describe_person(self):
		print(f"This user's first name is {self.first_name.title()} and their last name is {self.last_name.title()}.")
		print(f"This user's age is {self.age} and their location is {self.location.title()}.")
	
	def greet_user(self):
		print(f"Hello {self.first_name.title()} {self.last_name.title()}. There is a new nando's near {self.location.title()} which is where you live.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0	


user = Users('john', 'osborne', 14, 'milngavie')
user.describe_person()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")