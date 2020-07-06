import os

inventario = {}

while True:
    comando = input(str("Por favor typee que accion desea realizar en el inventario: AGREGAR / QUITAR en formato [accion-elemento-cantidad]\n typee SALIR para terminar:\n"))

    if comando.lower() == 'salir':
        print("INVENTARIO")
        print("-----------")
        for i in inventario:
            print(i + ": " + str(inventario[i]))
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
                    inventario[elemento] = cantidad
                    os.system('clear')
                    print(f'NUEVO PRODUCTO {elemento} AGREGADO')
                else:
                    inventario[elemento] += cantidad
                    os.system('clear')
            elif accion.lower() == 'quitar':
                if elemento not in inventario:
                    print('No tienes nigun producto con ese nombre en tu inventario.')
                else:
                    if inventario[elemento] < cantidad:
                        print('La cantidad de ese producto en tu inventario es menor a la solicitada.')
                    else:
                        inventario[elemento] -= cantidad
            else:
                print('Has ingresado un comando incorrecto, por favor intenta de nuevo.')
