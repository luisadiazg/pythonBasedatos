import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

MONGO_BASE_DATOS = "prueba5"
# Insertar un documento en la colección
documento = {
    "nombre": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "precio": 15.99,
    "proveedor": "Editorial Sudamericana",
    "stock": 100
}

try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
    base = cliente[MONGO_BASE_DATOS]
    coleccion = base["libros"]
    insertar = coleccion.insert_one(documento)
    print("ID insertado", insertar.inserted_id)
except pymongo.errors.ConnectionFailure as errorConection:
    print("Fallo la coneccion")

    