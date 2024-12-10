class Evento:
    def __init__(self, titulo, fecha, ubicacion, descripcion):
        self.titulo = titulo
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.descripcion = descripcion

class PlataformaEventos:
    def __init__(self):
        self.eventos_publicos = []

    def publicar_evento(self, evento):
        self.eventos_publicos.append(evento)

    def listar_eventos(self):
        return self.eventos_publicos

class ActividadGrupal:
    def __init__(self, titulo, ubicacion, fecha, invitados):
        self.titulo = titulo
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.invitados = invitados

class PlataformaActividades:
    def __init__(self):
        self.actividades_grupales = []

    def organizar_actividad(self, actividad):
        self.actividades_grupales.append(actividad)

    def listar_actividades(self):
        return self.actividades_grupales
