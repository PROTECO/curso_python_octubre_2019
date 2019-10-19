#########################
# Diccionarios
##########################

# Estructuras que mapean un objeto llave-valor

diccionario = {"uno":"Jorge","dos":"Daniel","tres":"Alma"}

print(diccionario)

print(diccionario["uno"])   #Buscar por valor

calificaciones = {"Jorge":[1,2,3,4],"Bruno":8,"Óscar":10}

# Si no existe la llave, marcará error

print("La calificación de Jorge es: %s" 
	% calificaciones["Jorge"])

# Si no existe la llave, no marcará error

cals_jorge = calificaciones.get("Juan")

print("Calificaciones Jorge: ", cals_jorge)

calificaciones.update({"Jorge":10})  # Actualizando un elemento del diccionario
calificaciones.update({"Isa":10}).   # Añadiendo nuevo elemento al diccionario

print("Calificaciones Jorge: ", calificaciones["Jorge"])
print(calificaciones)

# Obteniendo las llaves del diccionario

print(list(calificaciones.keys()))

# Obteniendo los valores del diccionario

print(list(calificaciones.values()))

# Llaves y valores, en tuplas


print(list(calificaciones.items()))

# Crear una copia de un diccionario

calificaciones_copia = calificaciones.copy()







































