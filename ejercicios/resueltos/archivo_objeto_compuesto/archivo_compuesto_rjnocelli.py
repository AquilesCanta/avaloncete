import os


def pregunta():
    while True:
        nombre = input('Hola, quien sos?\n')
        if nombre.isalpha():
            break
        else:
            os.system('clear')
            print(
                'Nombre debe ser un string')
    while True:
        edad = input('Que edad tenes?\n')
        try:
            type(int(edad)) != int
        except ValueError:
            os.system('clear')
            print('Edad debe ser un numero.\n')
        else:
            os.system('clear')
            print(
                f'Hola, {nombre} de {edad}. La proxima vez me acordare de vos\n')
            with open('archivo2.txt', 'w') as f:
                f.write(f'{nombre} {edad}')
                # variable frenar_loop pertenece a rama 'soy yo' del if statement
                global frenar_loop
                frenar_loop = False
                return frenar_loop


def te_conozco(nombre, edad):
    os.system('clear')
    with open('archivo2.txt', 'r') as f:
        global frenar_loop
        frenar_loop = True
    while frenar_loop:
        respuesta = input(
            f'Hola {nombre} de {edad}. O sos otra persona? [comandos: "soy yo" - "soy otra persona"]\n')
        if respuesta.lower() == 'soy otra persona':
            pregunta()
        elif respuesta.lower() == 'soy yo':
            os.system('clear')
            print(f'Hola de nuevo, {nombre} de {edad}!')
            frenar_loop = False
            break
        else:
            os.system('clear')
            print('Has ingresado un comando incorrecto')


def no_te_conozco():
    pregunta()


def correr_programa():
    with open('archivo2.txt', 'r') as f:
        archivos = f.read().split()
    if archivos:
        nombre_guardado = archivos[0]
        edad_guardada = archivos[1]
        te_conozco(nombre_guardado, edad_guardada)
    else:
        no_te_conozco()


correr_programa()
