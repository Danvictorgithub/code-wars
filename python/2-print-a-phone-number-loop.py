number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def create_phone_number(n):
	num_string = ""
	for i in range(len(n)):
		if i == 0:
			num_string += "("
		if i < 3 and not i > 3:
			num_string += str(n[i])
		if i == 3:
			num_string += ") "
		if i < 6 and not i < 3:
			num_string += str(n[i])
		if i == 6:
			num_string += "-"
		if i < 10 and not i < 6:
			num_string += str(n[i])
	return num_string
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


	
