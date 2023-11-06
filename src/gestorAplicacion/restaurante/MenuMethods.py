from abc import ABC, abstractmethod

class MenuMethods(ABC):

    @staticmethod
    @abstractmethod
    def mostrarMenuComidas():
        pass

    @staticmethod
    @abstractmethod
    def mostrarMenuGaseosas():
        pass
