#################################################################################################
# Tarea 3 , Problema 10
# Escriba un programa de Python que solicite una cadena al usuario e imprima la misma cadena omitiendo todas sus vocales.
# EJEMPLO: Entrada: "¡Hola, mundo!" - Salida: "¡Hl, mnd!"
#################################################################################################


cadena = input("Escribe una cadena, la dejaré sin vocales: ")
cadena_aux = ''
vocales = ['a','e','i','o','u','A','E','I','O','U']

for letra in cadena:
	if letra not in vocales:
		cadena_aux += letra

print("La cadena sin vocales es: %s"%cadena_aux)
print("La cadena sin vocales es: ",''.join(letra for letra in cadena if letra not in 'aeiouAEIOU'))


