class Mesero:
    ocupacion = "Mesero"
    mesasDeTrabajo = []

    def __init__(self, nombre, idEmpleado, salario):
        self.nombre = nombre
        self.idEmpleado = idEmpleado
        self.salario = salario

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

    def __str__(self):
        cadena = "EL mesero es el encargado de las mesas: "
        for mesa in self.mesasDeTrabajo:
            cadena += str(mesa.getIdMesa()) + ", "
        return cadena
