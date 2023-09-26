class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")	
		print(f"The restaurant's cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"The restaurant is open")

restaurant = Restaurant("John's Pizza Galore", 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print("")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("")

restaurant2 = Restaurant("Kenneth's Mouth Suprise", 'Sugar')
print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)

print("")

restaurant2.describe_restaurant()