from src.gestorAplicacion.administracion.Empleado import Empleado


class Mesero(Empleado):
    ocupacion = "Mesero"
    mesasDeTrabajo = []

    def __init__(self, nombre, salario, idEmpleado):
        super().__init__(nombre,salario, idEmpleado)
        self.nombre = nombre
        self.salario = salario
        self.idEmpleado = idEmpleado

    def agregarMesas(self, mesa):
        self.mesasDeTrabajo.append(mesa)

    def quitarMesas(self, quitar):
        self.mesasDeTrabajo = [mesa for mesa in self.mesasDeTrabajo if mesa != quitar]

    def getOcupacion(self):
        return "Mesero"

    def getNombre(self):
        return self.nombre


    def accion(self):
        return "El Mesero " + self.nombre + " está atendiendo las mesas."

    def mesasEncargadas(self):
        cadena = "EL mesero es el encargado de las mesas: "
        for mesa in self.mesasDeTrabajo:
            cadena += str(mesa.getIdMesa()) + ", "
        return cadena
