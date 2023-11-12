from src.gestorAplicacion.administracion.Calificacion import Calificacion
from abc import ABC, abstractmethod
class Empleado(ABC):
    empleados = []
    cantidadEmpleados = 0

    def __init__(self, nombre=None, idEmpleado = 100, salario=0):
        if nombre is not None:
            Empleado.cantidadEmpleados += 1
            self.nombre = nombre
            self.idEmpleado = idEmpleado
            self.salario = salario
            Empleado.empleados.append(self)
    @abstractmethod
    def getOcupacion(self):
        pass


    def accion(self):
        return "El Empleado esta Trabajando"

    def bono(self):
        calificacionesEmpleado = []
        suma = 0
        for calificacion in Calificacion.Calificacion.calificaciones():
            if calificacion.getEmpleado() == self:
                calificacionesEmpleado.append(calificacion.getCalificacion())
        for califica in calificacionesEmpleado:
            suma += califica
        promedio = suma / len(calificacionesEmpleado)
        return promedio >= 4.5

    def getCantidadEmpleados(self):
        return Empleado.cantidadEmpleados
    def getEmpleados(self):
        return Empleado.empleados

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getIdEmpleado(self):
        return self.idEmpleado

    def setIdEmpleado(self, idEmpleado):
        self.idEmpleado = idEmpleado

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def __str__(self):
        sb = "El empleado: " + self.getNombre() + "\n"
        sb += "Tiene el id: " + str(self.getIdEmpleado()) + "\n"
        sb += "Gana un salario de: " + str(self.getSalario()) + "\n"
        if self.bono():
            sb += "El empleado tiene bono" + "\n"
        else:
            sb += "El empleado no tiene bono" + "\n"
        return sb
