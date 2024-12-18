from behave import *
from app.Reporte import Reporte


@step('que un ciudadano ha proporcionado los siguientes datos:')
def step_given_datos_proporcionados(context):
    reporte_datos = {}
    for row in context.table:
        reporte_datos[row['Campo']] = row['Valor']

    reporte = Reporte(
        tipo=reporte_datos.get('Tipo', '').strip(),
        descripcion=reporte_datos.get('Descripcion', '').strip(),
        ubicacion=reporte_datos.get('Ubicacion', '').strip(),
        foto=reporte_datos.get('Foto', '').strip(),
    )

    context.reporte = reporte

@step('el ciudadano envía el reporte a la entidad municipal')
def step_when_envia_reporte(context):
    context.reporte.enviar_reporte()

@step('la entidad municipal debe procesar el reporte según los datos proporcionados')
def step_then_procesar_reporte(context):
    assert hasattr(context, 'estado_registro'), "El reporte no fue procesado correctamente."

@step('notificar al ciudadano el "{estado_registro}"')
def step_then_notificar_ciudadano(context, estado_registro):
    assert context.estado_registro == estado_registro, f"Se esperaba '{estado_registro}' pero se obtuvo '{context.estado_registro}'."
