###############
# Python - MySQL
###############

import pymysql

# Conectarnos a una base de datos

conexion = pymysql.connect(host='127.0.0.1',
						   user='root',
						   passwd='hola123',
						   database='alumnos')
cursor = conexion.cursor()

# Crear una sentencia de SQL

sentencia_sql = 'SELECT * FROM alumno;'

# Ejecutar la sentencia

cursor.execute(sentencia_sql)
# Guardar los datos en una lista

registros = cursor.fetchall()

for registro in registros:
	print(registro)

# Finalizar

conexion.commit()
conexion.close()

 









