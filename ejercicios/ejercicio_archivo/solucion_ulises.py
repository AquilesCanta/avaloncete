from io import open
import os #para windows, no se si es igual en otros sistemas operativos

def imprimir_saludo(nombre):
    print(f"Hola {nombre.capitalize()}! La proxima vez sabré tu nombre")

def solicitar_nombre():
    return input("No te conozco, quien sos?: ")

def revisar_nombre():
    return  input("Ingresa 'soy yo' o 'soy otra persona': ")

def leer_archivo():
    with open (PATH_ARCHIVO_NOMBRE, "r") as fichero_externo:
        lista_de_nombres = fichero_externo.readlines()
    return lista_de_nombres
    
PATH_ARCHIVO_NOMBRE = "Fichero_de_nombres.txt"

if os.path.isfile(PATH_ARCHIVO_NOMBRE):
    lista_de_nombres = leer_archivo()
else:
    with open (PATH_ARCHIVO_NOMBRE, "a") as fichero_externo:
        lista_de_nombres = leer_archivo()

reconocimiento = "Nada"

if len(lista_de_nombres) == 0:
    with open ("Fichero_de_nombres.txt", "w") as fichero_externo:
        nombre = solicitar_nombre()
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
                nombre = solicitar_nombre()
                imprimir_saludo(nombre)
                fichero_externo.write(f"{nombre.lower()}")
        else:
            print("No entiendo! Entiendo 'soy yo' o 'soy otra persona'")