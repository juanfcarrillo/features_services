from abc import ABC, abstractmethod

from app.Reporte import Reporte


class RepositorioDeReporte(ABC):
    @abstractmethod
    async def obtener_reportes_por_asunto(self, asunto: str):
        pass

    @abstractmethod
    async def agregar_reporte(self, reporte: Reporte):
        pass

    @abstractmethod
    async def actualziar_prioridad_de_reporte_por_asunto(self, asunto: str, prioridad: int, frecuencia: str):
        pass
