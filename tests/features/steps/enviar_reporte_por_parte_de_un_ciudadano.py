from behave import *

from app.Ciudadano import Ciudadano
from app.Reporte import Reporte
from app.TipoReporte import TipoReporte
from domain.GestorReportes import GestorReportes


# use_step_matcher("re")

ciudadano1 = Ciudadano(nombre="Marco Sanchez", correo="marco.sanchez@example.com", identificacion="2547896321")
ciudadano2 = Ciudadano(nombre="María López", correo="maria.lopez@example.com", identificacion="0987654321")

tipo_reporte1 = TipoReporte(asunto="Inundación recurrente",
                                descripcion="La calle principal se inunda cada vez que llueve.")
tipo_reporte2 = TipoReporte(asunto="Inundación recurrente",
                                descripcion="El parque central siempre se inunda en temporada de lluvias.")

reporte1 = Reporte(ciudadano=ciudadano1, tipo_reporte=tipo_reporte1, ubicacion="Calle Principal #123")
reporte2 = Reporte(ciudadano=ciudadano2, tipo_reporte=tipo_reporte2, ubicacion="Parque Central")

GestorReportes.enviar_reporte(reporte1)
GestorReportes.enviar_reporte(reporte2)


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
    GestorReportes.enviar_reporte(context.reporte)


@step("se encuentra registros previos del problema")
def step_impl(context):
    asunto_actual = context.reporte.get_tipo_reporte().get_asunto()
    registros_previos = GestorReportes.buscar_por_asunto(asunto_actual)
    assert len(registros_previos) > 1, "No se encontraron registros previos del problema."


@step('el reporte se asigna con frecuencia "{frecuencia}" y prioridad "{prioridad}"')
def step_impl(context, frecuencia, prioridad):
    context.reporte.set_frecuencia(frecuencia)
    context.reporte.set_prioridad(prioridad)
    GestorReportes.actualizar_reporte(context.reporte)


@step("el ciudadano recibe una confirmación del envío del reporte")
def step_impl(context):
    if context.reporte.get_estado_registro() == "registrado":
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
    else:
        raise AssertionError("El reporte no está registrado. No se puede enviar el correo.")


@step("no se encuentra registros previos del problema")
def step_impl(context):
    asunto_actual = context.reporte.get_tipo_reporte().get_asunto()
    registros_previos = GestorReportes.buscar_por_asunto(asunto_actual)
    assert len(registros_previos) == 1, "Se encontraron registros previos del problema."