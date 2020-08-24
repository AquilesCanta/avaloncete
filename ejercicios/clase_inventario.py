import datetime

ARCHIVO_INVENTARIO = "inventario.txt"

ACCION_TERMINAR = "terminar"
ACCION_AGREGAR = "agregar"
ACCION_QUITAR = "quitar"
ACCION_IMPRIMIR = "imprimir"
ACCION_HISTORIA = "historia"

SEPARADOR = "|"

class ModificacionDeProducto:
  def __init__(self, cantidad, marca_de_tiempo):
    self.__cantidad = cantidad
    self.__marca_de_tiempo = marca_de_tiempo

  def cantidad(self):
    return self.__cantidad

  def marca_de_tiempo(self):
    return self.__marca_de_tiempo

class Producto:

  def __init__(self, nombre, cantidad=0, modificaciones=None):
    self.__nombre = nombre
    self.__cantidad = cantidad
    self.__modificaciones = modificaciones if modificaciones is not None else []

  def modificar_cantidad(self, cantidad):
    """
    Modifica la cantidad del producto sumando la cantidad provista.
    Devuelve verdadero si la modificación se realizó con éxito.
    """
    if self.__cantidad + cantidad < 0:
      return False
    self.__modificaciones.append(
        ModificacionDeProducto(cantidad, datetime.datetime.now()))
    self.__cantidad += cantidad
    return True

  def cantidad(self):
    return self.__cantidad

  def nombre(self):
    return self.__nombre

  def modificaciones(self):
    return tuple(self.__modificaciones)

def modificar_inventario(comando, inventario):
  if comando[0] not in (ACCION_AGREGAR, ACCION_QUITAR):
    return False
  if len(comando) != 3:
    print("Sintaxis invalida: " + str(comando))
    return True
  accion = comando[0]
  nombre_producto = comando[1]
  cantidad = int(comando[2])
  if cantidad < 0:
    print("Error: cantidad negativa.")
    return True
  if accion == ACCION_QUITAR:
    cantidad *= -1
  if not nombre_producto in inventario:
    inventario[nombre_producto] = Producto(nombre_producto)
  producto = inventario[nombre_producto]
  if producto.modificar_cantidad(cantidad):
    print(f"La nueva cantidad de {producto.nombre()} "
          f"es {producto.cantidad()}")
  else:
    print(f"Modificación inválida. Cantidad actual: {producto.cantidad()}.")
  return True

def imprimir_inventario(comando: list, inventario: dict) -> bool:
  if comando[0] != ACCION_IMPRIMIR:
    return False
  print("\ninventario")
  print("==========")
  for k, v in inventario.items():
    print(f"{k}: {v.cantidad()}")
  print()
  return True

def imprimir_historia(comando, inventario):
  if comando[0] != ACCION_HISTORIA:
    return False
  nombre_producto = comando[1]
  if nombre_producto not in inventario:
    print(f"El producto {nombre_producto} no existe.")
    return True
  producto = inventario[nombre_producto]
  cantidad = producto.cantidad()
  modificaciones = reversed(producto.modificaciones())
  for modificacion in modificaciones:
    signo = "+" if modificacion.cantidad() > 0 else "-"
    print(f"Cantidad: {signo}{modificacion.cantidad()},"
          f" Nuevo: {cantidad} | {modificacion.marca_de_tiempo()}")
    cantidad += modificacion.cantidad()

def leer_inventario(nombre_de_archivo):
  open(nombre_de_archivo, "a").close()
  inventario = {}
  with open(nombre_de_archivo, "r") as archivo:
    for s in archivo.read().splitlines():
      elementos = s.split(SEPARADOR)
      inventario[elementos[0]] = Producto(elementos[0], int(elementos[1]))
  return inventario

def escribir_inventario(inventario, nombre_de_archivo):
  with open(nombre_de_archivo, "w") as archivo:
    for producto in inventario.values():
      archivo.write(f"{producto.nombre()}{SEPARADOR}{producto.cantidad()}\n")

def main(inventario):
  manejadores_de_comando = [
      modificar_inventario,
      imprimir_inventario,
      imprimir_historia
    ]
  while True:
    comando = input("Ingrese un comando (terminar, agregar, quitar, historia)\n").split()
    accion = comando[0]
    if accion == ACCION_TERMINAR:
      break
    manejado = False
    for manejador in manejadores_de_comando:
      manejado = manejador(comando, inventario)
      if manejado:
        break
    if not manejado:
      print(f"Comando inválido: {accion}.")

inventario = leer_inventario(ARCHIVO_INVENTARIO)
try:
  main(inventario)
except Exception as e:
  print(e)
escribir_inventario(inventario, ARCHIVO_INVENTARIO)
