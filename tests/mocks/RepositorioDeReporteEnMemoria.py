from faker.proxy import Faker

from app.models.Reporte import Reporte
from app.models.Ciudadano import Ciudadano
from app.models.RepositorioDeReporte import RepositorioDeReporte
from app.models.TipoReporte import TipoReporte


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



def generar_registros(repositorio ,cantidad_registro, asunto):
    fake = Faker()

    for _ in range(int(cantidad_registro)):
        ciudadano = Ciudadano(nombre=fake.name(), identificacion=fake.ssn(), correo=fake.email())
        tipo_reporte = TipoReporte(asunto=asunto, descripcion=fake.text())
        reporte = Reporte(ciudadano=ciudadano, tipo_reporte=tipo_reporte, ubicacion=fake.address())
        reporte.prioridad = fake.random_int(min=1, max=5)

        repositorio.agregar_reporte(reporte)
