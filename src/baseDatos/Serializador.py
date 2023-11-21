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
# Serializar un objeto Gaseosas
gaseosas_serializada = Serializador.serializar(sprite)

# Deserializar el objeto Gaseosas
gaseosas_deserializada = Serializador.deserializar(gaseosas_serializada)

# Serializar un objeto Ingredientes
ingredientes_serializado = Serializador.serializar(pan)

# Deserializar el objeto Ingredientes
ingredientes_deserializado = Serializador.deserializar(ingredientes_serializado)

# Serializar un objeto Comida
comida_serializada = Serializador.serializar(clasicaDeCarne)

# Deserializar el objeto Comida
comida_deserializada = Serializador.deserializar(comida_serializada)

# Serializar un objeto Mesero
mesero_serializado = Serializador.serializar(camilo)

# Deserializar el objeto Mesero
mesero_deserializado = Serializador.deserializar(mesero_serializado)

# Serializar un objeto Cocinero
cocinero_serializado = Serializador.serializar(david)

# Deserializar el objeto Cocinero
cocinero_deserializado = Serializador.deserializar(cocinero_serializado)