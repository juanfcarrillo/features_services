from behave import *
from app.modelos import *

# use_step_matcher("re")


@step('que un ciudadano llamado "{nombre}" con correo "{correo}" e identificación "{identificacion}" está en comunicación con un asistente')
def step_impl(context, nombre, correo, identificacion):
    context.ciudadano = Ciudadano(nombre, correo, identificacion)
    assert context.ciudadano is not None, "El ciudadano no fue creado correctamente."


@step('el ciudadano proporciona un asunto "{asunto}"')
def step_impl(context, asunto):
    context.asunto = asunto
    assert context.asunto, "El asunto no puede estar vacío."


@step('detalla la descripción "{descripcion}"')
def step_impl(context, descripcion):
    context.descripcion = descripcion
    assert context.descripcion, "La descripción no puede estar vacía."


@step('proporciona la ubicación "{ubicacion}"')
def step_impl(context, ubicacion):
    context.ubicacion = ubicacion
    assert context.ubicacion, "La ubicación no puede estar vacía."


@step("el cidudadano termina de dar los detalles y se envía el reporte")
def step_impl(context):
    context.reporte = Reporte(context.asunto, context.descripcion, context.ubicacion, context.ciudadano)
    context.resultado = context.reporte.enviar()


@step("se notifica al ciudadano que el reporte fue enviado con éxito")
def step_impl(context):
    assert context.resultado == f"El reporte con asunto '{context.asunto}' ha sido enviado con éxito.", "La notificación no es correcta."