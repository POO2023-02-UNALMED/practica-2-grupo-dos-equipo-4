from src.gestorAplicacion.administracion.Contabilidad import Contabilidad

class Ingredientes:
    ingredientesComprados = 0
    listaIngredientes = []

    def __init__(self, nombre=None, precio=None, cantidad=None):
        if nombre is not None and precio is not None and cantidad is not None:
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            Ingredientes.listaIngredientes.append(self)

    def comprar(self, cantidad, ingrediente):
        for i in Ingredientes.listaIngredientes:
            if i == ingrediente:
                ingrediente.cantidad += cantidad
                Contabilidad.saldo -= ingrediente.precio * cantidad
                Contabilidad.setGastos(ingrediente.precio * cantidad)
                Ingredientes.ingredientesComprados += ingrediente.precio * cantidad

    def restarIngredientes(self, cantidad):
        self.cantidad -= cantidad

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Cantidad: {self.cantidad}"

    def getNombre(self):
        return self.nombre
