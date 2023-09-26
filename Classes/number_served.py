class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")	
		print(f"The restaurant's cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"The restaurant is open")

	def set_number_served(self, number_served):
		self.number_served = number_served	

	def increment_number_served(self, more_served):
		self.number_served += more_served

restaurant = Restaurant("John's Pizza Galore", 'Pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(100)
print("Number served: " + str(restaurant.number_served))