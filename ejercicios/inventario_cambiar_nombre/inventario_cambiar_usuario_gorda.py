from io import open
from datetime import datetime
import os

class Modificacion_producto:
    def __init__(self, nombre):
        self.__nombre_producto = nombre
        self.__historial_cantidad = []
        self.__historial_fecha = []
        self.__historial_usuarios = []

    def imprimir_historial(self):
        lista_modificaciones = []
        for i in range(len(self.__historial_cantidad)):
            if i == 0:
                modificacion = self.__historial_cantidad[0]
                nuevo_valor = modificacion
            else:
                modificacion = self.__historial_cantidad[i] 
                nuevo_valor = nuevo_valor + self.__historial_cantidad[i]
            fecha = self.__historial_fecha[i]
            usuario = self.__historial_usuarios[i]
            string = f"Modificación: {modificacion}, Nuevo valor: {nuevo_valor}, Fecha de modificación: {fecha}, Usuario: {usuario}"
            lista_modificaciones.append(string)
        print(f"$ {self.__nombre_producto}")
        for i in lista_modificaciones:
            print(i)

    def agregar_lista_cantidad(self, lista):
        self.__historial_cantidad = [int(i) for i in lista]
    
    def agregar_lista_fechas(self, lista):
        self.__historial_fecha = lista

    def agregar_lista_usuarios(self, lista):
        self.__historial_usuarios = lista

    def actualizar_historiales(self, fecha, cantidad, usuario):
        self.__historial_fecha.append(fecha)
        self.__historial_usuarios.append(usuario)
        self.__historial_cantidad.append(int(cantidad))

    def string_historial_cantidad(self):
        string_final = f"#|{self.__nombre_producto}|"
        for i in range(len(self.__historial_cantidad)):
            if i != len(self.__historial_cantidad) - 1:
                string_final += str(self.__historial_cantidad[i]) + "|"
            else: 
                string_final += str(self.__historial_cantidad[i])
        return f"{string_final}\n"

    def string_historial_fecha(self):
        string_final = f"$|{self.__nombre_producto}|"
        for i in range(len(self.__historial_fecha)):
            if i != len(self.__historial_fecha) - 1:
                string_final += self.__historial_fecha[i] + "|"
            else:
                string_final += self.__historial_fecha[i]
        return f"{string_final}\n"

    def string_historial_usuario(self):
        string_final = f"%|{self.__nombre_producto}|"
        for i in range(len(self.__historial_usuarios)):
            if i != len(self.__historial_usuarios) - 1:
                string_final += self.__historial_usuarios[i] + "|"
            else:
                string_final += self.__historial_usuarios[i]
        return f"{string_final}\n"

class Producto:
    def __init__(self, nombre, cantidad):
        self.__nombre_producto = nombre
        self.__cantidad_final = int(cantidad)

    def agregar_cantidad(self, cantidad):
        self.__cantidad_final += cantidad

    def quitar_cantidad(self, cantidad):
        self.__cantidad_final -= cantidad

    def dar_cantidad(self):
        return self.__cantidad_final

    def dar_nombre(self):
        return self.__nombre_producto

    def convertir_producto_a_string(self):
        return f"@|{self.__nombre_producto}|{self.__cantidad_final}\n"

def crear_o_autenticar_usuario(diccionario_usuarios):
    usuario_actual = None
    while usuario_actual == None:
        print ("Utilice el comando 'AUTENTICAR' si ya dispone de un usuario, de lo contrario utilice el comando 'CREAR'")
        inicio = input("Desea 'AUTENTICAR' o 'CREAR': ")
        if inicio == "autenticar":
            if len(diccionario_usuarios) == 0:
                print("No hay usuarios registrados")
            else:    
                usuario = input("Usuario: ")
                contrasenia = input("Contraseña: ")
                if usuario in diccionario_usuarios:
                    if diccionario_usuarios[usuario] == contrasenia:
                        usuario_actual = usuario
                    else:
                        print("Error de autenticación.")
                else:
                    print("Error de autenticación.")
        elif inicio == "crear":
            usuario = input("Ingrese el nombre del usuario nuevo: ")
            contrasenia = input("contraseña:")
            if usuario in diccionario_usuarios:
                    print("Error de autenticación.")
                    usuario = None
            else:
                diccionario_usuarios[usuario] = contrasenia
                usuario_actual = usuario   
        else:
            print("El comando es incorrrecto.")

    print(f"Bienvenido {usuario_actual}")
    return usuario_actual, diccionario_usuarios

def ingresar_comando():
    comando = input("ingrese el comando: ")
    return comando.lower().split()

def mostrar_comando_invalido():
    print ("El comando no es valido. Comandos aceptados: [agregar, quitar, terminar, imprimir, historia 'nombre del producto']")

def imprimir_inventario(inventario):
    str_inicial = "|Producto       |Cantidad      |"
    separador =   "+---------------+--------------+"
    str_final = ""
    for item, valor in inventario.items():
        producto = item
        cantidad = str(valor.dar_cantidad())
        cantidad = cantidad + " " * (14 - len(cantidad))
        if len(producto) > 15:
            producto = producto[0:12] + "..."
        else:
            producto = producto + " " * (15 - len(producto))
        str_final += f"|{producto}|{cantidad}|\n{separador}\n"
    print(f"{separador}\n{str_inicial}\n{separador}\n{str_final}")

