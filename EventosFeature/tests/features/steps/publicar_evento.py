from behave import *
from app.modelos import Evento, PlataformaEventos

@step('que un ciudadano desea crear un nuevo evento')
def step_impl(context):
    context.plataforma = PlataformaEventos()
    context.evento = None

@step('proporciona el título del evento "{titulo}"')
def step_impl(context, titulo):
    context.titulo_evento = titulo

@step('establece la fecha del evento "{fecha}"')  # Nombre único
def step_impl(context, fecha):
    context.fecha = fecha

@step('selecciona la ubicación del evento "{ubicacion}"')  # Nombre único
def step_impl(context, ubicacion):
    context.ubicacion = ubicacion

@step('escribe una descripción para el evento "{descripcion}"')  # Nombre único
def step_impl(context, descripcion):
    context.descripcion = descripcion

@step('publica el evento')
def step_impl(context):
    context.evento = Evento(
        titulo=context.titulo_evento,
        fecha=context.fecha,
        ubicacion=context.ubicacion,
        descripcion=context.descripcion
    )
    context.plataforma.publicar_evento(context.evento)

@step('el evento "{titulo}" aparecerá en la lista de eventos públicos')
def step_impl(context, titulo):
    eventos_publicos = context.plataforma.listar_eventos()
    assert any(evento.titulo == titulo for evento in eventos_publicos), \
        f"El evento '{titulo}' no se encuentra en la lista de eventos públicos."
