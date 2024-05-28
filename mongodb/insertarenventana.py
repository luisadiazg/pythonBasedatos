import pymongo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONTO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

MONGO_BASE_DATOS = "supermercado"
MONGO_TABLA = "productos"

def agregarProducto():
    cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONTO_TIEMPO_FUERA)
    basedatos = cliente[MONGO_BASE_DATOS]
    coleccion = basedatos[MONGO_TABLA]
    if len(nombre.get()) !=0 and len(Presentacion.get())!=0 and len(Precio.get()) != 0 and len(Proveedor.get()) != 0 :
        
        documento = {"nombre" : nombre.get(),"presentacion" : Presentacion.get(),"precio" : Precio.get(),"proveedor" : Proveedor.get()}
        coleccion.insert_one(documento)

def mostrarDatos(tabla):
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONTO_TIEMPO_FUERA)
        basedatos = cliente[MONGO_BASE_DATOS]
        coleccion = basedatos[MONGO_TABLA]
        for datos in coleccion.find():
            tabla.insert("", "end", values=(datos.get("nombre"), datos.get("presentacion"), datos.get("precio"), datos.get("proveedor")))
    except pymongo.errors.ConnectionFailure as errorConection:
        print("Fallo la conexión")

ventana = Tk()

tabla = ttk.Treeview(ventana, columns=("Nombre", "Presentación", "Precio", "Proveedor"), show="headings")
tabla.grid(row=1, column=0, columnspan=5)
tabla.heading("#1", text="Nombre")
tabla.heading("#2", text="Presentación")
tabla.heading("#3", text="Precio")
tabla.heading("#4", text="Proveedor")

# Centrar el contenido de las columnas
tabla.column("#1", anchor="center")
tabla.column("#2", anchor="center")
tabla.column("#3", anchor="center")
tabla.column("#4", anchor="center")

# Campos para insertar
#Nombre
Label(ventana, text="Nombre").grid(row=2, column=0)
nombre = Entry(ventana)
nombre.grid(row=2, column=1)

#Presentación
Label(ventana, text="Presentación").grid(row=3, column=0)
Presentacion = Entry(ventana)
Presentacion.grid(row=3, column=1)

#Precio
Label(ventana, text="Precio").grid(row=4, column=0)
Precio = Entry(ventana)
Precio.grid(row=4, column=1)

#Proveedor
Label(ventana, text="Provedor").grid(row=5, column=0)
Proveedor = Entry(ventana)
Proveedor.grid(row=5, column=1)

#Boton agregar
agregar = Button(ventana, text="Agregar producto", command=agregarProducto)
agregar.grid(row=5,column=3)
mostrarDatos(tabla)
ventana.mainloop()