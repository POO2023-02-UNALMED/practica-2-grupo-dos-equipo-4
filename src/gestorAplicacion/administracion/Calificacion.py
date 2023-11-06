class Calificacion:
    calificaciones = []
    def __init__(self, idFactura=None, empleado=None, calificacion=None):
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
        return self.empleado

    def getCalificacion(self):
        return self.calificacion

    def __str__(self):
        return "Empleado: " + self.getEmpleado().getNombre() + "\n" + \
            "Del servicio: " + str(self.idFactura) + "\n" + \
            "Su calificación fue: " + str(self.calificacion) + "\n"
