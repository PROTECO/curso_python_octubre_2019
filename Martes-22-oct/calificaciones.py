###############
# Condicional IF ELSE
###############

print("Escribe tus calificaciones: \n")

calculo = int(input("¿Cuánto sacaste en cálculo?\n"))
algebra = int(input("¿Cuánto sacaste en álgebra?\n"))
ecuaciones_diferenciales = int(input("¿Cuánto sacaste en E.D?\n"))
termo = int(input("¿Cuánto sacaste en termo?\n"))
quimica = int(input("¿Cuánto sacaste en quimica?\n"))

resultado = (calculo + algebra + ecuaciones_diferenciales +termo + quimica)/5

if resultado >= 7:
	print("Estás chido, aprobaste!")
else:
	print("Estás chavo, te veo el otro semestre!")

