from src.errorAplicacion.ErrorAplicacion import ErrorAplicacion


class ErroresAdministracion(ErrorAplicacion):
    def __init__(self, tipo_error):
        if tipo_error == "factura_ya_pagada":
            message = "La factura ya ha sido pagada"
        elif tipo_error == "calificacion_invalida":
            message = "La calificación es inválida"
        elif tipo_error == "saldo_insuficiente":
            message = "El saldo es insuficiente"
        else:
            message = "Error desconocido"
        super().__init__(message)

    def manejo_error(self):
        print(self.message)
