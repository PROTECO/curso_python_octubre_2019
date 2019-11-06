class Perro:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def __add__(self, otro_perro):
		return self.edad + otro_perro.edad

sol = Perro('Sol',3)
bola = Perro('Bola',1)

print('Suma de edades: ',sol+bola)