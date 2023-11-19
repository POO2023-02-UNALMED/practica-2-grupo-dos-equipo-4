import pickle
from src.uiMain.Hamburgueseria import *
class Serializador:
    @staticmethod
    def serializar(objeto):
        return pickle.dumps(objeto)

    @staticmethod
    def deserializar(datos_serializados):
        return pickle.loads(datos_serializados)

    # Serializar un pedido
pedido_serializado = Serializador.serializar(pedido1)

# Deserializar el pedido
pedido_deserializado = Serializador.deserializar(pedido_serializado)