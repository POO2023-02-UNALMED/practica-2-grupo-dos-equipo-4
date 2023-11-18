from src.errorAplicacion.ErrorAdministracion import ErroresAdministracion
from src.gestorAplicacion.administracion.Contabilidad import Contabilidad
from src.gestorAplicacion.restaurante.Inventario import Inventario



class Ingredientes(Inventario):
    listaIngredientes = []

    def __init__(self, nombre=None, precio=None, cantidad=None):
        if nombre is not None and precio is not None and cantidad is not None:
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            Ingredientes.listaIngredientes.append(self)

    def comprar(self, cantidad): #Este metodo activa comprar ingredientes desde el objeto en si (Usar este de ser necesario)
        try:
            if self.cantidad*self.precio > Contabilidad.saldo:
                raise ErroresAdministracion("saldo_insuficiente")
            self.cantidad += cantidad
            Contabilidad.saldo -= self.precio * cantidad
            Contabilidad.gastos += self.precio*cantidad
        except ErroresAdministracion as e:
            e.manejo_error()

    @staticmethod
    def comprarIngredientes(cantidad, ingrediente): #Este metodo activa comprar ingredientes desde la clase recibiendo el nombre del ingrediente (Usar este de ser necesario)
        for i in Ingredientes.listaIngredientes:
            if Ingredientes.getNombre(i) == ingrediente:
                i.cantidad += cantidad
                Contabilidad.saldo -= i.precio * cantidad
                Contabilidad.setGastos(i.precio * cantidad)
                Ingredientes.ingredientesComprados += i.precio * cantidad

    def restarIngredientes(self, cantidad):
        self.cantidad -= cantidad

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Cantidad: {self.cantidad}"

    def getNombre(self):
        return self.nombre
