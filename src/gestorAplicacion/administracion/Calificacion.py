from src.errorAplicacion.ErrorAdministracion import ErroresAdministracion


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
        try:
            if calificacion < 0 or calificacion > 5:
                raise ErroresAdministracion("calificacion_invalida")
            self.calificacion = calificacion
        except ErroresAdministracion as e:
            e.manejo_error()
    def getIdFactura(self):
        return self.idFactura

    def getEmpleadoNombre(self):
        return self.empleado.getNombre()

    def getEmpleado(self):
        return self.empleado

    def getCalificacion(self):
        return self.calificacion

    def __str__(self):
        sb = ""
        sb += "Id factura: " + str(self.getIdFactura()) + "\n"
        sb += "Empleado: " + str(self.getEmpleadoNombre()) + "\n"
        sb += "Calificación: " + str(self.getCalificacion()) + "\n"
        return sb

