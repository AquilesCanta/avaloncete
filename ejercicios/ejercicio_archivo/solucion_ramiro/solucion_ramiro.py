import os

with open('archivos.txt','r') as f:
    if f.read():
        f.seek(0)
        os.system('clear')
        pregunta = input(str('Hola ' + str(f.read()) + '!' + ' O sos otra persona? (Ingresa: "Soy yo" o "Soy otra persona")\n'))
        if pregunta.lower() == 'soy otra persona':
                os.system('clear')
                nombre = input(str('Como te llamas?\n'))
                print(f'Hola {nombre}!, la proxima sabre tu nombre.')
                with open('archivos.txt','w') as f:
                    f.seek(0)
                    f.write(str(nombre))
        elif pregunta.lower() == 'soy yo':
            f.seek(0)
            print('Hola de nuevo, ' + f.read() + '!')
        else:
            while True:
                os.system('clear')
                pregunta = input(str('No entendi! Entiendo "Soy yo" o "Soy otra persona"\n'))
                if pregunta.lower() == 'soy yo':
                    f.seek(0)
                    os.system('clear')
                    print('Hola de nuevo, ' + f.read() + '!')
                    break
                elif pregunta.lower() == 'soy otra persona':
                    nombre = input(str('Como te llamas?\n'))
                    print(f'Hola {nombre}!, la proxima sabre tu nombre.')
                    with open('archivos.txt','w') as f:
                        f.seek(0)
                        f.write(str(nombre))
                    break
    else:
        with open('archivos.txt','w') as f:
            os.system('clear')
            nombre = input(str('No te conozco, quien sos?\n'))
            f.write(str(nombre))
            print(f'Hola {nombre}!, la proxima sabre tu nombre.')
