class Ciudadano:
    def __init__(self, nombre, correo, identificacion):
        self.nombre = nombre
        self.correo = correo
        self.identificacion = identificacion

class InstitucionMunicipal:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.reportes = []  # Lista para almacenar los reportes

    def recibir_reporte(self, reporte):
        self.reportes.append(reporte)  # Guardar el reporte en la lista
        return f"La institución {self.nombre} ha recibido el reporte con asunto '{reporte.asunto}'."

    def listar_reportes(self):
        return [f"Asunto: {reporte.asunto}, Ciudadano: {reporte.ciudadano.nombre}" for reporte in self.reportes]

class Reporte:
    def __init__(self, asunto, descripcion, ubicacion, ciudadano, institucion):
        self.asunto = asunto
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.ciudadano = ciudadano
        self.institucion = institucion
        self.estado = "pendiente"

    def enviar(self):
        self.estado = "enviado"
        notificacion_ciudadano = f"El reporte con asunto '{self.asunto}' ha sido enviado con éxito."
        notificacion_institucion = self.institucion.recibir_reporte(self)
        return notificacion_ciudadano, notificacion_institucion
