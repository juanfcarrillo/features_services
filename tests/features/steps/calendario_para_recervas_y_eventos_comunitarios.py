from behave import *

from app.models.Calendario import Calendario

# use_step_matcher("re")
calendario = Calendario()

@step("un ciudadano visualiza los espacios disponibles en el calendario comunitario")
def step_impl(context):
    context.espacios_disponibles = calendario.espacios_disponibles


@step("selecciona una fecha, horario y completa los detalles del evento")
def step_impl(context):
    context.fecha_horario = "2024-12-15 10:00"
    context.detalles_evento = {
        "tipo": "Reunión",
        "descripcion": "Reunión de planificación",
        "propósito": "Definir actividades para 2025"
    }


@step('el sistema registra la reserva como "Pendiente de Aprobación"')
def step_impl(context):
    context.reserva_id = calendario.agregar_reserva(context.fecha_horario, context.detalles_evento)

@step('bloquea el horario en el calendario como "En Proceso"')
def step_impl(context):
    pass


@step("notifica al ciudadano sobre la reserva.")
def step_impl(context):
    mensaje = calendario.mostrar_notificacion(context.reserva_id)
    print(mensaje)