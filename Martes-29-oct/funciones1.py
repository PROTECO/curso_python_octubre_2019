###################
#   Funciones
###################

def hola_mundo(nombre):
	"""
	Funcíon que saluda a una persona 
	:param nombre Nombre de quien se va a saludar
	:return saludo El saludo que se va a mandar 
	"""
	saludo = "Hola mundo de: " + nombre
	return saludo	

saludo_regresado = hola_mundo('Jorge')

print(saludo_regresado)

print(hola_mundo.__doc__)








