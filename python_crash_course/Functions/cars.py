def car(manufacture, model_name, **kwarg):
	kwarg['manufacture'] = manufacture
	kwarg['model_name'] = model_name
	return kwarg


car1 = car('audi', 'R8', bought=2002)
print(car1)

print()

car2 = car('volvo', 'V40', bought=2019, last_cleaned='09/07/2020')
print(car2)