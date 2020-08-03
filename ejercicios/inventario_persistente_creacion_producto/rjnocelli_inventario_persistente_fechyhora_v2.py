import os
from datetime import datetime, date 

ARCHIVO_PATH = "inventario.txt"
open(ARCHIVO_PATH, "a").close()

class Producto():

    def __init__(self,nombre,cantidad,fecha):
        self.nombre = nombre
        self.cantidad = cantidad
        self.fecha_de_creacion = fecha
    
    def __str__(self):
        return self.nombre 
    
def calcular_fecha_y_hora():
    hora_ahora = datetime.now().strftime("%H:%M")
    fecha_ahora = date.today()
    elemento = f'{fecha_ahora} {hora_ahora}'
    return elemento

def persistir_inventario(path, inventario):
    with open(path, 'w') as f:
        f.truncate(0)
        for producto in inventario.values():
            f.write(producto.nombre + ' ' + str(producto.cantidad) + ' ' + str(producto.fecha_de_creacion) + ' \n')

def crear_o_actualizar_inventario(path):

    inventario = {}

    with open(path, 'r') as f:
        contenido = f.read()
        contenido = contenido.split()

    for elemento in range(0, len(contenido), 4):
        elemento = Producto(contenido[elemento],int(contenido[+1]),f'{contenido[+2]} {contenido[+3]}')
        inventario[elemento.nombre] = elemento

    return inventario

def imprimir_inventario(inventario):

    inventario = inventario

    print('+---------------+--------------+----------------+')
    print('|Producto       |Cantidad      |Agregado el:    |')
    print('+---------------+--------------+----------------+')

    for producto in inventario.values():
        imprimir_producto(producto.nombre, producto.cantidad, producto.fecha_de_creacion)

def imprimir_producto(nombre, cantidad, fecha_de_creacion):
    if len(nombre) > 15:
        print('|' + nombre[0:12] + "..." + '|' + str(cantidad)
              + (' ' * (14-len(str(cantidad)))) + '|' + fecha_de_creacion + '|' + '\n+---------------+--------------+----------------+')

    else:
        print('|' + nombre + (' '*(15-len(nombre))) + '|' + str(cantidad)
              + (' '*(14-len(str(cantidad)))) + '|' + fecha_de_creacion + '|' + '\n+---------------+--------------+----------------+')


def ejecutar_programa_inventario():

    inventario = crear_o_actualizar_inventario(ARCHIVO_PATH)

    while True:
        comando = input(
            "Por favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR \n formato [accion-elemento-cantidad] ejemplo: agregar manzana 3\
            \n typee IMPRIMIR para ver el inventario\n typee SALIR para terminar\n")
        if comando.lower() == 'imprimir':
            os.system('clear')
            imprimir_inventario(inventario)
        elif comando.lower() == 'salir':
            persistir_inventario(ARCHIVO_PATH, inventario)
            print('Fin del programa.')
            break
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
                accion = comando[0].lower()
                elemento = comando[1].lower()
                cantidad = comando[2]
                if accion.lower() == 'agregar':
                    if elemento not in inventario:
                        os.system('clear')
                        elemento = Producto(elemento,cantidad,calcular_fecha_y_hora())
                        inventario[elemento.nombre] = elemento
                        print(f'NUEVO PRODUCTO {elemento.nombre} AGREGADO\n')
                    else:   
                        inventario[elemento.nombre].cantidad += cantidad
                        os.system('clear')
                elif accion.lower() == 'quitar':
                    if elemento not in inventario:
                        os.system('clear')
                        print(
                            'No tienes nigun producto con ese nombre en tu inventario.')
                    else:
                        if inventario[elemento.nombre].cantidad < cantidad:
                            os.system('clear')
                            print(
                                'La cantidad de ese producto en tu inventario es menor a la solicitada.')
                        else:
                            inventario[elemento.nombre].cantidad -= cantidad
                else:
                    print(
                        'Has ingresado un comando incorrecto, por favor intenta de nuevo.')


ejecutar_programa_inventario()
