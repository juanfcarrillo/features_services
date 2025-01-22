from app.TipoReporte import TipoReporte


class Reporte:
    estado_registro: str
    frecuencia: str
    prioridad: int

    def __init__(self, ciudadano="Anónimo", tipo_reporte: TipoReporte=None, **kwargs):
        if tipo_reporte:
            self.tipo_reporte = tipo_reporte
            self.asunto = tipo_reporte.asunto
            self.prioridad = tipo_reporte.prioridad
        if kwargs.get("descripcion"):
            self.descripcion = kwargs.get("descripcion")
        if kwargs.get("ubicacion"):
            self.ubicacion = kwargs.get("ubicacion")
        if kwargs.get("foto"):
            self.foto = kwargs.get("foto")
        self.ciudadano = ciudadano
        self.frecuencia = "Desconocida"

    def validar_reporte(self) -> bool:
        es_valido = bool(hasattr(self, "asunto") and hasattr(self, "descripcion") and hasattr(self, "ubicacion"))
        return es_valido

    def enviar_reporte(self) -> None:
        es_valido = self.validar_reporte()

        if es_valido:
            self.estado_registro = "registrado"
        else:
            self.estado_registro = "no_registrado"
