from src.gestorAplicacion.administracion.Cocinero import *
from src.gestorAplicacion.administracion.Mesero import *

cocinero = Cocinero("David", 100, 50000, "Calvas")
print(cocinero.getOcupacion())
mesero = Mesero("Camilo", 100, 2000)
print(mesero.accion())
