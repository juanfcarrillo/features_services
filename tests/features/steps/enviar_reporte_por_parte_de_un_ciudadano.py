from behave import *
from app.modelos import *

# use_step_matcher("re")

@step('que un ciudadano llamado "{nombre}" con correo "{correo}" e identificación "{identificacion}" está en comunicación con un asistente')
def step_impl(context, nombre, correo, identificacion):
    context.ciudadano = Ciudadano(nombre, correo, identificacion)
    assert context.ciudadano is not None, "El ciudadano no fue creado correctamente."

@step('una institución municipal llamada "{nombre}" con email "{email}"')
def step_impl(context, nombre, email):
    context.institucion = InstitucionMunicipal(nombre, email)
    assert context.institucion is not None, "La institución no fue creada correctamente."

@step('el ciudadano proporciona un reporte con asunto "{asunto}", descripción "{descripcion}" y ubicación "{ubicacion}"')
def step_impl(context, asunto, descripcion, ubicacion):
    context.asunto = asunto
    context.descripcion = descripcion
    context.ubicacion = ubicacion
    assert all([context.asunto, context.descripcion, context.ubicacion]), "Faltan detalles en el reporte."

@step("el cidudadano termina de dar los detalles y se envía el reporte")
def step_impl(context):
    context.reporte = Reporte(context.asunto, context.descripcion, context.ubicacion, context.ciudadano, context.institucion)
    context.resultado_ciudadano, context.resultado_institucion = context.reporte.enviar()

@step("se notifica al ciudadano que el reporte fue enviado con éxito")
def step_impl(context):
    assert context.resultado_ciudadano == f"El reporte con asunto '{context.asunto}' ha sido enviado con éxito.", "La notificación al ciudadano no es correcta."

@step("la institución municipal recibe y guarda el reporte")
def step_impl(context):
    # Validar que la institución haya recibido y almacenado el reporte
    assert context.reporte in context.institucion.reportes, "El reporte no fue almacenado en la institución."
    esperado = f"La institución {context.reporte.institucion.nombre} ha recibido el reporte con asunto '{context.asunto}'."
    assert context.resultado_institucion == esperado, "La institución no recibió el reporte correctamente."