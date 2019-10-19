#########################
# Tuplas
##########################


tupla = (1,"hola","adios",True)

tupla2 = 1,2,3,4,5,7,6  # Empaquetamiento  


print(tupla[1])  # Indexación

print(tupla2)

a,b,c,d,e,f,g = tupla2. # Desempaquetamiento

print(d)

tuplachida = (('a','b','c'),[1,2,3])

tuplachida[1][0] = "hola"

print(tuplachida)

lista_otro_bando = [1,2,4,5]

print(type(lista_otro_bando))

tupla_closet = tuple(lista_otro_bando)

print(type(tupla_closet))













