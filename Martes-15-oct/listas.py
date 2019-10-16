######################
# Listas
######################

mandado = [ 'jabón',
			'comida',
			'sopa',
			'agua',
			'pan',
			'leche',
			'cereal',
			'atún',
			'café'
			]

print(mandado[1:])
print("Me falta por comprar: ", mandado[6:9])
print(mandado[5])

vocales = ['E','I','O']

vocales += ['A']
# Casteo o conversión a otro tipo de dato con función
vocales = list('U') + vocales
print(vocales)

# Métodos internos de la clase List
# Ordenamiento
vocales.sort()
mandado.sort()
print(vocales)
print(mandado)

numeros = [3,7,1,6,8,9,2,4,5]

numeros.sort()
print(numeros)

# Revertir lista
numeros.reverse()
print(numeros)

# Indexable

numeros[4] = 100 #Sí soporta asignación por item 
print(numeros)

lista = [1,"hola",True,"hola",[1,2,3]]

print(lista[1][1:4])
print(lista*3)

print(lista[-4])



print(lista.index(1))

# Insertar elemento

lista.insert(3,"A")
print(lista)

# Remover último elemento

lista.pop()
print(lista)

# Remover elemento indicado

lista.remove("hola")
print(lista)






