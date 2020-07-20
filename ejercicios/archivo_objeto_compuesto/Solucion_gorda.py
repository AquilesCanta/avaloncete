from io import open
import os #para windows, no se si es igual en otros sistemas operativos

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def convertir_a_string(self):
        return f"{self.__nombre} de {self.__edad}"

    def ingresar_al_fichero(self):
        with open (PATH_ARCHIVO_EXTERNO, "w") as fichero_externo:
            fichero_externo.write(self.convertir_a_string())

    def imprimir_saludo(self):
        print(f"Hola {self.convertir_a_string()}! La proxima vez sabré tu nombre")


    

def solicitar_nombre():
    return input("No te conozco, quien sos?: ")

def solicitar_edad():
    return input("Cuantos años tenés?: ")

def revisar_nombre():
    return input("Ingresa 'soy yo' o 'soy otra persona': ")

def leer_archivo():
    with open(PATH_ARCHIVO_EXTERNO, "r") as fichero_externo:
        return fichero_externo.read()
    
    
PATH_ARCHIVO_EXTERNO = "Fichero_de_nombres.txt"

if os.path.isfile(PATH_ARCHIVO_EXTERNO):
        lista_del_nombre = leer_archivo().split()
else:
    with open(PATH_ARCHIVO_EXTERNO, "a") as fichero_externo:
        lista_del_nombre = leer_archivo().split()

reconocimiento = "Nada"

if len(lista_del_nombre) == 0:
    nombre = solicitar_nombre()
    edad = str(solicitar_edad())
    usuario = Persona(nombre, edad)
    usuario.imprimir_saludo()
    usuario.ingresar_al_fichero()
else:
    usuario = Persona(lista_del_nombre[0], lista_del_nombre[2])
    nombre_completo = usuario.convertir_a_string()
    print(f"Hola {nombre_completo}! O sos otra persona?")
    while reconocimiento.lower() != "soy yo" and reconocimiento.lower() != "soy otra persona":
        reconocimiento = revisar_nombre() 
        if reconocimiento.lower() == "soy yo":
            print(f"Hola de nuevo, {nombre_completo}")
        elif reconocimiento.lower() == "soy otra persona":
            nombre = solicitar_nombre()
            edad = str(solicitar_edad())
            usuario = Persona(nombre, edad)
            usuario.imprimir_saludo()
            usuario.ingresar_al_fichero()
        else:
            print("No entiendo! Entiendo 'soy yo' o 'soy otra persona'")
