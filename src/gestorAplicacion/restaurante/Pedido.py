from src.gestorAplicacion.restaurante.Mesas import Mesas
from src.gestorAplicacion.administracion.Factura import Factura
from src.gestorAplicacion.restaurante.Gaseosas import Gaseosas


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

    def __init__(self, mesa, fecha, empleado):  # el constructor que se usa para clientes que no tienen reserva
        Pedido.idPedido += 1
        self.mesa = mesa
        self.fecha = fecha
        self.pedidoComidas = []
        self.pedidoGaseosas = []
        self.empleado = empleado
        Mesas.efectuarReserva(1, fecha)

    def agregarComidaAlPedido(self, *comidas):
        self.pedidoComidas.extend(comidas)

    def agregarGaseosaAlPedido(self, *gaseosas):
        self.pedidoGaseosas.extend(gaseosas)

    def confirmarOrden(self):
        insufficientItems = []

        for comida in self.pedidoComidas:
            if not comida.verificarIngredientes():
                insufficientItems.append(f"No hay suficientes ingredientes para preparar {comida.getNombre()}\n")


        for gaseosa in self.pedidoGaseosas:
            if gaseosa.getCantidad() < 1:
                insufficientItems.append(f"No hay suficientes {gaseosa.getNombre()}\n")


        if len(insufficientItems) > 0:
            return ''.join(insufficientItems)

        ordenConfirmada = "Orden confirmada y factura creada"
        if len(insufficientItems) == 0:
            for gaseosa in self.pedidoGaseosas:
                gaseosa.restarGaseosas(1, gaseosa)
            for comida in self.pedidoComidas:
                comida.restarCantidad()
            factura = Factura(self.getEmpleado(), self.getMesa(), self, self.getIdPedido(), self.fecha,self.precioTotal(), self.precioTotalSinGanancia())
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

    def imprimirGaseosas(self):
        sb = ''
        for gaseosas in self.pedidoGaseosas:
            sb += "Gaseosa: " + gaseosas.getNombre() + " - " + str(gaseosas.getPrecioConGanancia())+"\n"
        return sb

    def imprimirComidas(self):
        sb = ""
        for comida in self.pedidoComidas:
            sb += "Comida: " + comida.getNombre() + " - "+ str(comida.calcularPrecioConGanancia())+"\n"
        return sb

