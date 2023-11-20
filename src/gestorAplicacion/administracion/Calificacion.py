from src.errorAplicacion.ErrorAdministracion import ErroresAdministracion


class Calificacion:
    calificaciones = []
    def __init__(self, idFactura, empleado, calificacion):
        # Constructor sin argumentos necesario para deserialización
        self._idFactura = idFactura
        self._empleado = empleado
        self._calificacion = calificacion

    def setIdFactura(self, _idFactura):
        self._idFactura = _idFactura

    def setIdEmpleado(self, id_empleado):
        self._empleado = id_empleado

    def setCalificacion(self, _calificacion):
        try:
            if _calificacion < 0 or _calificacion > 5:
                raise ErroresAdministracion("_calificacion_invalida")
            self._calificacion = _calificacion
        except ErroresAdministracion as e:
            e.manejo_error()
    def getIdFactura(self):
        return self._idFactura

    def getEmpleadoNombre(self):
        return self._empleado.getNombre()

    def getEmpleado(self):
        return self._empleado

    def getCalificacion(self):
        return self._calificacion

    def __str__(self):
        sb = ""
        sb += "Id factura: " + str(self.getIdFactura()) + "\n"
        sb += "empleado: " + str(self.getEmpleadoNombre()) + "\n"
        sb += "Calificación: " + str(self.getCalificacion()) + "\n"
        return sb

