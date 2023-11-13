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

    def comprar(self, cantidad, gaseosa):
        for i in Gaseosas.listaGaseosas:
            if i == gaseosa:
                gaseosa.cantidad += cantidad
                Contabilidad.saldo -= gaseosa.precio * cantidad
                Contabilidad.setGastos(gaseosa.precio * cantidad)

    def restarGaseosas(self, cantidad, gaseosas):
        gaseosas.cantidad -= cantidad

    def __str__(self):
        return f"Nombre: {self.nombre} Precio {self.precio} Cantidad: {self.cantidad}"

    def getPrecioConGanancia(self):
        return self.precio + self.precio * 10 / 100

    @staticmethod
    def getListaGaseosas():
        return Gaseosas.listaGaseosas
