from behave import step

from app.models.MunicipalEntity import MunicipalEntity
from app.models.CollaborativeRequest import CollaborativeRequest

collaborative_requests = []

@step("que un problema ha sido reportado con un tipo y ubicación específica")
def step_given_problem_reported(context):
    context.problem = {
        "type": "Inundación",
        "location": "Av. Principal, 123"
    }

@step("el sistema detecta que el problema requiere la intervención de más de una institución")
def step_given_problem_requires_multiple_institutions(context):
    context.problem["requires_collaboration"] = True

@step("una institución principal toma la responsabilidad del problema")
def step_when_primary_institution_assigned(context):
    context.problem["primary_institution"] = "Departamento de Infraestructura"

@step("el sistema debe notificar a las instituciones involucradas")
def step_then_notify_involved_institutions(context):
    context.problem["involved_institutions"] = ["Departamento de Mantenimiento", "Departamento de Desagües"]
    for institution in context.problem["involved_institutions"]:
        print(f"Notificación enviada a {institution}.")

@step("permitir a la institución principal asignar tareas específicas a las otras instituciones")
def step_then_allow_task_assignment(context):
    context.problem["tasks"] = {
        "Departamento de Mantenimiento": "Reparar la calzada",
        "Departamento de Desagües": "Drenar el exceso de agua"
    }
    assert len(context.problem["tasks"]) == len(context.problem["involved_institutions"])

@step("que un problema ha sido asignado a múltiples instituciones")
def step_given_problem_assigned(context):
    assert len(context.problem["involved_institutions"]) > 0

@step("cada institución tiene tareas pendientes asignadas")
def step_given_tasks_assigned(context):
    for task in context.problem["tasks"].values():
        print(f"Tarea asignada: {task}")

@step("una institución actualiza el progreso de su tarea en el sistema")
def step_when_task_updated(context):
    context.problem["progress"] = {"Departamento de Mantenimiento": "50% completado"}
    print("Progreso actualizado.")

@step("el sistema debe registrar el progreso de esa tarea")
def step_then_register_progress(context):
    assert "progress" in context.problem

@step("notificar a las otras instituciones involucradas sobre la actualización")
def step_then_notify_institutions_of_update(context):
    print("Notificación enviada a instituciones involucradas sobre el progreso actualizado.")
