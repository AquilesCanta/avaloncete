from io import open
from datetime import datetime
import os

class Producto:
    def __init__(self, nombre, cantidad, fecha_ingreso):
        self.__producto = nombre
        self.__cantidad = int(cantidad)
        self.__fecha_ingreso = fecha_ingreso
    
    def dar_nombre(self):
        return self.__producto

    def dar_cantidad(self):
        return int(self.__cantidad)

    def dar_fecha_ingreso(self):
        return self.__fecha_ingreso

    def agregar_cantidad(self, cantidad):
        self.__cantidad += cantidad

    def quitar_cantidad(self, cantidad):
        self.__cantidad -= cantidad

    def convertir_a_string(self):
        return f"{self.__producto}|{self.__cantidad}|{self.__fecha_ingreso}\n"
    
def leer_archivo():
    with open(PATH_ARCHIVO_EXTERNO, "r") as inventario_persistente:
        inventario = inventario_persistente.readlines()
        diccionario_productos = {}
        for producto in inventario:
            producto = producto.split("|")
            producto = Producto(producto[0], producto[1], producto[2])
            nombre = producto.dar_nombre()
            diccionario_productos[nombre] = producto
        return diccionario_productos

def ingresar_comando():
    comando = input("ingrese el comando: ")
    comando = comando.lower()
    comando = comando.split()
    return comando

def mostrar_comando_invalido():
    print ("El comando no es valido. Comandos aceptados: [agregar, quitar, terminar, imprimir]")

def imprimir_inventario(inventario):
    str_inicial = "|Producto       |Cantidad      |Ingreso            |"
    separador =   "+---------------+--------------+-------------------+"
    str_final = ""
    producto_imp = ""
    cantidad_imp = ""
    fecha_ingreso_imp = ""
    for item, valor in inventario.items():
        producto_imp = item
        cantidad_imp = str(valor.dar_cantidad())
        fecha_ingreso_imp = valor.dar_fecha_ingreso()
        while len(cantidad_imp) < 14:
            cantidad_imp += " "
        if len(producto_imp) >= 15:
            producto_imp = producto_imp[0:12] 
            producto_imp += "..."
            str_final += f"|{producto_imp}|{cantidad_imp}|{fecha_ingreso_imp[0:19]}|\n{separador}\n" 
        else:
            while len(producto_imp) != 15:
                producto_imp += " "
            str_final += f"|{producto_imp}|{cantidad_imp}|{fecha_ingreso_imp[0:19]}|\n{separador}\n"
    print(f"{separador}\n{str_inicial}\n{separador}\n{str_final}")

PATH_ARCHIVO_EXTERNO = "inventario_prueba.txt"

if os.path.isfile(PATH_ARCHIVO_EXTERNO):
    diccionario_productos = leer_archivo()
else:
    with open (PATH_ARCHIVO_EXTERNO, "a") as inventario_persistente:
        diccionario_productos = {}

comando = ingresar_comando()

while comando[0] != "terminar":
        
    if comando[0] == "imprimir":
        imprimir_inventario(diccionario_productos)
        comando = ingresar_comando()
        continue
    else:
        if len(comando) != 3:
            mostrar_comando_invalido()
            comando = ingresar_comando()
            continue
        else:
            accion = comando[0]
            producto = comando[1] 
            try:
                cantidad = int(comando[2])
            except:
                print(f"{comando[2]} no se puede intepretar como numero, ingrese un numero. Ejemplo: agregar aceite 4.")
                comando = ingresar_comando()
                continue

        if accion == "agregar":
            fecha = str(datetime.now())
            if producto not in diccionario_productos:
                producto_nuevo = Producto(producto, cantidad, fecha)
                nombre = producto_nuevo.dar_nombre()
                diccionario_productos[nombre] = producto_nuevo
            else:
                producto_actual = diccionario_productos[producto] 
                producto_actual.agregar_cantidad(cantidad)

        elif accion == "quitar":
            if producto not in diccionario_productos:
                print(f"{producto} no se encuentra en el inventario")
            else:
                producto_actual = diccionario_productos[producto]
                cantidad_inicial = producto_actual.dar_cantidad()
                if cantidad_inicial < cantidad:
                    print("Hay menos productos de los que queres quitar")
                else:
                    producto_actual.quitar_cantidad(cantidad)

        else:
            mostrar_comando_invalido()
            comando = ingresar_comando()
            continue

        comando = ingresar_comando()

with open(PATH_ARCHIVO_EXTERNO, "w") as inventario_persistente:
    for item, valor in diccionario_productos.items():
        inventario_persistente.write(valor.convertir_a_string())

