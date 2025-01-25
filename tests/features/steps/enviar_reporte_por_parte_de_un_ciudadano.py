from behave import *
from faker.proxy import Faker

from app.Ciudadano import Ciudadano
from app.Reporte import Reporte
from app.TipoReporte import TipoReporte
from domain.RepositorioDeReporteEnMemoria import RepositorioDeReporteEnMemoria
from domain.ServicioDeReporte import ServicioDeReporte

repositorioEnMemoria = RepositorioDeReporteEnMemoria()
servicioDeReporte = ServicioDeReporte(repositorioEnMemoria)

def generar_registros(repositorio ,cantidad_registro, asunto):
    fake = Faker()

    for _ in range(int(cantidad_registro)):
        ciudadano = Ciudadano(nombre=fake.name(), identificacion=fake.ssn(), correo=fake.email())
        tipo_reporte = TipoReporte(asunto=asunto, descripcion=fake.text())
        reporte = Reporte(ciudadano=ciudadano, tipo_reporte=tipo_reporte, ubicacion=fake.address())
        reporte.prioridad = fake.random_int(min=1, max=5)

        repositorio.agregar_reporte(reporte)

@step(
    'que un ciudadano llamado "{nombre}" con correo "{correo}" e identificación "{identificacion}" ha identificado un problema')
def step_impl(context, nombre, correo, identificacion):
    context.ciudadano = Ciudadano(nombre, correo, identificacion)


@step(
    'proporciona sus detalles en un reporte con asunto "{asunto}", descripción "{descripcion}" y ubicación "{ubicacion}"')
def step_impl(context, asunto, descripcion, ubicacion):
    context.tipo_reporte = TipoReporte(asunto, descripcion)
    context.reporte = Reporte(context.ciudadano, context.tipo_reporte, ubicacion=ubicacion)

@step("se envía el reporte descrito")
def step_impl(context):
    servicioDeReporte.enviar_reporte(context.reporte)

@step('se asigna una prioridad de acuerdo a "{cantidad_registro}" registros previos del problema con asunto "{asunto}"')
def step_impl(context, cantidad_registro, asunto):
    generar_registros(repositorioEnMemoria, cantidad_registro, asunto)
    context.reporte = servicioDeReporte.priorizar(context.reporte)

@step('el reporte es asignado con prioridad "{prioridad_esperada}"')
def step_impl(context, prioridad_esperada):
    assert int(prioridad_esperada) == context.reporte.prioridad
