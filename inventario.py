import os

inventario = {}

def imprimir_inventario(inventario):
    os.system('clear')
    print('+---------------+--------------+')
    print('|Producto       |Cantidad      |')
    print('+---------------+--------------+')
    for i in inventario:
        if len(i) > 15:
            print('|' + i[0:12] + "..." +"|" + str(inventario[i]) +(' '*(14-len(str(inventario[i]))) + '|'))
            print('+---------------+--------------+')
        else:
            print('|' + i + (' '*(15-len(i)) + "|" + str(inventario[i]) + (' '*(14-len(str(inventario[i])))+ '|')))
            print('+---------------+--------------+')


while True:
    comando = input(str("Por favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR en formato [accion-elemento-cantidad]\ntypee IMPRIMIR para ver el inventario\ntypee SALIR para terminar\n"))

    if comando.lower() == 'imprimir':
        imprimir_inventario(inventario)
        
    elif comando.lower() == 'salir':
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
                else:
                    inventario[elemento] += cantidad
                    os.system('clear')
            elif accion.lower() == 'quitar':
                if elemento not in inventario:
                    os.system('clear')
                    print('No tienes nigun producto con ese nombre en tu inventario.')
                else:
                    if inventario[elemento] < cantidad:
                        os.system('clear')
                        print('La cantidad de ese producto en tu inventario es menor a la solicitada.')
                    else:
                        inventario[elemento] -= cantidad
            else:
                print('Has ingresado un comando incorrecto, por favor intenta de nuevo.')
