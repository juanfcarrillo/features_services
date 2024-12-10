class Calendario:
    def __init__(self):
        self.reservas = {}
        self.espacios_disponibles = {
            "2024-12-15 10:00": "Disponible",
            "2024-12-15 11:00": "Disponible"
        }

    def agregar_reserva(self, fecha_horario, detalles_evento):
        reserva_id = f"RES-{len(self.reservas) + 1}"
        self.reservas[reserva_id] = {
            "fecha_horario": fecha_horario,
            "detalles": detalles_evento,
            "estado": "Pendiente de Aprobación"
        }
        self.bloquear_horario(fecha_horario)
        return reserva_id

    def bloquear_horario(self, fecha_horario):
        if fecha_horario in self.espacios_disponibles:
            self.espacios_disponibles[fecha_horario] = "En Proceso"

    @staticmethod
    def mostrar_notificacion(reserva_id):
        return f"La reserva con ID {reserva_id} está 'Pendiente de Aprobación'."
