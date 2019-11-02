############################
#   FUNCIONES - PARÁMETROS
############################

#PARÁMETRO POR OMISIÓN
def saludar(nombre, mensaje='fmdosamfodsamf',edad=''):
	print(mensaje,nombre,edad)

#saludar(nombre=input("¿Cómo te llamas?\n"),
#		mensaje='¡Qué onda!',
#		edad='10')

# PARÁMETROS ARBITRARIOS - SE GUARDAN EN UNA TUPLA
'''def imprime_calificaciones(nombre,*calificaciones):
	print('Calificaciones de: %s'%nombre)
	print(type(calificaciones))
	for calificacion in calificaciones:
		print(calificacion)
'''
# imprime_calificaciones('Jorge',[9,7,10,8,11,9,5,5])

# PARÁMETROS KWARGS(KEY-WORD ARGUMENTS)  - SE GUARDAN EN UN
def imprime_calificaciones(curso,*nombres,**calificaciones):
	print('Curso de: %s'%curso)

	for nombre in nombres:
		print(nombre)
	for calificacion in calificaciones:
		print(calificaciones[calificacion])

#imprime_calificaciones('Python','César','Sína','Daniel','Ángel','Jessica',
#						alumno1=10,alumno2=9,alumno3=10,alumno4=9)


# Desempaquetamiento

def calcular_descuento(importe,descuento):
	return importe - (importe*descuento/100)

# datos = [1500,10]

# print(calcular_descuento(*datos))
 
datos = {"importe":1500,"descuento":10}

print(calcular_descuento(**datos))





























