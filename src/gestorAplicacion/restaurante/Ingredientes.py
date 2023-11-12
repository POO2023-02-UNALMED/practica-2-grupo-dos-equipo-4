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

    def comprar(self, cantidad): #Este metodo activa comprar ingredientes desde el objeto en si (Usar este de ser necesario)
        self.cantidad += cantidad
        Contabilidad.saldo -= self.precio * cantidad
        Contabilidad.setGastos(self.precio * cantidad)
        Ingredientes.ingredientesComprados += self.precio * cantidad

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
