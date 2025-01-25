from app.Reporte import Reporte
from domain.RepositorioDeReporte import RepositorioDeReporte


class ServicioDeReporte:
    def __init__(self, reporte_repositorio: RepositorioDeReporte):
        self.reporte_repositorio = reporte_repositorio

    async def priorizar(self, reporte: Reporte):
        reportes_previos = await self.reporte_repositorio.obtener_reportes_por_asunto(reporte.tipo_reporte.asunto) or []
        cantidad_reportes = len(reportes_previos)

        if cantidad_reportes >= 5:
            reporte.prioridad(1)
            reporte.frecuencia("Recurrente")
        else:
            reporte.prioridad(5)
            reporte.frecuencia("Único")

        await self.reporte_repositorio.actualziar_prioridad_de_reporte_por_asunto(reporte.tipo_reporte.asunto, reporte.prioridad, reporte.frecuencia)

    async def enviar_reporte(self, reporte: Reporte):
        if not reporte.validar_reporte():
            raise ValueError("El reporte no es válido.")
        await self.reporte_repositorio.agregar_reporte(reporte)