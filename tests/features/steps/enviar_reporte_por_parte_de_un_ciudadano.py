from behave import *

from app.Ciudadano import Ciudadano
from app.Reporte import Reporte
from app.TipoReporte import TipoReporte


# use_step_matcher("re")


@step(
    'que un ciudadano llamado "{nombre}" con correo "{correo}" e identificación "{identificacion}" ha identificado un problema')
def step_impl(context, nombre, correo, identificacion):
    context.ciudadano = Ciudadano(nombre, correo, identificacion)

@step(
    'proporciona sus detalles en un reporte con asunto "{asunto}", descripción "{descripcion}" y ubicación "{ubicacion}"')
def step_impl(context, asunto, descripcion, ubicacion):
    context.reporte = Reporte(
        ciudadano=context.ciudadano,
        tipo=TipoReporte(asunto, descripcion, 0),
        descripcion=descripcion,
        ubicacion=ubicacion,
    )


@step("se envía el reporte descrito")
def step_impl(context):
    if context.reporte.validar_reporte():
        context.reporte.enviar_reporte()
    else:
        raise ValueError("El reporte tiene información incompleta.")


@step("se encuentra registros previos del problema")
def step_impl(context):
    context.reporte.asignar_frecuencia_y_prioridad()
    if context.reporte.frecuencia == "Desconocida":
        raise ValueError("No se pudo asignar frecuencia al reporte.")


@step('el reporte se asigna con frecuencia "{frecuencia}" y prioridad "{prioridad}"')
def step_impl(context, frecuencia, prioridad):
    assert context.reporte.frecuencia == frecuencia
    assert str(context.reporte.prioridad) == prioridad


@step("el ciudadano recibe una confirmación del envío del reporte")
def step_impl(context):
    assert context.reporte.estado_registro == "registrado"


@step("no se encuentra registros previos del problema")
def step_impl(context):
    context.reporte.frecuencia = "Nuevo"
    context.reporte.prioridad = 4
