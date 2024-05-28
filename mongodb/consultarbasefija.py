import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

MONGO_BASE_DATOS = "supermercado"
MONGO_TABLA = "productos"
try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
    basedatos = cliente[MONGO_BASE_DATOS]
    coleccion = basedatos[MONGO_TABLA]
    for datos in coleccion.find():
            print(datos)
            #print(datos[nombre])
except pymongo.errors.ConnectionFailure as errorConection:
    print("Fallo la coneccion")

    