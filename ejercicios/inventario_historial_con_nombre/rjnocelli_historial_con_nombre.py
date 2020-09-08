import os
from datetime import datetime, date 

# PARTE 1: FUNCIONES Y OBJETOS -------------------------------------

def crear_archivo_de_texto(*args):
    archivos = {}
    
    for i in args:
        archivos[i] = i + '.txt'
        archivo = archivos[i]
        open(archivo, "a").close()
    
    return archivos

archivos = crear_archivo_de_texto('inventario','usuarios')

INVENTARIO_PATH = archivos['inventario']
USUARIOS_PATH = archivos['usuarios']

class Usuario():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

class Producto():
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.lista_de_modificaciones = []

class ModificacionDeProducto():
    def __init__(self, modificacion, tiempo, usuario):
        self.modificacion = modificacion
        self.tiempo = tiempo
        self.usuario = usuario

def imprimir_historial_de_producto(producto):
    total = producto.cantidad
    print(f'$ {producto.nombre}')
    for modificacion in reversed(producto.lista_de_modificaciones):
        print(f'Modificación: {modificacion.modificacion}, Nuevo valor: {total}, Fecha de modificacion: {modificacion.tiempo} ({modificacion.usuario})')
        mod = modificacion.modificacion.split()
        cantidad = int(mod[1])
        operacion = mod[0]
        if operacion == "+":
            total -= cantidad
        else:
            total += cantidad

def obtener_fecha_y_hora():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def persistir_inventario(path, inventario):
    with open(path, 'w') as f:
        for producto in inventario.values():
            f.write('@ ' + producto.nombre + ' ' + str(producto.cantidad) + ' \n')
            for mod in producto.lista_de_modificaciones:
                f.write('# ' + mod.modificacion + ' ' + mod.tiempo + ' ' + mod.usuario + ' \n')

def persistir_diccionario_de_usuarios(path, diccionario_de_usuarios):
    with open(path, 'w') as f:
        for usuario in diccionario_de_usuarios.values():
            f.write(f'{usuario.nombre} {usuario.contraseña}' + ' \n')
            
def leer_usuarios_de_archivo(path):
    diccionario_de_usuarios = {}

    with open(path,'r') as f:
        contenido = f.readlines()
        for datos in contenido:
            datos = datos.split()
            usuario = datos[0]
            contraseña = datos[1]
            usuario = Usuario(usuario, contraseña)
            if datos[0] == '#':
                mod = datos[1] + ' ' + datos[2]
                tiempo = datos[3] + ' ' + datos[4]
                modificador = datos[5]
                objeto_modificacion = ModificacionDeProducto(mod, tiempo, modificador)
                usuario.modificaciones.append(objeto_modificacion)
            diccionario_de_usuarios[usuario.nombre] = usuario
    return diccionario_de_usuarios

def leer_inventario_de_archivo(path):
    productos = {}

    with open(path, 'r') as f:
        contenido = f.readlines()
        
    for datos in contenido:
        datos = datos.split()
        if datos[0] == '@':
            nombre_de_producto = datos[1]
            cantidad = int(datos[2])
            producto = Producto(nombre_de_producto,cantidad)
            productos[producto.nombre] = producto
        if datos[0] == '#':
            mod = datos[1] + ' ' + datos[2]
            tiempo = datos[3] + ' ' + datos[4]
            modificador = datos[5]
            objeto_modificacion = ModificacionDeProducto(mod, tiempo, modificador)
            producto.lista_de_modificaciones.append(objeto_modificacion)

    return productos

def imprimir_inventario(inventario):
    inventario = inventario

    print('+---------------+--------------+')
    print('|Producto       |Cantidad      |')
    print('+---------------+--------------+')

    for producto in inventario.values():
        imprimir_producto(producto.nombre, producto.cantidad)

def imprimir_producto(nombre, cantidad):
    if len(nombre) > 15:
        print('|' + nombre[0:12] + "..." + '|' + str(cantidad)
              + (' ' * (14-len(str(cantidad)))) + '|' + '\n+---------------+--------------+')

    else:
        print('|' + nombre + (' '*(15-len(nombre))) + '|' + str(cantidad)
              + (' '*(14-len(str(cantidad)))) + '|' + '\n+---------------+--------------+')

def verificar_string_contiene_espacio(string):
    return " " in string

def cambiar_nombre_modificacion_de_producto(productos, nombre_actual, nuevo_nombre):
    for producto in productos.values():
        for modificacion in producto.lista_de_modificaciones:
            if modificacion.usuario == nombre_actual:
                modificacion.usuario = nuevo_nombre
    return productos
    
def cambiar_nombre_usuario():
    while True:
        nuevo_nombre = input("Ingrese nuevo nombre\n")
        if verificar_string_contiene_espacio(nuevo_nombre):
            print("El nombre no puede contener espacios")
        else:
            print(f"Nombre de Usuario cambiado a {nuevo_nombre}")
            return nuevo_nombre

def ejecutar_programa_inventario():

    inventario = leer_inventario_de_archivo(INVENTARIO_PATH)
    diccionario_de_usuarios = leer_usuarios_de_archivo(USUARIOS_PATH)
    usuario_autenticado = None
    terminar_loop_autenticar = False
    terminar_loop_programa = False


