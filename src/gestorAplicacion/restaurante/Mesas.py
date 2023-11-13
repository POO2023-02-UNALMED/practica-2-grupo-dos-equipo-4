import datetime

class Mesas:
    mesas = []

    def __init__(self, idMesa, numeroDeSillas):
        self.idMesa = idMesa
        self.numeroDeSillas = numeroDeSillas
        self.reservaPorCliente = {}
        self.ocupadoEnFecha = {}
        Mesas.mesas.append(self)

    def crearReserva(self, idCliente, idMesa, fecha):
        for mesa in Mesas.mesas:
            if mesa.getIdMesa() == idMesa and fecha not in mesa.reservaPorCliente.values():
                mesa.reservaPorCliente[idCliente] = fecha
                mesa.ocupadoEnFecha[fecha] = False

    def efectuarReserva(self, idCliente, fecha):
        if self.isOcupadoEnFecha(fecha):
            raise Exception("La mesa ya está reservada en esta fecha")
        self.reservaPorCliente.pop(idCliente, None)
        self.ocupadoEnFecha[fecha] = True


    def cancelarReserva(self, idCliente, fecha):
        for mesa in Mesas.mesas:
            if idCliente in mesa.reservaPorCliente and fecha in mesa.ocupadoEnFecha:
                del mesa.reservaPorCliente[idCliente]
                del mesa.ocupadoEnFecha[fecha]

    def __str__(self):
        stringBuilder = []
        stringBuilder.append(f"Mesa número: {self.idMesa}\n")
        stringBuilder.append(f"Número de sillas: {self.numeroDeSillas}\n")
        stringBuilder.append("Está ocupada: ")
        ocupada_fechas = [fecha.strftime("%d/%m/%Y %H:%M:%S") for fecha, ocupada in self.ocupadoEnFecha.items() if ocupada]
        stringBuilder.append(", ".join(ocupada_fechas))
        stringBuilder.append("\n")
        stringBuilder.append("Reservas:\n")
        for idCliente, fecha in self.reservaPorCliente.items():
            fecha_texto = fecha.strftime("%d/%m/%Y %H:%M:%S")  # Formatear la fecha en formato dd/mm/yyyy HH:MM:SS
            stringBuilder.append(f"ID de cliente: {idCliente}, Fecha de reserva: {fecha_texto}\n")
        return ''.join(stringBuilder)

    # Getters and Setters
    @staticmethod
    def getMesas():
        return Mesas.mesas

    def setIdMesa(self, idMesa):
        self.idMesa = idMesa

    def getNumeroDeSillas(self):
        return self.numeroDeSillas

    def setNumeroDeSillas(self, numeroDeSillas):
        self.numeroDeSillas = numeroDeSillas

    def isOcupadoEnFecha(self, fecha):
        return  self.ocupadoEnFecha.get(fecha, False)

    def setOcupadoEnFecha(self, estadoMesa, fecha):
        self.ocupadoEnFecha[fecha] = estadoMesa

    def set(self, key, value):
        self.reservaPorCliente[key] = value

    def getIdMesa(self):
        return self.idMesa

    def getReservaPorCliente(self):
        return self.reservaPorCliente

    def setReservaPorCliente(self, reservaPorCliente):
        self.reservaPorCliente = reservaPorCliente

    def getOcupadoEnFecha(self):
        return self.ocupadoEnFecha

    def setOcupadoEnFecha(self, ocupadoEnFecha):
        self.ocupadoEnFecha = ocupadoEnFecha