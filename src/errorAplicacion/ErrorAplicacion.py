class ErrorAplicacion(Exception):
    def __init__(self, message):
        self.message = "Manejo de errores de la Aplicacion: " + message
        super().__init__(self.message)

