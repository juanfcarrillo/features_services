class Reporte:
    estado_registro: str
    def __init__(self, ciudadano="Anónimo", **kwargs):
        if kwargs.get("tipo"):
            self.tipo = kwargs.get("tipo")
        if kwargs.get("descripcion"):
            self.descripcion = kwargs.get("descripcion")
        if kwargs.get("ubicacion"):
            self.ubicacion = kwargs.get("ubicacion")
        if kwargs.get("foto"):
            self.foto = kwargs.get("foto")
        self.ciudadano = ciudadano

    def validar_reporte(self) -> bool:
        es_valido = bool(hasattr(self, "tipo") and hasattr(self, "descripcion") and hasattr(self, "ubicacion"))
        return es_valido

    def enviar_reporte(self) -> None:
        es_valido = self.validar_reporte()

        if es_valido:
            self.estado_registro = "registrado"
        else:
            self.estado_registro = "no_registrado"