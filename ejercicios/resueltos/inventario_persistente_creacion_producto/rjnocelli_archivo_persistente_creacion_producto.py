import os
from datetime import datetime, date 

ARCHIVO_PATH = "inventario.txt"
open(ARCHIVO_PATH, "a").close()

def calcular_fecha_y_hora():
    hora_ahora = datetime.now().strftime("%H:%M")
    fecha_ahora = date.today()
    elemento = f'{fecha_ahora} {hora_ahora}'
    return elemento

#fyh = fecha y hora
def crear_objeto_fyh(elemento):
    fecha_y_hora = f'{elemento}_fyh'
    return fecha_y_hora

def persistir_inventario(path, inventario,fyh):
    with open(path, 'w') as f:
        f.truncate(0)
        for producto, cantidad in inventario.items():
            f.write(producto + ' ' + str(cantidad) + ' ' + fyh[crear_objeto_fyh(producto)] + ' \n')

def crear_o_actualizar_inventario(path):

    inventario = {}
    elemento_fyh = {}

    lista_de_diccionarios = [inventario,elemento_fyh]
    
    with open(path, 'r') as f:
        contenido = f.read()
        contenido = contenido.split()

    for elemento in range(0, len(contenido), 4):
        inventario[contenido[elemento]] = int(contenido[elemento+1])
        elemento_fyh[crear_objeto_fyh(contenido[elemento])] = f'{contenido[elemento+2]} {contenido[elemento+3]}'

    return lista_de_diccionarios


def imprimir_inventario(inventario,fyh):

    inventario = inventario

    print('+---------------+--------------+----------------+')
    print('|Producto       |Cantidad      |Agregado el:    |')
    print('+---------------+--------------+----------------+')

    for producto in inventario:
        imprimir_producto(producto, inventario[producto], fyh)


def imprimir_producto(nombre, cantidad, fyh):
    if len(nombre) > 15:
        print('|' + nombre[0:12] + "..." + '|' + str(cantidad)
              + (' ' * (14-len(str(cantidad)))) + '|' + fyh[crear_objeto_fyh(nombre)] + '|' + '\n+---------------+--------------+----------------+')

    else:
        print('|' + nombre + (' '*(15-len(nombre))) + '|' + str(cantidad)
              + (' '*(14-len(str(cantidad)))) + '|' + fyh[crear_objeto_fyh(nombre)] + '|' + '\n+---------------+--------------+----------------+')


def ejecutar_programa_inventario():

    inventario = crear_o_actualizar_inventario(ARCHIVO_PATH)[0]
    elemento_fyh = crear_o_actualizar_inventario(ARCHIVO_PATH)[1]

    while True:
        comando = input(
            "Por favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR \n formato [accion-elemento-cantidad] ejemplo: agregar manzana 3\
            \n typee IMPRIMIR para ver el inventario\n typee SALIR para terminar\n")
        if comando.lower() == 'imprimir':
            os.system('clear')
            imprimir_inventario(inventario,elemento_fyh)
        elif comando.lower() == 'salir':
            persistir_inventario(ARCHIVO_PATH, inventario, elemento_fyh)
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
                        inventario[elemento] = cantidad
                        elemento_fyh[crear_objeto_fyh(elemento)] = calcular_fecha_y_hora()
                        print(f'NUEVO PRODUCTO {elemento} AGREGADO\n')
                    else:   
                        inventario[elemento] += cantidad
                        os.system('clear')
                elif accion.lower() == 'quitar':
                    if elemento not in inventario:
                        os.system('clear')
                        print(
                            'No tienes nigun producto con ese nombre en tu inventario.')
                    else:
                        if inventario[elemento] < cantidad:
                            os.system('clear')
                            print(
                                'La cantidad de ese producto en tu inventario es menor a la solicitada.')
                        else:
                            inventario[elemento] -= cantidad
                else:
                    print(
                        'Has ingresado un comando incorrecto, por favor intenta de nuevo.')


ejecutar_programa_inventario()