def leer_archivo_inventario(PATH_ARCHIVO_INVENTARIO):
    with open(PATH_ARCHIVO_INVENTARIO, "r") as inventario_persistente:
        linea_productos = inventario_persistente.read().splitlines() 
        diccionario_productos = {}
        diccionario_modificaciones = {}
        for lista in linea_productos:
            if lista[0] == "@":
                producto = lista.split("|")
                producto = Producto(producto[1], producto[2])
                nombre = producto.dar_nombre()
                diccionario_productos[nombre] = producto
                modificacion = Modificacion_producto(nombre)
                diccionario_modificaciones[nombre] = modificacion
            elif lista[0] == "#":
                lista_cantidad = lista.split("|")
                for item, valor in diccionario_modificaciones.items():
                    if lista_cantidad[1] == item:
                        valor.agregar_lista_cantidad(lista_cantidad[2:])
            elif lista[0] == "$":
                lista_fechas = lista.split("|")
                for item, valor in diccionario_modificaciones.items():
                    if lista_fechas[1] == item:
                        valor.agregar_lista_fechas(lista_fechas[2:])
            elif lista[0] == "%":
                lista_usuario = lista.split("|")
                for item, valor in diccionario_modificaciones.items():
                    if lista_usuario[1] == item:
                        valor.agregar_lista_usuarios(lista_usuario[2:])
        return diccionario_productos, diccionario_modificaciones

def leer_archivo_usuarios(PATH_ARCHIVO_USUARIOS):
    with open(PATH_ARCHIVO_USUARIOS, "r") as archivo_usuarios:
        usuarios = archivo_usuarios.read().splitlines()
        diccionario_usuarios = {}
        for usuario in usuarios:
            usuario = usuario.split("|")
            diccionario_usuarios[usuario[0]] = usuario[1]
    return diccionario_usuarios

PATH_ARCHIVO_USUARIOS = "archivo usuarios.txt"

if os.path.isfile(PATH_ARCHIVO_USUARIOS):
    diccionario_usuarios = leer_archivo_usuarios(PATH_ARCHIVO_USUARIOS)
else:
    diccionario_usuarios = {}

usuario_actual, diccionario_usuarios = crear_o_autenticar_usuario(diccionario_usuarios)

PATH_ARCHIVO_INVENTARIO = "archivo inventario.txt"

if os.path.isfile(PATH_ARCHIVO_INVENTARIO):
    diccionario_productos, diccionario_modificaciones = leer_archivo_inventario(PATH_ARCHIVO_INVENTARIO)
else:
    with open (PATH_ARCHIVO_INVENTARIO, "a") as inventario_persistente:
        diccionario_productos = {}
        diccionario_modificaciones = {}

comando = ingresar_comando()

while comando[0] != "terminar":
    fecha = datetime.today().strftime("%d-%m-%y %H:%M:%S")
    if comando[0] == "imprimir":
        imprimir_inventario(diccionario_productos)
        comando = ingresar_comando()
        continue
    elif comando[0] == "historia":
        historial = comando[1]
        for item, valor in diccionario_modificaciones.items():
            if historial  not in diccionario_modificaciones:
                print("El producto no existe.")
                comando = ingresar_comando()
                continue
            elif historial == item:
                valor.imprimir_historial()
                comando = ingresar_comando()
                continue

    elif comando[0] == "cambiar" and comando[1] == "usuario":
        usuario_actual, diccionario_usuarios = crear_o_autenticar_usuario(diccionario_usuarios)
        comando = ingresar_comando()
        continue

    else:
        if len(comando) != 3 :
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
            if "|" in producto:
                print("Este programa no acepta el uso de '|'")
            else:
                if producto not in diccionario_productos:
                    producto_nuevo = Producto(producto, cantidad)
                    modificaciones_nuevo = Modificacion_producto(producto)
                    modificaciones_nuevo.actualizar_historiales(fecha, cantidad, usuario_actual)
                    diccionario_productos[producto] = producto_nuevo
                    diccionario_modificaciones[producto] = modificaciones_nuevo
                else:
                    diccionario_productos[producto].agregar_cantidad(cantidad)
                    diccionario_modificaciones[producto].actualizar_historiales(fecha, cantidad, usuario_actual)

        elif accion == "quitar":
            if producto not in diccionario_productos:
                print(f"{producto} no se encuentra en el inventario")
            else:
                producto_actual = diccionario_productos[producto]
                cantidad_inicial = diccionario_productos[producto].dar_cantidad()
                if cantidad_inicial < cantidad:
                    print("Hay menos productos de los que queres quitar")
                else:
                    producto_actual.quitar_cantidad(cantidad)
                    modificacion_actual = diccionario_modificaciones[producto]
                    modificacion_actual.actualizar_historiales(fecha, cantidad * -1, usuario_actual)
        else:
            mostrar_comando_invalido()

        comando = ingresar_comando()

with open(PATH_ARCHIVO_INVENTARIO, "w") as archivo_productos:
    for item, valor in diccionario_productos.items():
        archivo_productos.write(valor.convertir_producto_a_string())
    for item, valor in diccionario_modificaciones.items():
        archivo_productos.write(valor.string_historial_cantidad())
        archivo_productos.write(valor.string_historial_fecha())
        archivo_productos.write(valor.string_historial_usuario())
with open(PATH_ARCHIVO_USUARIOS, "w") as archivo_usuarios:
    for item, valor in diccionario_usuarios.items():
        archivo_usuarios.write(f"{item}|{valor}\n")
