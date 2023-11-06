import pickle


class Factura:
    facturasSinPagar = []
    facturasPagadas = []

    def __init__(self, empleado=None, mesa=None, pedido=None, idFactura=None, fecha=None, precioTotal=None, precioTotalSinGanancia=None):
        self.empleado = empleado
        self.mesa = mesa
        self.pedido = pedido
        self.idFactura = idFactura
        self.facturaPagada = False
        self.fecha = fecha
        self.precioTotal = precioTotal
        self.precioTotalSinGanancia = precioTotalSinGanancia

    def pagarFactura(self):
        self.facturaPagada = True
        self.precioTotal = self.pedido.precioTotal()
        Factura.facturasPagadas.append(self)
        Factura.facturasSinPagar.remove(self)
        Contabilidad.sumarIngresosPedidoAlSaldo(self.getPrecioTotal())
        Contabilidad.calcularUtilidades(self.getPrecioTotal(), self.getPrecioTotalSinGanancia())
        Mesas.cancelarReserva(self.getIdFactura(), self.getFecha())

    def calificarEmpleado(self, valoracion):
        calificacion = Calificacion(self.getIdFactura(), self.getEmpleado(), valoracion)
        Calificacion.calificaciones.append(calificacion)

    # Getters y setters

    def getIdEmpleado(self):
        return self.empleado

    def getMesa(self):
        return self.mesa

    def setMesa(self, mesa):
        self.mesa = mesa

    def getPedido(self):
        return self.pedido

    def setPedido(self, pedido):
        self.pedido = pedido

    def getIdFactura(self):
        return self.idFactura

    def getCalificacionFinal(self):
        return self.calificacionFinal

    def setCalificacionFinal(self, calificacionFinal):
        self.calificacionFinal = calificacionFinal

    def setIdFactura(self, idFactura):
        self.idFactura = idFactura

    def getEmpleado(self):
        return self.empleado

    def setEmpleado(self, empleado):
        self.empleado = empleado

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getPrecioTotal(self):
        return self.precioTotal

    def setPrecioTotal(self, precioTotal):
        self.precioTotal = precioTotal

    def getPrecioTotalSinGanancia(self):
        return self.precioTotalSinGanancia

    def setPrecioTotalSinGanancia(self, precioTotalSinGanancia):
        self.precioTotalSinGanancia = precioTotalSinGanancia

    def __str__(self):
        estado_factura = "La factura está pagada" if self.factura_pagada else "La factura no está pagada"
        pedido_str = self.pedido.imprimir_comidas() + "\n" + self.pedido.imprimir_gaseosas()
        return (f" Id factura: {self.id_factura}\n"
                f"fecha: {self.fecha}\n"
                f"{estado_factura}\n"
                f" tu pedido fue: \n{pedido_str}\n"
                f" te atendio: {self.empleado}\n"
                f" estuviste en la Mesa: {self.mesa.get_id_mesa()}\n"
                f" el valor a pagar es: {self.pedido.precio_total()}\n\n")