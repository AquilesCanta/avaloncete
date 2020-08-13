import os

if os.path.exists('inventario.txt'):
    ARCHIVO_PATH = 'inventario.txt'
else:
    with open('inventario.txt', 'w+'):
        ARCHIVO_PATH = 'inventario.txt'


def agregar_inventario_a_archivo(path, nombre_de_inventario):
    with open(path, 'r+') as f:
        f.read()
        for producto in nombre_de_inventario:
            f.write(producto + ' ' + str(nombre_de_inventario[producto]) + ' ')


def crear_o_actualizar_inventario(path):

    inventario = {}

    with open(path, 'r') as f:
        content = f.read()
        content = content.split()

    for item in range(0, len(content), 2):
        inventario[content[item]] = int(content[item+1])

    return inventario


def imprimir_inventario(path):

    inventario = crear_o_actualizar_inventario(path)

    print('+---------------+--------------+')
    print('|Producto       |Cantidad      |')
    print('+---------------+--------------+')

    for producto in inventario:
        imprimir_producto(producto, inventario[producto])


def imprimir_producto(nombre, cantidad):
    if len(nombre) > 15:
        print('|' + nombre[0:12] + "..." + "|" + str(cantidad)
              + (' ' * (14-len(str(cantidad)))) + '|' + '\n+---------------+--------------+')

    else:
        print('|' + nombre + (' '*(15-len(nombre))) + "|" + str(cantidad)
              + (' '*(14-len(str(cantidad)))) + '|' + '\n+---------------+--------------+')


def ejecutar_programa_inventario():

    inventario = crear_o_actualizar_inventario(ARCHIVO_PATH)

    while True:
        comando = input(
            "Por favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR \n formato [accion-elemento-cantidad] ejemplo: agregar manzana 3\
            \n typee IMPRIMIR para ver el inventario\n typee SALIR para terminar\n")
        if comando.lower() == 'imprimir':
            os.system('clear')
            imprimir_inventario(ARCHIVO_PATH)
        elif comando.lower() == 'salir':
            os.system('clear')
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
                        print(f'NUEVO PRODUCTO {elemento} AGREGADO\n')
                        agregar_inventario_a_archivo(ARCHIVO_PATH, inventario)
                    else:
                        inventario[elemento] += cantidad
                        os.system('clear')
                        agregar_inventario_a_archivo(ARCHIVO_PATH, inventario)
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
                            agregar_inventario_a_archivo(
                                ARCHIVO_PATH, inventario)
                else:
                    print(
                        'Has ingresado un comando incorrecto, por favor intenta de nuevo.')


ejecutar_programa_inventario()
