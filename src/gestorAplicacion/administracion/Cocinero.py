from src.gestorAplicacion.administracion.Empleado import Empleado


class Cocinero(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad
        self.ocupacion = "Cocinero"
        Empleado.empleados.append(self)

    def accion(self):
        return f"El Cocinero {self.nombre} esta cocinando."

    def getOcupacion(self):
        return self.ocupacion

    def preparar_plato(self, pedido):
        print(f"El cocinero {self.nombre} ha terminado de preparar el pedido de {pedido.id_pedido}")

    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, especialidad):
        self.especialidad = especialidad
