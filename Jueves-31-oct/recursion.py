###################
# FUNCIONES - RECURSIÓN
###################

# Factorial iterativo    !0 = 1   !1= 1   !3= 1*2*3

def factorial_iterativo(numero):
	factorial = 1
	if numero == 1 or numero == 0:
		return 1
	else:
		for i in range(1,numero+1):
			factorial *= i
		return factorial

# print(factorial_iterativo(int(input("Calcula el factorial de: "))))

def factorial_recursivo(numero):
	if numero<2:
		return 1
	return numero*factorial_recursivo(numero-1)

# print(factorial_recursivo(int(input("Calcula el factorial de: "))))

# FIBONACCI
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,…

def fibonacci(numero):
	if numero == 0:
		return 0
	elif numero == 1:
		return 1
	else:
		return fibonacci(numero-1)+fibonacci(numero-2)

print("El fibonacci de %d es  %d"%(0,fibonacci(0)))
print("El fibonacci de %d es  %d"%(1,fibonacci(1)))
print("El fibonacci de %d es  %d"%(3,fibonacci(3)))
print("El fibonacci de %d es  %d"%(10,fibonacci(10)))
print("El fibonacci de %d es  %d"%(999,fibonacci(998)))









