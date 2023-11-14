from src.gestorAplicacion.administracion.Contabilidad import Contabilidad
from src.gestorAplicacion.restaurante.Inventario import Inventario


class Gaseosas(Inventario):
    listaGaseosas = []

    def __init__(self, nombre=None, precio=None, cantidad=None):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        if nombre is not None and precio is not None and cantidad is not None:
            Gaseosas.listaGaseosas.append(self)

    def comprar(self, cantidad):
        self.cantidad += cantidad
        Contabilidad.saldo -= self.precio * cantidad
        Contabilidad.gastos += self.precio*cantidad

    def restarGaseosas(self, cantidad, gaseosas):
        gaseosas.cantidad -= cantidad

    def __str__(self):
        return f"Nombre: {self.nombre} Precio {self.precio} Cantidad: {self.cantidad}"

    def getPrecioConGanancia(self):
        return self.precio + self.precio * 10 / 100

    @staticmethod
    def getListaGaseosas():
        return Gaseosas.listaGaseosas
