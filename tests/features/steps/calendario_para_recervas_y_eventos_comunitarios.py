from behave import *

# use_step_matcher("re")

@step("un ciudadano visualiza los espacios disponibles en el calendario comunitario")
def step_impl(context):
    context.calendario = {}
    context.espacios_disponibles = {
        "2024-12-15 10:00": "Disponible",
        "2024-12-15 11:00": "Disponible"
    }


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
    reserva_id = f"RES-{len(context.calendario) + 1}"
    context.calendario[reserva_id] = {
        "fecha_horario": context.fecha_horario,
        "detalles": context.detalles_evento,
        "estado": "Pendiente de Aprobación"
    }
    context.reserva_id = reserva_id


@step('bloquea el horario en el calendario como "En Proceso"')
def step_impl(context):
    if context.fecha_horario in context.espacios_disponibles:
        context.espacios_disponibles[context.fecha_horario] = "En Proceso"


@step("notifica al ciudadano sobre la reserva.")
def step_impl(context):
    print(f"Notificación: La reserva con ID {context.reserva_id} está 'Pendiente de Aprobación'.")