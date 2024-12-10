from behave import *
from app.modelos import ActividadGrupal, PlataformaActividades

@step('que un ciudadano desea organizar una nueva actividad grupal')
def step_impl(context):
    context.plataforma = PlataformaActividades()
    context.actividad = None

@step('proporciona el título de la actividad "{titulo}"')  # Nombre único
def step_impl(context, titulo):
    context.titulo_actividad = titulo

@step('selecciona la ubicación de la actividad grupal "{ubicacion}"')  # Nombre único
def step_impl(context, ubicacion):
    context.ubicacion = ubicacion

@step('establece la fecha de la actividad grupal "{fecha}"')  # Nombre único
def step_impl(context, fecha):
    context.fecha = fecha

@step('envía invitaciones para la actividad a "{cantidad_invitados:d}" personas')  # Nombre único
def step_impl(context, cantidad_invitados):
    context.cantidad_invitados = cantidad_invitados

@step('publica la actividad grupal')
def step_impl(context):
    context.actividad = ActividadGrupal(
        titulo=context.titulo_actividad,
        ubicacion=context.ubicacion,
        fecha=context.fecha,
        invitados=context.cantidad_invitados
    )
    context.plataforma.organizar_actividad(context.actividad)

@step('la actividad grupal "{titulo}" aparecerá en la lista de actividades disponibles')
def step_impl(context, titulo):
    actividades_grupales = context.plataforma.listar_actividades()
    assert any(actividad.titulo == titulo for actividad in actividades_grupales), \
        f"La actividad grupal '{titulo}' no se encuentra en la lista de actividades disponibles."
