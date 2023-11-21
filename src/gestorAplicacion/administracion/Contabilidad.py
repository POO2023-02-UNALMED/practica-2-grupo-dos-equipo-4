from src.errorAplicacion.ErrorAdministracion import ErroresAdministracion
from src.gestorAplicacion.administracion import Empleado
from src.gestorAplicacion.administracion.Cocinero import Cocinero
from src.gestorAplicacion.administracion.Mesero import Mesero


class Contabilidad:
    saldo = 1000000
    utilidades = 0
    ingresos = 500000
    sueldos = 0
    gastos = 0
    serviciosPublicos = 50000

    def __init__(self):
        Contabilidad.utilidades = 0
        Contabilidad.ingresos = 0
        Contabilidad.sueldos = 0
        Contabilidad.gastos = 0
        Contabilidad.serviciosPublicos = 0

    @staticmethod
    def pagarServicios():
        try:
            if Contabilidad.serviciosPublicos> Contabilidad.saldo:
                raise ErroresAdministracion("saldo_insuficiente")
            Contabilidad.saldo -= Contabilidad.serviciosPublicos
            Contabilidad.gastos += Contabilidad.serviciosPublicos
        except ErroresAdministracion as e:
            e.manejo_error()
            #return "se pagaron: " + str(Contabilidad.getServiciosPublicos()) + " de servicios públicos"

    @staticmethod
    def sumarIngresosPedidoAlSaldo(ingreso):
        Contabilidad.saldo += ingreso
        Contabilidad.ingresos += ingreso

    @staticmethod
    def calcularUtilidades(ganancia, neto):
        Contabilidad.utilidades = ganancia + neto


    @staticmethod
    def pagarSueldos():
        try:
            totalPago = 0
            for mesero in Mesero.empleados:
                totalPago += mesero.getSalario()
                if mesero.bono():
                    totalPago += mesero.getSalario() * (15 / 100)
            if totalPago > Contabilidad.saldo:
                raise ErroresAdministracion("saldo_insuficiente")
            Contabilidad.saldo -= totalPago
            Contabilidad.gastos += totalPago
            return totalPago

        except ErroresAdministracion as e:
            e.manejo_error()

    @staticmethod
    def calcularGastos():
        Contabilidad.gastos += Contabilidad.pagarSueldos() + Contabilidad.pagarServicios()
        return Contabilidad.gastos

    @staticmethod
    def setSaldo(saldo):
        Contabilidad.saldo = saldo

    @staticmethod
    def getUtilidades():
        return Contabilidad.utilidades

    @staticmethod
    def setUtilidades(utilidades):
        Contabilidad.utilidades = utilidades

    @staticmethod
    def getIngresos():
        return Contabilidad.ingresos

    @staticmethod
    def setIngresos(ingresos):
        Contabilidad.ingresos = ingresos

    @staticmethod
    def getSueldos():
        return Contabilidad.sueldos

    @staticmethod
    def setSueldos(sueldos):
        Contabilidad.sueldos = sueldos

    @staticmethod
    def getGastos():
        return Contabilidad.gastos
    def setGastos(self, gasto):
        Contabilidad.gastos += gasto

    @staticmethod
    def setServiciosPublicos(servicios):
        Contabilidad.serviciosPublicos = servicios
    @staticmethod
    def getServiciosPublicos():
        return Contabilidad.serviciosPublicos
