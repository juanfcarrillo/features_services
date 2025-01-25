from app import Reporte
from domain.RepositorioDeReporte import RepositorioDeReporte


class RepositorioDeReporteEnMemoria(RepositorioDeReporte):
    def __init__(self):
        self.baseDeDato = {}

    async def obtener_reportes_por_asunto(self, asunto: str):
        return self.baseDeDato.get(asunto, [])

    async def agregar_reporte(self, reporte: Reporte):
        if reporte.asunto not in self.baseDeDato:
            self.baseDeDato[reporte.asunto] = []
        self.baseDeDato[reporte.asunto].append(reporte)

    async def actualziar_prioridad_de_reporte_por_asunto(self, asunto: str, prioridad: int, frecuencia: str):
        if asunto in self.baseDeDato:
            for report in self.baseDeDato[asunto]:
                report.prioridad = prioridad