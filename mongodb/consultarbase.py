import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

#MONGO_BASE_DATOS = "supermercado"
#MONGO_TABLA = "productos"
MONGO_BASE_DATOS = input("ingrese la base de datos\n")
MONGO_TABLA = input("ingrese la tabla a consultar\n")
consulta = input("Igrese la consulta\n")
try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
    basedatos = cliente[MONGO_BASE_DATOS]
    coleccion = basedatos[MONGO_TABLA]
    if consulta == "":
        for datos in coleccion.find():
            print(datos)
    else:
        for datos in coleccion.find():
            print(datos[consulta])
    #crear una base de datos
    nomtabla = input("ingrese nombre de la tabla a crear")
    #basedatos.createCollection(nomtabla)
    basedatos.create_collection(nomtabla)

    #cliente.server_info()
    #print("Coneccion exitosa")
except pymongo.errors.ConnectionFailure as errorConection:
    print("Fallo la coneccion")

    