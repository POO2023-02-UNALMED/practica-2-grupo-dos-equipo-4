import pickle
from src.uiMain.Hamburgueseria import *

def serializar(Objetos):
    #La función 'serializar' toma un objeto y lo guarda como un archivo pickle con un nombre dado en el directorio.
    file=open("src/baseDatos/temp/objetos.pickle.pickle","wb")
    pickle.dump(Objetos,file)
    file.close()

def deserializar():
    #La función deserializar toma un objeto, abre un archivo pickle correspondiente y devuelve el objeto deserializado.
    file=open("src/baseDatos/temp/objetos.pickle.pickle","rb")
    datos=pickle.load(file)
    return datos

    # Serializar un pedido
#pedido_serializado = Serializador.serializar(pedido1)

# Deserializar el pedido
#pedido_deserializado = Serializador.deserializar(pedido_serializado)
# Serializar un objeto Gaseosas
#gaseosas_serializada = Serializador.serializar(sprite)

# Deserializar el objeto Gaseosas
#gaseosas_deserializada = Serializador.deserializar(gaseosas_serializada)

# Serializar un objeto Ingredientes
#ingredientes_serializado = Serializador.serializar(pan)

# Deserializar el objeto Ingredientes
#ingredientes_deserializado = Serializador.deserializar(ingredientes_serializado)

# Serializar un objeto Comida
#comida_serializada = Serializador.serializar(clasicaDeCarne)

# Deserializar el objeto Comida
#comida_deserializada = Serializador.deserializar(comida_serializada)

# Serializar un objeto Mesero
#mesero_serializado = Serializador.serializar(camilo)

# Deserializar el objeto Mesero
#mesero_deserializado = Serializador.deserializar(mesero_serializado)

# Serializar un objeto Cocinero
#cocinero_serializado = Serializador.serializar(david)

# Deserializar el objeto Cocinero
#cocinero_deserializado = Serializador.deserializar(cocinero_serializado)