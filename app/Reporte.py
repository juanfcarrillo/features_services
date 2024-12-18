class Reporte:
    estado_registro: str
    def __init__(self, tipo, descripcion, ubicacion, foto, ciudadano="Anónimo"):
        self.tipo = tipo
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.foto = foto
        self.ciudadano = ciudadano

    def validar_reporte(self) -> bool:
        es_valido = bool(self.tipo.strip() and self.descripcion.strip() and self.ubicacion.strip())
        return es_valido

    def enviar_reporte(self) -> None:
        es_valido = self.validar_reporte()

        if es_valido:
            self.estado_registro = "registrado"
        else:
            self.estado_registro = "no_registrado"