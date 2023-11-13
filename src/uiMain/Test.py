from src.gestorAplicacion.administracion.Cocinero import Cocinero
from src.gestorAplicacion.administracion.Mesero import Mesero
from src.gestorAplicacion.restaurante.Ingredientes import Ingredientes
from src.gestorAplicacion.restaurante.Comida import Comida
from src.gestorAplicacion.restaurante.Gaseosas import Gaseosas
from src.gestorAplicacion.restaurante.Mesas import Mesas
from src.gestorAplicacion.restaurante.Pedido import Pedido
from src.gestorAplicacion.administracion.Contabilidad import Contabilidad
from src.gestorAplicacion.administracion.Factura import Factura
from datetime import datetime

sprite = Gaseosas("Sprite", 2000, 20)
coca_cola = Gaseosas("Coca cola", 2100, 20)
quatro = Gaseosas("Quatro", 1960, 20)

pan = Ingredientes("Pan", 1000, 20)
carneDeRes = Ingredientes("Carne de res", 6000, 20)
carneDePollo = Ingredientes("Carne de pollo", 7000, 20)
carneVegana = Ingredientes("Carne vegana", 4000, 20)
tomate = Ingredientes("Tomate", 400, 20)
cebolla = Ingredientes("Cebolla", 200, 20)
lechuga = Ingredientes("Lechuga", 150, 20)
queso = Ingredientes("Queso", 2000, 20)
tocineta = Ingredientes("Tocineta", 1000, 20)

print(pan.__str__())
pan.comprarIngredientes(20, "Pan")
print(pan.__str__())

IngredientesClasicaCarne = [pan, carneDeRes, tomate, cebolla, lechuga]
CantidadesClasicaCarne = [2, 1, 1, 1, 1]
clasicaDeCarne = Comida("Clasica de carne", IngredientesClasicaCarne, CantidadesClasicaCarne)

ingredientesCarneQuesoYTocineta = [pan, carneDeRes, queso, tocineta, tomate, cebolla, lechuga]
cantidadesCarneQuesoYTocineta = [2, 1, 2, 3, 1, 2, 2]
especialQuesoYTocineta = Comida("Especial con queso y tocineta", ingredientesCarneQuesoYTocineta,
                                cantidadesCarneQuesoYTocineta)

ingredientesClasicaPollo = [pan, carneDePollo, tomate, cebolla, lechuga]
cantidadesClasicaPollo = [2, 1, 1, 1, 1]
clasicaDePollo = Comida("Clasica de Pollo", ingredientesClasicaPollo, cantidadesClasicaPollo)

ingredientesPolloqueso = [pan, carneDePollo, queso, tomate, cebolla, lechuga]
cantidadespolloconQueso = [2, 1, 1, 1, 1, 1]
polloconQueso = Comida("Clasica de Pollo con queso", ingredientesPolloqueso, cantidadespolloconQueso)

ingredientesDobleCarneTocineta = [pan, carneDeRes, queso, tocineta, tomate, cebolla, lechuga]
cantidadesDobleCarneTocineta = [2, 2, 3, 4, 2, 2, 2]
dobleCarneTocineta = Comida("Doble carne tocineta", ingredientesDobleCarneTocineta, cantidadesDobleCarneTocineta)

ingredientesVegetariana = [pan, carneVegana, queso, tomate, cebolla, lechuga]
cantidadesVegetariana = [2, 1, 2, 2, 2, 2]
vegetariana = Comida("Vegetariana", ingredientesVegetariana, cantidadesVegetariana)

ingredientesCarnibora = [pan, carneDeRes, carneDePollo, tocineta, queso]
cantidadesCarnibora = [2, 1, 1, 4, 2]
carnibora = Comida("Carnibora", ingredientesCarnibora, cantidadesCarnibora)

Comida.listaComida.append(clasicaDeCarne)
Comida.listaComida.append(especialQuesoYTocineta)
Comida.listaComida.append(clasicaDePollo)
Comida.listaComida.append(polloconQueso)
Comida.listaComida.append(dobleCarneTocineta)
Comida.listaComida.append(vegetariana)
Comida.listaComida.append(carnibora)

mesa1 = Mesas(1, 2)
mesa2 = Mesas(2, 2)
mesa3 = Mesas(3, 2)
mesa4 = Mesas(4, 2)
mesa5 = Mesas(5, 4)
mesa6 = Mesas(6, 4)
mesa7 = Mesas(7, 4)
mesa8 = Mesas(8, 4)
mesa9 = Mesas(9, 4)
mesa10 = Mesas(10, 6)
mesa11 = Mesas(11, 6)
mesa12 = Mesas(12, 8)
mesa13 = Mesas(13, 8)
mesa14 = Mesas(14, 10)
mesa15 = Mesas(15, 10)

camilo = Mesero("Camilo", 100, 2000)
print(camilo.accion())

david = Cocinero("David", 100, 50000, "Calvas")
print(david.getOcupacion())

mesa12.crearReserva(890123, 12, datetime(2023,10,4,12,0,0))
mesa12.crearReserva(89012, 12, datetime(2023,12,3,1,0,0))
print(mesa12.__str__())

listaPedido = []
# pedidos con reservas
pedido1 = Pedido(mesa12, datetime(2023,10,4,12,0,0), camilo, 890123)
print(mesa12.__str__())
pedido1.agregarComidaAlPedido(especialQuesoYTocineta, polloconQueso, vegetariana)
pedido1.agregarGaseosaAlPedido(quatro, coca_cola, coca_cola)

# pedidos sin reservas
pedido3 = Pedido(mesa4, datetime(2023,10,4,12,0,0), camilo)
pedido3.agregarGaseosaAlPedido(coca_cola, coca_cola)
pedido3.agregarComidaAlPedido(clasicaDeCarne, dobleCarneTocineta)

pedido5 = Pedido(mesa2, datetime(2023,3,11,2,0,0), camilo)
pedido5.agregarGaseosaAlPedido(coca_cola, sprite)
pedido5.agregarComidaAlPedido(vegetariana)
print(pedido5.confirmarOrden())

pedido4 = Pedido(mesa1,datetime(2023,3,10,4,30,0), camilo)
pedido4.agregarGaseosaAlPedido(quatro, sprite)
pedido4.agregarComidaAlPedido(clasicaDePollo, especialQuesoYTocineta)

listaPedido.append(pedido4)
listaPedido.append(pedido3)
listaPedido.append(pedido5)
