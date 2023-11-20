from abc import ABC, abstractmethod
from src.gestorAplicacion.restaurante import Gaseosas, Comida

class MenuMethods:
    @staticmethod
    def mostrarMenuComidas():
        menuComidas = []
        for comida in Comida.listaComida:
            menuComidas.append(f"{comida.getNombre()} - Precio: ${comida.calcularPrecio()}")
        return "\n".join(menuComidas)

    @staticmethod
    def mostrarMenuGaseosas():
        menuGaseosas = []
        for gaseosa in Gaseosas.listaGaseosas:
            menuGaseosas.append(f"{gaseosa.getNombre()} - Precio: ${gaseosa.getPrecio()}")
        return "\n".join(menuGaseosas)
