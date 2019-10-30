############################
# FOREACH
############################

numeros = [1,2,3,4]

for numero in numeros:
	print(numero * .16)

dias = (
		'Lunes',
		'Martes',
		'Miercoles',
		'Jueves',
		'Viernes',
		'Sabado',
		'Domingo')

for dia in dias:
	if dia == 'Martes':
		print('Toca python, hay que llegar tempra!')
	else:
		print('Hay que hacer la tarea de python')

calificaciones = {
				'Jorge': 10,
				'Sína': 9,
				'Daniel':8,
				'Ángel': 9
				}
# llaves -> ('Jorge','Sína','Daniel','Ángel')

for alumno in calificaciones:
	print("%s sacó %d " %(alumno,calificaciones[alumno]))

# Iteración for para desempaquetar

colores_favs = [("Jorge", "Azul"),
				("Itzel", "Verde"),
				("Enrique", "Rojo"),
				("Jesús", "Morado"),
				("Ángel", "Vino")
				]
for nombre,color in colores_favs:
	print("El color %s es el favorito de %s" % (color,nombre))

















