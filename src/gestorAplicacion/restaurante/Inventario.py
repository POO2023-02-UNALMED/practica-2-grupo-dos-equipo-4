from abc import ABC, abstractmethod

class Inventario(ABC):

    listaInventario = []

    def __init__(self, nombre=None, precio=None, cantidad=None):
        if nombre is not None and precio is not None and cantidad is not None:
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            Inventario.listaInventario.append(self)
        self.disponibilidad = False

    @abstractmethod
    def comprar(self, cantidad, elemento):
        pass

    def verificarDisponibilidad(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Cantidad: {self.cantidad}"

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def isDisponibilidad(self):
        return self.disponibilidad

    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad
