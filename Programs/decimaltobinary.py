def DecToBin(num):
	if num > 1:
		DecToBin(num // 2)
	print(num % 2, end = '')

dec_value = int(input("Please enter a number to convert to binary: "))
DecToBin(dec_value)		