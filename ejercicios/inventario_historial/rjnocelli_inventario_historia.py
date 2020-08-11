import os
from datetime import datetime, date 

ARCHIVO_PATH = "inventario.txt"
open(ARCHIVO_PATH, "a").close()

class Producto():
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.lista_de_modificaciones = []
    
    def __str__(self):
        return self.nombre 

class ModificacionDeProducto():
    def __init__(self,modificacion,tiempo):
        self.modificacion = modificacion
        self.tiempo = tiempo

def imprimir_historial_de_producto(producto):
    total = producto.cantidad
    print(f'$ {producto.nombre}')
    for objeto_modificacion in range(len(producto.lista_de_modificaciones)-1,-1,-1):
        objeto = producto.lista_de_modificaciones[objeto_modificacion]
        mod = objeto.modificacion.split()
        print(f'Modificación: {objeto.modificacion}, Nuevo valor: {total}, Fecha de modificacion: {objeto.tiempo}')
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
                f.write('# ' + mod.modificacion + ' ' + mod.tiempo + ' \n')

def crear_o_actualizar_inventario(path):
    inventario = {}

    with open(path, 'r') as f:
        contenido = f.readlines()
        
    for datos in contenido:
        datos = datos.split()
        if datos[0] == '@':
            nombre_de_producto = datos[1]
            cantidad = int(datos[2])
            producto = Producto(nombre_de_producto,cantidad)
            inventario[producto.nombre] = producto
        if datos[0] == '#':
            mod = datos[1] + ' ' + datos[2]
            tiempo = datos[3] + ' ' + datos[4]
            objeto_modificacion = ModificacionDeProducto(mod,tiempo)
            producto.lista_de_modificaciones.append(objeto_modificacion)

    return inventario

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

def ejecutar_programa_inventario():

    inventario = crear_o_actualizar_inventario(ARCHIVO_PATH)

    while True:
        comando = input('''\n\t\tPor favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR
                formato [accion-elemento-cantidad] ejemplo: agregar manzana 3\n
                typee IMPRIMIR para ver el inventario
                typee SALIR para terminar
                typee HISTORIA 'nombre_del_producto' para ver el historial del producto\n''').lower() 
            
        if comando == 'imprimir':
            os.system('clear')
            imprimir_inventario(inventario)
        elif comando == 'salir':
            persistir_inventario(ARCHIVO_PATH, inventario)
            print('Fin del programa.')
            break
        elif len(comando.split()) == 2 and comando.split()[0] == 'historia':
            comando = comando.split()
            try:
                imprimir_historial_de_producto(inventario[comando[1]])
            except KeyError:
                print('Producto no existe en inventario')
        elif len(comando.split()) < 3:
            print('Por favor ingresar comandos correctos.')
        else:
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
                        objeto_modificacion = ModificacionDeProducto(f'+ {cantidad}',obtener_fecha_y_hora())
                        elemento.lista_de_modificaciones.append(objeto_modificacion)
                        inventario[elemento.nombre] = elemento
                        print(f'NUEVO PRODUCTO {elemento.nombre} AGREGADO\n')
                    else:   
                        inventario[elemento].cantidad += cantidad
                        objeto_modificacion = ModificacionDeProducto(f'+ {cantidad}',obtener_fecha_y_hora())
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
                        objeto_modificacion = ModificacionDeProducto(f'- {cantidad}',obtener_fecha_y_hora())
                        inventario[elemento].lista_de_modificaciones.append(objeto_modificacion)
                else:
                     print(
                        'Has ingresado un comando incorrecto, por favor intenta de nuevo.')


ejecutar_programa_inventario()
