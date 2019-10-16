######################
# Continuación cadenas
#  Cuestionario: bit.ly/2MgIqar
######################

#Características de las cadenas

#Indexación
cad = 'hola'
print(cad[0])
print(cad[1])
print(cad[2])
print(cad[3])
# cad[1] = 'u' #No se puede porque es inmutable
# Subcadenas, slicing ->rebanada

print(cad[1:4], " ke ase?")
cad2 = '¿Cómo estan?'
print(cad2[5:10])
print(cad2[7:10])
print(cad2[6:11])

#Concatenación

saludo = "Qué onda!"
despedida = "Adiós!"

saluspedida = saludo + despedida
print(saluspedida)
print(saludo + despedida )
halago = "El profe es el: "
bueno = "\nmejor"
print(halago,bueno*100)

# Cadena cruda

print("Python es \nlo máximo!!!")

print(r"Python es \nlo máximo!!!")

# Placeholders

a = 2
b = 3
print("El valor a es: %d y de b es: %d " % (a,b))












