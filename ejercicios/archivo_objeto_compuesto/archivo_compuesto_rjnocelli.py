import os


def te_conozco(nombre, edad):
    os.system('clear')
    with open('archivo2.txt', 'r') as f:
        frenar_loop = True
    while frenar_loop:
        os.system('clear')
        respuesta = input(
            f'Hola {nombre} de {edad}. O sos otra persona? [comandos: "soy yo" - "soy otra persona"]\n')
        if respuesta.lower() == 'soy otra persona':
            while True:
                nombre = input('Quien sos?\n')
                if nombre.isalpha():
                    break
                else:
                    print(
                        'Nombre debe ser un string')
            while True:
                edad = input('Que edad tenes?\n')
                try:
                    type(int(edad)) != int
                except ValueError:
                    print('Edad debe ser un numero.\n')
                else:
                    os.system('clear')
                    print(
                        f'Hola, {nombre} de {edad}. La proxima vez me acordare de vos\n')
                    with open('archivo2.txt', 'w') as f:
                        f.write(f'{nombre} {edad}')
                        frenar_loop = False
                        break
        elif respuesta.lower() == 'soy yo':
            os.system('clear')
            print(f'Hola de nuevo, {nombre} de {edad}!')
            break
        else:
            print('Has ingresado un comando incorrecto')


def no_te_conozco():
    while True:
        os.system('clear')
        nombre = input('Hola, quien sos?\n')
        if nombre.isalpha():
            break
        else:
            print(
                'Nombre debe ser un string')
    while True:
        edad = input('Que edad tenes?\n')
        try:
            type(int(edad)) != int
        except ValueError:
            print('Edad debe ser un numero.\n')
        else:
            os.system('clear')
            print(
                f'Hola, {nombre} de {edad}. La proxima vez me acordare de vos\n')
            with open('archivo2.txt', 'w') as f:
                f.write(f'{nombre} {edad}')
                frenar_loop = False
                break


with open('archivo2.txt', 'r') as f:
    archivos = f.read().split()
    if archivos:
        nombre_guardado = archivos[0]
        edad_guardada = archivos[1]
        te_conozco(nombre_guardado, edad_guardada)
    else:
        no_te_conozco()
