class Ciudadano:
    def __init__(self, nombre, correo, identificacion):
        self.nombre = nombre
        self.correo = correo
        self.identificacion = identificacion

class Reporte:
    def __init__(self, asunto, descripcion, ubicacion, ciudadano):
        self.asunto = asunto
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.ciudadano = ciudadano

    def enviar(self):
        self.estado = "enviado"
        return f"El reporte con asunto '{self.asunto}' ha sido enviado con éxito."
