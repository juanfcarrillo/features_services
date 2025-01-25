from behave import *
from asyncio import run

from app.Ciudadano import Ciudadano
from app.Reporte import Reporte
from app.TipoReporte import TipoReporte
from domain.RepositorioDeReporteEnMemoria import RepositorioDeReporteEnMemoria

# use_step_matcher("re")

repositorioEnMemoria = RepositorioDeReporteEnMemoria()

ciudadano1 = Ciudadano(
    nombre="Juan Pérez",
    correo="juan.perez@example.com",
    identificacion="1728394857"
)

tipo_reporte1 = TipoReporte(
    asunto="Inundación recurrente",
    descripcion="Reporte de un bache peligroso en una avenida principal."
)

tipo_reporte2 = TipoReporte(
    asunto="Inundación recurrente",
    descripcion="Reporte de un bache en una avenida principal."
)

run(repositorioEnMemoria.agregar_reporte(Reporte(ciudadano1, tipo_reporte1, ubicacion="Avenida Principal", prioridad=2, frecuencia="Recurrente")))
run(repositorioEnMemoria.agregar_reporte(Reporte(ciudadano1, tipo_reporte2, ubicacion="Avenida Principal", prioridad=2, frecuencia="Recurrente")))

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
    run(repositorioEnMemoria.agregar_reporte(context.reporte))

@step("se encuentra registros previos del problema")
def step_impl(context):
    registros_previos = run(repositorioEnMemoria.obtener_reportes_por_asunto(context.tipo_reporte.asunto)) or []
    context.cantidad_reportes = len(registros_previos)

    assert context.cantidad_reportes > 1, "No se encontraron registros previos del problema"


@step('el reporte se asigna con frecuencia "{frecuencia}" y prioridad "{prioridad}"')
def step_impl(context, frecuencia, prioridad):
    run(repositorioEnMemoria.actualziar_prioridad_de_reporte_por_asunto(context.tipo_reporte.asunto, prioridad, frecuencia))


@step("el ciudadano recibe una confirmación del envío del reporte")
def step_impl(context):
    print(
        f"""
                        Hola {context.reporte.get_ciudadano().get_nombre()}:,

                        Hemos recibido tu reporte con los siguientes detalles:
                        Asunto: {context.reporte.get_tipo_reporte().get_asunto()}
                        Descripción: {context.reporte.get_tipo_reporte().get_descripcion()}
                        Ubicación: {context.reporte.get_ubicacion()}

                        Tu reporte ha sido registrado exitosamente con estado: {context.reporte.get_estado_registro()}.

                        Gracias por contribuir a mejorar nuestra comunidad.

                        Atentamente,
                        Equipo de Gestión de Reportes
                        """
    )


@step("no se encuentra registros previos del problema")
def step_impl(context):
    registros_previos = run(repositorioEnMemoria.obtener_reportes_por_asunto(context.tipo_reporte.asunto)) or []
    context.cantidad_reportes = len(registros_previos)

    assert context.cantidad_reportes == 1, "Se encontraron registros previos del problema"