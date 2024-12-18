from behave import *
from app.Reporte import Reporte


@step('que un ciudadano ha proporcionado los siguientes datos: tipo "{tipo}", descripcion "{descripcion}", ubicacion "{ubicacion}", foto "{foto}"')
def step_given_datos_proporcionados(context, tipo, descripcion, ubicacion, foto):
    reporte = Reporte(
        tipo=tipo if tipo != "None" else None,
        descripcion=descripcion if descripcion != "None" else None,
        ubicacion=ubicacion if ubicacion != "None" else None,
        foto=foto if foto != "None" else None,
    )

    context.reporte = reporte

@step('el ciudadano envía el reporte a la entidad municipal')
def step_when_envia_reporte(context):
    context.reporte.enviar_reporte()

@step('la entidad municipal debe procesar el reporte según los datos proporcionados')
def step_then_procesar_reporte(context):
    assert hasattr(context.reporte, 'estado_registro'), "El reporte no fue procesado correctamente."

@step('notificar al ciudadano el "{estado_registro}"')
def step_then_notificar_ciudadano(context, estado_registro):
    assert context.reporte.estado_registro == estado_registro, f"Se esperaba '{estado_registro}' pero se obtuvo '{context.reporte.estado_registro}'."