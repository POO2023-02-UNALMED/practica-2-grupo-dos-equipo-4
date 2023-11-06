from src.gestorAplicacion.administracion import Empleado


class Contabilidad:
    saldo = 1000000
    utilidades = 0
    ingresos = 0
    sueldos = 0
    gastos = 0
    serviciosPublicos = 0

    def __init__(self):
        Contabilidad.utilidades = 0
        Contabilidad.ingresos = 0
        Contabilidad.sueldos = 0
        Contabilidad.gastos = 0
        Contabilidad.serviciosPublicos = 0

    @staticmethod
    def pagarServicios():
        Contabilidad.saldo -= Contabilidad.serviciosPublicos
        return Contabilidad.saldo

    @staticmethod
    def sumarIngresosPedidoAlSaldo(ingreso):
        Contabilidad.saldo += ingreso
        Contabilidad.ingresos += ingreso

    @staticmethod
    def calcularUtilidades(ganancia, neto):
        Contabilidad.utilidades = ganancia + neto

    @staticmethod
    def pagarSueldos():
        totalPago = 0
        for empleado in Empleado.Empleado.empleados():
            totalPago += empleado.getSalario()
            if empleado.bono() == True:
                totalPago += empleado.getSalario() * (15 / 100)
            else:
                totalPago += empleado.getSalario()
        Contabilidad.saldo -= totalPago
        return totalPago

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

    @staticmethod
    def setGastos(gastos):
        Contabilidad.gastos += gastos
