def puissance(a,b):
	if type(a)is not int or type(b)is not int:
		raise TypeError("Only integers are allowed")
	x = a**b
	return x
