from src.errorAplicacion.ErrorAplicacion import ErrorAplicacion


class ErrorRestaurante(ErrorAplicacion):
    def __init__(self, tipo_error, mensaje = "ErrorRestaurante: "):
        self.mensaje = mensaje
        if tipo_error == "mesa_ocupada":
            message = self.mensaje + "La mesa ya está ocupada en esta fecha"
        elif tipo_error == "pedido_vacio":
            message = self.mensaje + "No se han agregado comidas o gaseosas al pedido"
        elif tipo_error == "sin_ingredientes":
            message = self.mensaje + "No hay suficientes ingredientes para la orden"

        else:
            message = self.mensaje + "Error desconocido"
        super().__init__(message)

    def manejo_error(self):
        print(self.message)
