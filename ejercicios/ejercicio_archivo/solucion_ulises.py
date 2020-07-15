from io import open
import os #para windows, no se si es igual en otros sistemas operativos

def imprimir_saludo(nombre):
    print(f"Hola {nombre.capitalize()}! La proxima vez sabré tu nombre")

def imprimir_nombre():
    nombre = input("No te conozco, quien sos?: ")
    return nombre

def revisar_nombre():
    reconocimiento = input("Ingresa 'soy yo' o 'soy otra persona': ")
    return reconocimiento

def leer_archivo():
    fichero_externo = open("Fichero_de_nombres.txt", "r")
    lista_de_nombres = fichero_externo.readlines()
    fichero_externo.close()
    return lista_de_nombres
    
path = "C:Users\\usuario\\Fichero_de_nombres.txt"

if os.path.isfile(path):
    lista_de_nombres = leer_archivo()
else:
    fichero_externo = open("Fichero_de_nombres.txt", "a")
    fichero_externo.close()
    lista_de_nombres = leer_archivo()

reconocimiento = "Nada"

if len(lista_de_nombres) == 0:
    with open ("Fichero_de_nombres.txt", "w") as fichero_externo:
        nombre = imprimir_nombre()
        imprimir_saludo(nombre)
        fichero_externo.write(f"{nombre.lower()}")
else:
    nombre = lista_de_nombres[-1]
    print(f"Hola {nombre}! O sos otra persona?")
    while reconocimiento.lower() != "soy yo" and reconocimiento.lower() != "soy otra persona":
        reconocimiento = revisar_nombre() 
        if reconocimiento.lower() == "soy yo":
            print(f"Hola de nuevo, {nombre.capitalize()}")
        elif reconocimiento.lower() == "soy otra persona":
            with open ("Fichero_de_nombres.txt", "w") as fichero_externo:
                nombre = imprimir_nombre()
                imprimir_saludo(nombre)
                fichero_externo.write(f"{nombre.lower()}")
        else:
            print("No entiendo! Entiendo 'soy yo' o 'soy otra persona'")
            reconocimiento = "Nada"