# PARTE 2: AUTENTICACION -------------------------------------

    while not terminar_loop_autenticar:
        usuario_respuesta = input("Desea 'AUTENTICAR' o 'CREAR' una cuenta de usuario? [typee 'SALIR' para terminar programa]\n").lower()
        if usuario_respuesta == 'crear':
                nombre_de_usuario = input("Por favor ingrese nombre de usuario (10 caracteres max)\n").lower()
                try:
                    if len(nombre_de_usuario) > 10:
                        raise ValueError
                    if verificar_string_contiene_espacio(nombre_de_usuario):
                        raise ValueError
                    if nombre_de_usuario in diccionario_de_usuarios:
                        raise ValueError
                except ValueError:
                    print("Usuario ya existente O cantidad de caracteres excede el maximo O nombre de usuario contiene espacios")     
                else:
                    contraseña = input("Por favor ingrese contraseña (10 caracteres max)\n").lower()
                    try:
                        if len(contraseña) > 10:
                            raise ValueError
                        if verificar_string_contiene_espacio(contraseña):
                            raise ValueError
                    except ValueError:
                        print("Caracteres de la contraseña excede el maximo o contraseña contiene espacios")
                    else:
                        confirmacion_de_contraseña = input("Confirme la contraseña\n").lower()
                        try:
                            if confirmacion_de_contraseña != contraseña:
                                raise ValueError
                        except ValueError:
                            print("Contraseñas no coinciden")
                        else:
                            nombre_de_usuario = Usuario(nombre_de_usuario, contraseña)
                            diccionario_de_usuarios[nombre_de_usuario.nombre] = nombre_de_usuario
                            usuario_autenticado = nombre_de_usuario.nombre
                            print(f'Usuario {nombre_de_usuario.nombre} creado')
                            terminar_loop_autenticar = True
        elif usuario_respuesta == 'autenticar':
                nombre_de_usuario = input('Ingrese su nombre de usuario\n').lower()
                contraseña = input('Ingrese su contraseña\n').lower()
                try:
                    if nombre_de_usuario not in diccionario_de_usuarios or diccionario_de_usuarios[nombre_de_usuario].contraseña != contraseña:
                        raise ValueError
                except ValueError:
                    print("Usuario y contraseña no coinciden")
                else:
                    print(f'{nombre_de_usuario}')
                    usuario_autenticado = nombre_de_usuario
                    terminar_loop_autenticar = True
        elif usuario_respuesta == 'salir':
            terminar_programa = True
            terminar_loop_programa = True
            break
        else:
            print("Ha ingresado un comando incorrecto")


# PARTE 3: INVENTARIO -------------------------------------


    while not terminar_loop_programa:

        print(f'Usuario Autenticado: {usuario_autenticado}')

        comando = input('''\n\t\tPor favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR
                formato [accion-elemento-cantidad] ejemplo: agregar manzana 3\n
                typee IMPRIMIR para ver el inventario
                typee SALIR para terminar
                typee HISTORIA 'nombre_del_producto' para ver el historial del producto\n
                typee CAMBIAR NOMBRE para modificar tu nombre de usuario\n''').lower() 
        
        if comando == 'cambiar nombre':
            nuevo_nombre = cambiar_nombre_usuario()
            inventario = cambiar_nombre_modificacion_de_producto(inventario, usuario_autenticado, nuevo_nombre)
            diccionario_de_usuarios[usuario_autenticado].nombre = nuevo_nombre 
            diccionario_de_usuarios[nuevo_nombre] = diccionario_de_usuarios.pop(usuario_autenticado)
            usuario_autenticado = diccionario_de_usuarios[nuevo_nombre].nombre
        elif comando == 'imprimir':
            os.system('clear')
            imprimir_inventario(inventario)
        elif comando == 'salir':
            persistir_inventario(INVENTARIO_PATH, inventario)
            persistir_diccionario_de_usuarios(USUARIOS_PATH,diccionario_de_usuarios)
            print('Fin del programa.')
            break
        elif len(comando.split()) == 2 and comando.split()[0] == 'historia':
            comando = comando.split()
            try:
                imprimir_historial_de_producto(inventario[comando[1]])
            except KeyError:
                print('Producto no existe en inventario')
        elif len(comando.split()) == 3:
            comando = comando.split()
            try:
                comando[2] = int(comando[2])
                if comando[2] < 0:
                    raise ValueError
            except ValueError:
                print('Cantidad debe ser en formato numerico positivo.')
            else:
                accion = comando[0]
                elemento = comando[1]
                cantidad = comando[2]
                if accion == 'agregar':
                    if elemento not in inventario:
                        os.system('clear')
                        elemento = Producto(elemento,cantidad)
                        objeto_modificacion = ModificacionDeProducto(f'+ {cantidad}',obtener_fecha_y_hora(), usuario_autenticado)
                        elemento.lista_de_modificaciones.append(objeto_modificacion)
                        inventario[elemento.nombre] = elemento
                        print(f'NUEVO PRODUCTO {elemento.nombre} AGREGADO\n')
                    else:   
                        inventario[elemento].cantidad += cantidad
                        objeto_modificacion = ModificacionDeProducto(f'+ {cantidad}',obtener_fecha_y_hora(), usuario_autenticado)
                        inventario[elemento].lista_de_modificaciones.append(objeto_modificacion)
                elif accion == 'quitar':
                    if elemento not in inventario:
                        print(
                            'No tienes nigun producto con ese nombre en tu inventario.')
                    elif inventario[elemento].cantidad < cantidad:
                        print(
                            'La cantidad de ese producto en tu inventario es menor a la solicitada.')
                    else:
                        inventario[elemento].cantidad -= cantidad
                        objeto_modificacion = ModificacionDeProducto(f'- {cantidad}',obtener_fecha_y_hora(), usuario_autenticado)
                        inventario[elemento].lista_de_modificaciones.append(objeto_modificacion)
                else:
                     print(
                        'Has ingresado un comando incorrecto, por favor intenta de nuevo.')
        else:
            print(
                'Has ingresado un comando incorrecto, por favor intenta de nuevo.')

ejecutar_programa_inventario()
