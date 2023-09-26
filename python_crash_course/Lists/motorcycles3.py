motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles2)
motorcycles2.remove('suzuki')
print(motorcycles2)
