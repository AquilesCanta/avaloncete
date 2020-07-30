from io import open
import os

class Producto:
    def __init__(self, nombre, cantidad):
        self.__producto = nombre
        self.__cantidad = int(cantidad)

    def convertir_a_string(self):
        return f"{self.__producto}:{self.__cantidad}\n"

    def ingresar_al_inventario(self):
        with open (PATH_ARCHIVO_EXTERNO, "a") as inventario_persistente:
            inventario_persistente.write(self.convertir_a_string())
    
def leer_archivo():
    with open(PATH_ARCHIVO_EXTERNO, "r") as inventario_persistente:
        diccionario_inventario = {}
        inventario = inventario_persistente.readlines()
        for producto in inventario:
            producto = producto.split(":")
            diccionario_inventario[producto[0]] = int(producto[1])
        return diccionario_inventario

def ingresar_comando():
    comando = input("ingrese el comando: ")
    comando = comando.lower()
    comando = comando.split()
    return comando

def mostrar_comando_invalido():
    print ("El comando no es valido. Comandos aceptados: [agregar, quitar, terminar, imprimir]")

def imprimir_inventario(inventario):
    str_inicial = "|Producto       |Cantidad      |"
    separador =   "+---------------+--------------+"
    str_final = ""
    producto_imp = ""
    cantidad_imp = ""
    for item in inventario:
        producto_imp = item
        cantidad_imp = str(inventario[producto_imp])
        while len(cantidad_imp) < 14:
            cantidad_imp += " "
        if len(producto_imp) >= 15:
            producto_imp = producto_imp[0:12] 
            producto_imp += "..."
            str_final += f"|{producto_imp}|{cantidad_imp}|\n{separador}\n" 
        else:
            while len(producto_imp) != 15:
                producto_imp += " "
            str_final += f"|{producto_imp}|{cantidad_imp}|\n{separador}\n"
    print(f"{str_inicial}\n{separador}\n{str_final}")

PATH_ARCHIVO_EXTERNO = "inventario_prueba.txt"

if os.path.isfile(PATH_ARCHIVO_EXTERNO):
    diccionario_inventario = leer_archivo()
else:
    with open (PATH_ARCHIVO_EXTERNO, "a") as inventario_persistente:
        diccionario_inventario = {}

comando = ingresar_comando()

while comando[0] != "terminar":
        
    if comando[0] == "imprimir":
        imprimir_inventario(diccionario_inventario)
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
            if producto not in diccionario_inventario:
                diccionario_inventario[producto] = 0
            diccionario_inventario[producto] += cantidad

        elif accion == "quitar":
            if producto not in diccionario_inventario:
                print(f"{producto} no se encuentra en el inventario")
            elif cantidad > diccionario_inventario[producto]:
                print("Hay menos productos de los que queres quitar")
            else:
                diccionario_inventario[producto] -= cantidad

        else:
            mostrar_comando_invalido()
            comando = ingresar_comando()
            continue

        comando = ingresar_comando()

with open(PATH_ARCHIVO_EXTERNO, "w") as inventario_persistente:
    for i in diccionario_inventario:
        nombre = i
        cantidad = diccionario_inventario[i]
        prod = Producto(nombre, cantidad)
        prod.ingresar_al_inventario()