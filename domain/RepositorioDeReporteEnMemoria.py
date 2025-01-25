from app import Reporte
from domain.RepositorioDeReporte import RepositorioDeReporte


class RepositorioDeReporteEnMemoria(RepositorioDeReporte):
    def __init__(self):
        self.baseDeDato = {}

    def obtener_reportes_por_asunto(self, asunto: str):
        return self.baseDeDato.get(asunto, [])

    def agregar_reporte(self, reporte: Reporte):
        if reporte.tipo_reporte.asunto not in self.baseDeDato:
            self.baseDeDato[reporte.tipo_reporte.asunto] = []
        self.baseDeDato[reporte.tipo_reporte.asunto].append(reporte)

    def actualziar_prioridad_de_reporte_por_asunto(self, asunto: str, prioridad: int):
        if asunto in self.baseDeDato:
            for report in self.baseDeDato[asunto]:
                report.prioridad = prioridad