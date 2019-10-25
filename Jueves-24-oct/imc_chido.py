###############
# WHILE IMC
###############

while True:
	peso = float(input("Ingresa tu peso: \n"))
	altura = float(input("Ingresa tu estatura: \n"))
	imc = peso/altura**2
	if imc<18.5:
		print("Come más tacos!")
	elif imc>=18.5 and imc<25:
		print("Estas normal, no te preocupes! IMC= %d"%imc)
	elif imc>=25 and imc<30:
		print("Estas en sobrepeso, bájale a los tacos! IMC= %d"%imc)
	elif imc>=30 and imc<34.4:
		print("Estas O B E S O, prohíbidos los tacos! IMC= %d"%imc)
	else:
		print("Estas a un taco de morir IMC= %d"%imc)
	salir = input('Presiona "s" para salir o "c" calcular de nuevo:  	')
	if salir == 's' or salir == 'S':
		break 










