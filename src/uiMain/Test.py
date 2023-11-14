from src.gestorAplicacion.administracion.Cocinero import Cocinero
from src.gestorAplicacion.administracion.Mesero import Mesero
from src.gestorAplicacion.restaurante.Ingredientes import Ingredientes
from src.gestorAplicacion.restaurante.Comida import Comida
from src.gestorAplicacion.restaurante.Gaseosas import Gaseosas
from src.gestorAplicacion.restaurante.Mesas import Mesas
from src.gestorAplicacion.restaurante.Pedido import Pedido
from src.gestorAplicacion.administracion.Contabilidad import Contabilidad
from src.gestorAplicacion.administracion.Factura import Factura
from src.gestorAplicacion.administracion.Calificacion import Calificacion
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

camilo = Mesero("Camilo", 100)
linda = Mesero("Linda", 100)
david = Cocinero("David", 100, "Calvas")

mesa12.crearReserva(890123, 12, datetime(2023, 10, 4, 12, 0, 0))


listaPedido = []
# pedidos con reservas
pedido1 = Pedido(mesa12, datetime(2023, 10, 4, 12, 0, 0), camilo, 890123)
pedido1.agregarComidaAlPedido(especialQuesoYTocineta, polloconQueso, vegetariana)
pedido1.agregarGaseosaAlPedido(quatro, coca_cola, coca_cola)
pedido1.confirmarOrden()


# pedidos sin reservas
pedido3 = Pedido(mesa4, datetime(2023, 10, 4, 12, 0, 0), camilo)
pedido3.agregarGaseosaAlPedido(coca_cola, coca_cola)
pedido3.agregarComidaAlPedido(clasicaDeCarne, dobleCarneTocineta)
pedido3.confirmarOrden()

pedido4 = Pedido(mesa1, datetime(2023, 3, 10, 4, 30, 0), camilo)
pedido4.agregarGaseosaAlPedido(quatro, sprite)
pedido4.agregarComidaAlPedido(clasicaDePollo, especialQuesoYTocineta)
pedido4.confirmarOrden()

pedido5 = Pedido(mesa2, datetime(2023, 3, 11, 2, 0, 0), camilo)
pedido5.agregarGaseosaAlPedido(coca_cola, sprite)
pedido5.agregarComidaAlPedido(vegetariana)
pedido5.confirmarOrden()

pedido6 = Pedido(mesa2, datetime(2023, 2, 11, 2, 0, 0), linda)
pedido6.agregarGaseosaAlPedido(coca_cola, sprite)
pedido6.agregarComidaAlPedido(vegetariana)
pedido6.confirmarOrden()


pedido7 = Pedido(mesa7, datetime(2023, 2, 11, 2, 0, 0), linda)
pedido7.agregarGaseosaAlPedido(coca_cola, sprite)
pedido7.agregarComidaAlPedido(vegetariana)
pedido7.confirmarOrden()

for factura in Factura.facturasSinPagar:
    print(factura.__str__())


def pagarFacturaYCalificar(id, valoracion):
    for factura in Factura.facturasSinPagar:
        if factura.getIdFactura() == id:
            factura.pagarFactura()
            factura.calificarEmpleado(valoracion)
            break


pagarFacturaYCalificar(10000001, 5)


pagarFacturaYCalificar(10000002, 5)
pagarFacturaYCalificar(10000003, 5)
pagarFacturaYCalificar(10000004, 3.5)
pagarFacturaYCalificar(10000005, 4.5)
pagarFacturaYCalificar(10000006, 5)


# for calificacion in Calificacion.calificaciones:
#    print(calificacion.__str__())

# print(camilo.bono())

# for empleado in Mesero.empleados:
#    print(empleado.__str__())

'''
print(Contabilidad.saldo) #saldo con los ingresos de los pedidos
print(Contabilidad.ingresos) # el dinero que ha ingresado de los pedidos
print(Contabilidad.utilidades) #las ganancias de los pedidos

Contabilidad.setServiciosPublicos(20000) #lo que se va a pagar de servicios publicos
print(Contabilidad.pagarServicios())

print(Contabilidad.saldo) #saldo después de pagar servicios

print(Contabilidad.pagarSueldos()) #lo que se paga de sueldos

print(Contabilidad.saldo) # después de pagar sueldos



print(Contabilidad.gastos) #los gastos que hemos tenido

tomate.comprar(1)
coca_cola.comprar(1)

print(Contabilidad.saldo)
print(Contabilidad.gastos)

'''
