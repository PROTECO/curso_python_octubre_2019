import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="alejandro", 
                           passwd="2018_alejandro", 
                           database="personal")
cursor = conexion.cursor()

# Definir comandos para insertar registros
registro1 = "INSERT INTO Oficinas VALUES ('Central', 'Sevilla');"
registro2 = "INSERT INTO Oficinas VALUES ('Norte', 'Bilbao');"
registro3 = "INSERT INTO Oficinas VALUES ('Extremadura', 'Badajoz');"

# Ejecutar comandos
cursor.execute(registro1)
cursor.execute(registro2)
cursor.execute(registro3)

# Finalizar transacción y cerrar
conexion.commit()
conexion.close()