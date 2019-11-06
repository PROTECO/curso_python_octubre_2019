"""
Escriba un programa Python para adivinar un número entre 1 y 9.

Nota: Se le pide al usuario que ingrese una conjetura. 
Si el usuario se equivoca, entonces el mensaje aparece de nuevo 
hasta que la suposición es correcta, con una conjetura exitosa, 
el usuario obtendrá un "bien adivinado". Mensaje, y el programa saldrá.
"""
import random
numero_aleatorio = random.randint(1,9)

intento = 3

while True:
	print("Tienes %d intentos"%intento)
	numero_adivinado = int(input("Adivina el número que pensé: "))
	if numero_adivinado == numero_aleatorio:
		print("¡Felicidades, has adivinado, el número que pensé es: %d"%numero_aleatorio)
		break
	else:
		print("¡Mal, intenta de nuevo!")
		intento -= 1 # intento = intento -1	
		if intento == 0:
			print("¡Lo siento, perdiste!")
			break












