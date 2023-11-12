class Mesas:
    mesas = []

    def __init__(self, idMesa, numeroDeSillas):
        self.idMesa = idMesa
        self.numeroDeSillas = numeroDeSillas
        self.reservaPorCliente = {}
        self.ocupadoEnFecha = {}
        Mesas.mesas.append(self)

    @staticmethod
    def crearReserva(idCliente, idMesa, fecha):
        for mesa in Mesas.mesas:
            if mesa.getIdMesa() == idMesa and fecha not in mesa.reservaPorCliente.values():
                mesa.reservaPorCliente[idCliente] = fecha
                mesa.ocupadoEnFecha[fecha] = True

    @staticmethod
    def efectuarReserva(idCliente, fecha):
        for mesa in Mesas.mesas:
            if idCliente in mesa.reservaPorCliente and fecha in mesa.ocupadoEnFecha:
                del mesa.reservaPorCliente[idCliente]
                mesa.ocupadoEnFecha[fecha] = True

    @staticmethod
    def cancelarReserva(idCliente, fecha):
        for mesa in Mesas.mesas:
            if idCliente in mesa.reservaPorCliente and fecha in mesa.ocupadoEnFecha:
                del mesa.reservaPorCliente[idCliente]
                del mesa.ocupadoEnFecha[fecha]

    def __str__(self):
        stringBuilder = []
        stringBuilder.append(f"Mesa número: {self.idMesa}\n")
        stringBuilder.append(f"Número de sillas: {self.numeroDeSillas}\n")
        stringBuilder.append(f"Está ocupada: {list(self.ocupadoEnFecha.keys())}\n")
        stringBuilder.append("Reservas:\n")
        for idCliente, fecha in self.reservaPorCliente.items():
            stringBuilder.append(f"ID de cliente: {idCliente}, Fecha de reserva: {fecha}\n")
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
        return self.ocupadoEnFecha.get(fecha, False)

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
