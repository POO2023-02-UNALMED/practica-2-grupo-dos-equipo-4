
from src.gestorAplicacion.administracion import Contabilidad
from src.gestorAplicacion.administracion import Calificacion
from src.gestorAplicacion.restaurante import Mesas
from src.gestorAplicacion.administracion.Calificacion import Calificacion

class Factura:
    facturasSinPagar = []
    facturasPagadas = []

    def __init__(self, empleado, mesa, pedido, idFactura, fecha, precioTotal, precioTotalSinGanancia):
        self.empleado = empleado
        self.mesa = mesa
        self.pedido = pedido
        self.idFactura = idFactura
        self.factura_pagada = False
        self.fecha = fecha
        self.precioTotal = precioTotal
        self.precioTotalSinGanancia = precioTotalSinGanancia

    def pagarFactura(self):
        self.facturaPagada = True
        self.precioTotal = self.pedido.precioTotal()
        Factura.facturasPagadas.append(self)
        Factura.facturasSinPagar.remove(self)
        Contabilidad.Contabilidad.sumarIngresosPedidoAlSaldo(self.getPrecioTotal())
        Contabilidad.Contabilidad.calcularUtilidades(self.getPrecioTotal(), self.getPrecioTotalSinGanancia())
        self.mesa.cancelarReserva(self.getIdFactura(), self.getFecha())

    def calificarEmpleado(self, valoracion):
        calificacion = Calificacion(self.getIdFactura(), self.getEmpleado(), valoracion)
        Calificacion.calificaciones.append(calificacion)
        # Error por corregir no se esta creando la instancia de calificacion

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

    def getNombreEmpleado(self):
        return self.empleado.nombre
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
    def estaPagada(self):
        if self.factura_pagada is True:
            return "La factura está pagada"
        else:
            return  "La factura no está pagada"

    def __str__(self):
        sb = ""
        sb += "  Id factura:  " + str(self.getIdFactura()) + "\n"
        sb += "fecha: " + str(self.getFecha()) + "\n"
        sb += self.estaPagada() + "\n"
        sb += "  tu pedido fue: \n" + self.pedido.imprimirComidas() + "\n"
        sb += self.pedido.imprimirGaseosas() + "\n"
        sb += "  te atendio: " + str(self.getNombreEmpleado()) + "\n"
        sb += "  estuviste en la Mesa: " + str(self.mesa.getIdMesa()) + "\n"
        sb += "  el valor a pagar es: " + str(self.pedido.precioTotal()) + "\n"
        sb += "\n"
        return sb