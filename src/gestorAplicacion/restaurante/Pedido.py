from src.gestorAplicacion.restaurante.Mesas import Mesas
from src.gestorAplicacion.administracion.Factura import Factura
from src.gestorAplicacion.restaurante.Gaseosas import Gaseosas
from src.errorAplicacion.ErrorRestaurante import ErrorRestaurante
from datetime import datetime


class Pedido:
    idPedido = 10000000

    class Pedido:
        idPedido = 0

    class Pedido:
        idPedido = 10000000

    class Pedido:
        idPedido = 0

    def __init__(self, mesa, fecha, empleado, idCliente=None):
        Pedido.idPedido += 1
        self.mesa = mesa
        self.fecha = fecha
        self.pedidoComidas = []
        self.pedidoGaseosas = []
        self.empleado = empleado
        self.idCliente = idCliente if idCliente is not None else 1

        mesa.efectuarReserva(self.idCliente, fecha)

    def agregarComidaAlPedido(self, *comidas):
        self.pedidoComidas.extend(comidas)

    def agregarGaseosaAlPedido(self, *gaseosas):
        self.pedidoGaseosas.extend(gaseosas)

    def confirmarOrden(self):
        try:
            insufficientItems = []

            for comida in self.pedidoComidas:
                if not comida.verificarIngredientes():
                    insufficientItems.append(f"No hay suficientes ingredientes para preparar {comida.getNombre()}\n")

            for gaseosa in self.pedidoGaseosas:
                if gaseosa.getCantidad() < 1:
                    insufficientItems.append(f"No hay suficientes {gaseosa.getNombre()}\n")

            if len(insufficientItems) > 0:
                raise ErrorRestaurante("sin_ingredientes")

            if len(self.pedidoComidas) == 0 and len(self.pedidoGaseosas) == 0:
                raise ErrorRestaurante("pedido_vacio")

            ordenConfirmada = "Orden confirmada y factura creada"
            if len(insufficientItems) == 0:
                for gaseosa in self.pedidoGaseosas:
                    gaseosa.restarGaseosas(1, gaseosa)
                for comida in self.pedidoComidas:
                    comida.restarCantidad()
                factura = Factura(self.getEmpleado(), self.getMesa(), self, self.getIdPedido(), self.fecha,
                              self.precioTotal(), self.precioTotalSinGanancia(), self.idCliente)
                Factura.facturasSinPagar.append(factura)

            return ordenConfirmada

        except ErrorRestaurante as e:
            e.manejo_error()

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

    def getIdCliente(self):
        return self.idCliente

    def getIdPedido(self):
        return self.idPedido

    def setIdPedido(self, idPedido):
        self.idPedido = idPedido

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
            sb += "Gaseosa: " + gaseosas.getNombre() + " - " + str(gaseosas.getPrecioConGanancia()) + "\n"
        return sb

    def imprimirComidas(self):
        sb = ""
        for comida in self.pedidoComidas:
            sb += "Comida: " + comida.getNombre() + " - " + str(comida.calcularPrecioConGanancia()) + "\n"
        return sb
