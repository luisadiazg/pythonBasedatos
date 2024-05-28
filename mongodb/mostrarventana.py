import pymongo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 5000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

MONGO_BASE_DATOS = "supermercado"
MONGO_TABLA = "productos"

def mostrarDatos(tabla):
    try:
        cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONTO_TIEMPO_FUERA)
        basedatos = cliente[MONGO_BASE_DATOS]
        coleccion = basedatos[MONGO_TABLA]
        for datos in coleccion.find():
                tabla.insert("", "end", values=(datos.get("nombre"), datos.get("presentacion"), datos.get("precio"), datos.get("proveedor")))
                #print(datos[nombre])
    except pymongo.errors.ConnectionFailure as errorConection:
        print("Fallo la coneccion")

ventana = Tk()
tabla = ttk.Treeview(ventana,columns=("Nombre", "Presentación", "Precio", "Proveedor"), show="headings") #creo las columnas
tabla.grid(row=1,column=0,columnspan=5)
tabla.heading("#1",text="Nombre")
tabla.heading("#2",text="Presentación")
tabla.heading("#3",text="Precio")
tabla.heading("#4",text="Proveedor")
mostrarDatos(tabla)
ventana.mainloop() 