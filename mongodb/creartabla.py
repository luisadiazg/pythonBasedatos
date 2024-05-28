import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"
MONGO_BASE_DATOS = "supermercado"
MONGO_TABLA = "prueba4"
try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
    basedatos = cliente[MONGO_BASE_DATOS]
    #crear una base de datos
    basedatos.create_collection(MONGO_TABLA)
    coleccion = basedatos.list_collection_names()
    for colecciones in coleccion:
        print(coleccion)
        
except pymongo.errors.ConnectionFailure as errorConection:
    print("Fallo la coneccion")

    