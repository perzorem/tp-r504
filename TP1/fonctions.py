def puissance(a,b):
	if type(a)is not int or type(b)is not int:
		raise TypeError("Only integers are allowed")
	else:
		result = a
		if a == 0 and b != 0:
			if b<0:
				return("vous ne pouvez pas avoir une puissance négative")
			else:
				return(a)
			return(a)
		if a == 0 and b == 0:
			return(1)
		if a != 0 and b ==0:
			if a<0:
				return(-1)
			else:
				return(1)
		if a != 0 and b != 0:
			for i in range(1,b,1):
				result = result*a
			return(result)
