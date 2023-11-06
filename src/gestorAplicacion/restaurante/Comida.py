class Comida:
    listaComida = []

    def __init__(self, nombre=None, ingredientes=None, cantidades=None):
        self.nombre = nombre
        self.ingredientesDeComida = {}
        if nombre is not None and ingredientes is not None and cantidades is not None:
            for i in range(len(ingredientes)):
                self.ingredientesDeComida[ingredientes[i]] = cantidades[i]
            Comida.listaComida.append(self)

    def agregarIngrediente(self, ingrediente, cantidad):
        if ingrediente in self.ingredientesDeComida:
            self.ingredientesDeComida[ingrediente] += cantidad
        else:
            self.ingredientesDeComida[ingrediente] = cantidad

    def removerIngrediente(self, ingrediente, cantidad):
        if ingrediente in self.ingredientesDeComida:
            if self.ingredientesDeComida[ingrediente] <= cantidad:
                del self.ingredientesDeComida[ingrediente]
            else:
                self.ingredientesDeComida[ingrediente] -= cantidad

    def getIngredientesDeComida(self):
        return self.ingredientesDeComida

    def restarCantidad(self):
        for ingrediente, cantidad in self.ingredientesDeComida.items():
            ingrediente.restarIngredientes(cantidad)

    def calcularPrecio(self):
        precioTotal = 0
        for ingrediente, cantidad in self.ingredientesDeComida.items():
            precioTotal += ingrediente.precio * cantidad
        return precioTotal

    def calcularPrecioConGanancia(self):
        precioTotalConGanancia = 0
        for ingrediente, cantidad in self.ingredientesDeComida.items():
            precioTotalConGanancia += ingrediente.precio * cantidad + (ingrediente.precio * cantidad) * 10 / 100
        return precioTotalConGanancia

    def __str__(self):
        sb = f"Comida: {self.nombre}\nIngredientes:\n"
        for ingrediente, cantidad in self.ingredientesDeComida.items():
            sb += f"- {ingrediente.getNombre()}: {cantidad}\n"
        return sb

    def verificarIngredientes(self):
        for ingrediente, cantidadNecesaria in self.ingredientesDeComida.items():
            if ingrediente.getCantidad() < cantidadNecesaria:
                return False
        return True

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
