class Pedido:
    idPedido = 10000000

    def __init__(self, mesa, fecha, idCliente, empleado):
        Pedido.idPedido += 1
        self.mesa = mesa
        self.idCliente = idCliente
        self.fecha = fecha
        self.pedidoComidas = []
        self.pedidoGaseosas = []
        self.empleado = empleado
        Mesas.efectuarReserva(idCliente, fecha)

    def agregarComidaAlPedido(self, *comidas):
        self.pedidoComidas.extend(comidas)

    def agregarGaseosaAlPedido(self, *gaseosas):
        self.pedidoGaseosas.extend(gaseosas)

    def confirmarOrden(self):
        insufficientItems = []
        ordenConfirmada = None

        for comida in self.pedidoComidas:
            if not comida.verificarIngredientes():
                insufficientItems.append(f"No hay suficientes ingredientes para preparar {comida.getNombre()}\n")
            else:
                comida.restarCantidad()

        for gaseosa in self.pedidoGaseosas:
            if gaseosa.getCantidad() < 1:
                insufficientItems.append(f"No hay suficientes {gaseosa.getNombre()}\n")
            else:
                gaseosa.restarGaseosas(1, gaseosa)

        if len(insufficientItems) > 0:
            return ''.join(insufficientItems)

        ordenConfirmada = "Orden confirmada y factura creada"
        if ordenConfirmada == "Orden confirmada y factura creada":
            factura = Factura(self.getEmpleado(), self.getMesa(), self, self.getIdPedido(), self.fecha, self.precioTotal(), self.precioTotalSinGanancia())
            Factura.facturasSinPagar.append(factura)
        return ordenConfirmada

    def precioTotal(self):
        suma = 0
        for comida in self.pedidoComidas:
            suma += comida.calcularPrecioConGanancia()
        for gaseosa in self.pedidoGaseosas:
            suma += gaseosa.getPrecioConGanancia()
        return suma

    def precioTotalSinGanancia(self):
        suma = 0
        for comida in self.pedidoComidas:
            suma += comida.calcularPrecio()
        for gaseosa in self.pedidoGaseosas:
            suma += gaseosa.getPrecio()
        return suma

    # Getters y Setters
    def getIdPedido(self):
        return Pedido.idPedido

    def setIdPedido(self, idPedido):
        Pedido.idPedido = idPedido

    def getMesa(self):
        return self.mesa

    def setMesa(self, mesa):
        self.mesa = mesa

    def getPedidoComidas(self):
        return self.pedidoComidas

    def getPedidoGaseosas(self):
        return self.pedidoGaseosas

    def getEmpleado(self):
        return self.empleado

    def setEmpleado(self, empleado):
        self.empleado = empleado
