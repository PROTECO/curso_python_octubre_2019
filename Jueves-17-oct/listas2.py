#########################
# Listas, continución
##########################


lista = [2,3,6,4,6,1]

print("La lista tiene %d elementos" % len(lista))
print("El número %d se repite %d veces " % (lista[2],lista.count(lista[2]))) 

# Insertar elemento en una lista por posición  (posición,quéquieroinsertar)
lista.insert(0,7)
print(lista)

# Eliminar elemento de una lista por posición
del lista[1]
print(lista)


print("El número mayor de la lista es: %d " % max(lista) )

print("El número menor de la lista es: %d " % min(lista) )


########## Paso por valor

a = 4 
b = a

print("a = ",a)
print("b = ",b)

b = 120

print("a = ",a)
print("b = ",b)

########## Paso por referencia

l1  = ['a','b','c']
l2 = l1

print("Lista 1: ",l1)
print("Lista 2: ",l2)

l2[0] = 1

print("Lista 1: ",l1," id",id(l1))
print("Lista 2: ",l2," id",id(l2))

# Copiar lista

l3 = l1.copy()

print("Lista 2: ",l3," id",id(l3))

l3[1] = 2

print("Lista 2: ",l3," id",id(l3))
























