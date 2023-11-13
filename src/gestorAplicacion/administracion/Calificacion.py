
class Calificacion:
    calificaciones = []
    def __init__(self, idFactura, empleado, calificacion):
        # Constructor sin argumentos necesario para deserialización
        self.idFactura = idFactura
        self.empleado = empleado
        self.calificacion = calificacion

    def setIdFactura(self, idFactura):
        self.idFactura = idFactura

    def setIdEmpleado(self, idEmpleado):
        self.empleado = idEmpleado

    def setCalificacion(self, calificacion):
        self.calificacion = calificacion

    def getIdFactura(self):
        return self.idFactura

    def getEmpleado(self):
        return self.empleado.getNombre()

    def getCalificacion(self):
        return self.calificacion

    def __str__(self):
        sb = ""
        sb += "Id factura: " + str(self.getIdFactura()) + "\n"
        sb += "Empleado: " + str(self.getEmpleado()) + "\n"
        sb += "Calificación: " + str(self.getCalificacion()) + "\n"
        return sb

