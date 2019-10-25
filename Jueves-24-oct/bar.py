##############
# CONDICIONAL - EJERCICIO
##############


nombre = input("Hola, cómo te llamas? ")
edad = int(input("Introduce tu edad: "))
''' 
 La función input devuelve una cadena de lo 
 que introducimos por teclado.
 Si queremos algún otro tipo de dato
 debemos hacer un casteo o conversión de tipo
'''
# print(type(edad))

if edad <= 0: 
	print("Lo siento, aún no naces, introduce edad válida")  
elif edad < 18:
	print("Lo siento %s no puedes pasar, estas chavo! " % nombre)
elif edad >=18 and edad<=75:
	print("Bienvenido %s , pasala chido!" % nombre)
elif edad >75 and edad <=90:
	print("Lo siento %s no puedes pasar, estas viejo! " % nombre)
else:
	print("Estas seguro de tu edad?")






