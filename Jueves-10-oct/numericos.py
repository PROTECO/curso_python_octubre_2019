#!/usr/bin/python3
# -*- coding: utf-8 -*-

######################################################################
# Las líneas anteriores, sólo sirven en python 2.x. 				 #
# La primera nos ayuda a indicar con qué versión se ejecutará python #
# La segunda línea nos ayuda con la codificación en caso de que 	 #
# nuestro código tenga acentos, dieresis, entre otros caracteres.	 #	
######################################################################


######################
# Números
######################

#Enteros

a = 10
b = 8

#Flotantes

pi = 3.14
e = 2.72

#Complejos

c = 2 +5j
d = 7j

#Operadores aritméticos con enteros

print("\n Operadores aritméticos con enteros y flotantes\n")

print("Suma de",a,"+",b,"=",a+b)
print("Resta de",a,"-",b,"=",a-b)
print("Multiplicación de",a,"*",pi,"=",a*b)
print("División de",a,"/",b,"=",a/b)
print("División entera ",a,"/",b,"=",a//b)
print("Modulo de",a,"es ",a%2)
print("Potencia de ",e,"a la 2: ",e**2)

print("\n Operadores aritméticos con complejos\n")

print("Suma de",c,"+",d,"=",c+d)
print("Resta de",c,"-",d,"=",c-d)
print("Multiplicación de",c,"*",d,"=",c*d)
print("División de",c,"/",d,"=",c/d)
# print("División entera ",c,"/",d,"=",c//d) No es posible realizar división entera entre complejos
# print("Modulo de",c,"es ",c%2) No es posible obtener módulo de un complejo
print("Potencia de ",d,"a la 2: ",d**2)

hexa = 0x0d  #Hexadecimal ->13
octal = 0o13  # Octal
binario = 0b0101110  #Binario

#Al imprimir autómaticamente se ponen en base decimal

print("En decimal: " ,hexa)
print("En decimal: ",octal)
print("En decimal",binario)





