from behave import step

from app.models.MunicipalEntity import MunicipalEntity
from app.models.CollaborativeRequest import CollaborativeRequest

collaborative_requests = []

@step("un problema interinstitucional ha sido identificado con un tipo, descripción y ubicación")
def step_given_interinstitutional_problem(context):
    context.request = CollaborativeRequest(
        request_type="Inundación",
        description="Hay una inundación que requiere tanto mantenimiento vial como gestión de desagües",
        location="Av. Amazonas, 123"
    )

@step("una institución municipal toma la responsabilidad principal del problema")
def step_when_primary_entity_assigned(context):
    context.primary_entity = MunicipalEntity(name="Departamento de Infraestructura")
    context.request.primary_entity = context.primary_entity

@step("el sistema notifica a las instituciones involucradas")
def step_then_notify_institutions(context):
    context.involved_entities = [
        MunicipalEntity(name="Departamento de Mantenimiento Vial"),
        MunicipalEntity(name="Departamento de Gestión de Desagües")
    ]
    context.request.involved_entities = context.involved_entities
    for entity in context.involved_entities:
        print(f"Notificación: El {entity.name} ha sido asignado al problema #{context.request.id}.")

@step("el sistema permite asignar tareas específicas a las instituciones involucradas")
def step_then_assign_tasks(context):
    context.request.tasks = {
        "Departamento de Mantenimiento Vial": "Reparar la vía dañada",
        "Departamento de Gestión de Desagües": "Drenar el exceso de agua"
    }
    for entity, task in context.request.tasks.items():
        print(f"Tarea asignada: {entity} debe {task}.")

@step("el sistema registra el problema con un estado inicial \"En Proceso de Colaboración\"")
def step_then_register_collaborative_request(context):
    context.request.id = len(collaborative_requests) + 1
    context.request.status = "En Proceso de Colaboración"
    collaborative_requests.append(context.request)
    assert context.request in collaborative_requests
    assert context.request.status == "En Proceso de Colaboración"
    print(f"Problema #{context.request.id} registrado con estado: {context.request.status}.")
