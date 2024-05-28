import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"


try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
    cliente.server_info()
    print("Coneccion exitosa")
except pymongo.errors.ConnectionFailure as errorConection:
    print("Fallo la coneccion")

    