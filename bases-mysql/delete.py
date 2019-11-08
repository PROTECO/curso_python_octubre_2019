import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="alejandro", 
                           passwd="2018_alejandro", 
                           database="personal")
cursor = conexion.cursor()

# Construir comando para borrar tabla
BorrarTabla = "DROP TABLE IF EXISTS Oficinas;"

# Borrar tabla
cursor.execute(BorrarTabla)
print("Se ha suprimido una tabla de la base de datos")

# Finalizar transacción y cerrar
conexion.commit()
conexion.close()