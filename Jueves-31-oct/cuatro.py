'''
4. Escriba un programa de Python para construir el patrón siguiente, usando un bucle anidado.

#  * 
#  >>
#  * * * 
#  >>>>>>>> 
#  >>>>>>>> 
#  >>>>>>>> 
#  * * * 
#  >>
#  *
'''
elem_basics = ['*','>>','***']
count = 0

for elem in elem_basics:
	print(elem)
	if count>=2:
		for i in range(3):
			print(">>"*4)
			if count >=4:
				print('***','>>','*',sep="\n")
			count+=1
	count +=1








