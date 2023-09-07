import fonctions as f
### use of the fonctions.py file

condition = True
while condition == True:
	print("Hello, World!")
	a = int(input("entrez le nombre a : "))
	b = int(input("entrez le nombre b : "))
	res = f.puissance(a,b)
	print(res)
