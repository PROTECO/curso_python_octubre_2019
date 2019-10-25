############################
# FOREACH
############################

lista = [1,2,3.14,"Hola",True,(2,3),2]

for elemento in lista:
	print("[%d] Elemento: %s" %(lista.index(elemento),elemento))

dias = ('Lunes',
		'Martes',
		'Miércoles',
		'Jueves',
		'Viernes',
		'Sábado',
		'Domingo'
		)

for dia in dias:
	if dia == 'Viernes':
		print("¡Vamos por unas chelas!")
	else:
		print("Hoy no toca, vamos al curso!")

calificaciones = {
				  'Jorge': 10,
				  'César': 9,
				  'Jocelyn': 8,
				  'Jacob': 7 
				  }
# ['Jorge','César','Jocelyn','Jacob'] -> llaves

for alumno in calificaciones:
	print("%s sacó %d "%(alumno,calificaciones[alumno]))

# Iteración for para desempaquetar

colores_favs = [("Jorge", "Azul"),
				("Itzel", "Verde"),
				("Enrique", "Rojo"),
				("Jesús", "Morado"),
				("Ángel", "Vino")
				]
for nombre,color in colores_favs:
	print("El color %s es el favorito de %s" % (color,nombre))

cadena = "Ya-mañana-es-viernes!"

for letra in "Ya mañana es viernes!":
	print(letra+"-")










