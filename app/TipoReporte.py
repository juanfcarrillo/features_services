class TipoReporte:
    def __init__(self, asunto, descripcion, prioridad):
        self.asunto = asunto
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"Asunto: {self.asunto}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"