def puissance(a,b):
	if type(a)is not int or type(b)is not int:
		raise TypeError("Only integers are allowed")
	else:
		x = a**b
	return x
