from src.gestorAplicacion.administracion.Cocinero import Cocinero
from src.gestorAplicacion.administracion.Mesero import Mesero
from src.gestorAplicacion.restaurante.Ingredientes import Ingredientes
from src.gestorAplicacion.restaurante.Comida import Comida
from src.gestorAplicacion.restaurante.Mesas import Mesas

cocinero = Cocinero("David", 100, 50000, "Calvas")
print(cocinero.getOcupacion())
mesero = Mesero("Camilo", 100, 2000)
print(mesero.accion())
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
especialQuesoYTocineta = Comida("Especial con queso y tocineta", ingredientesCarneQuesoYTocineta, cantidadesCarneQuesoYTocineta)

ingredientesClasicaPollo = [pan, carneDeRes, tomate, cebolla, lechuga]
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


print(carnibora.calcularPrecio())
print(carnibora.calcularPrecioConGanancia())

print(carnibora.verificarIngredientes())


print(clasicaDeCarne.__str__())
print(especialQuesoYTocineta.__str__())
print(clasicaDePollo.__str__())
print(polloconQueso.__str__())

Comida.listaComida.append(clasicaDeCarne)
Comida.listaComida.append(especialQuesoYTocineta)
Comida.listaComida.append(clasicaDePollo)
Comida.listaComida.append(polloconQueso)
Comida.listaComida.append(dobleCarneTocineta)
Comida.listaComida.append(vegetariana)
Comida.listaComida.append(carnibora)

print(Comida.listaComida.__str__())
