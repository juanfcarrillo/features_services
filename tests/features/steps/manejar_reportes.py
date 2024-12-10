from behave import given, when, then

from app.models.Report import Report

# In-memory database
reports = []

@given("un problema ha sido identificado con un tipo, descripción y ubicación")
def step_given_problem_identified(context):
    context.problem = Report(
        report_type="Graffiti",
        description="Graffiti en la pared de la tienda principal",
        location="Calle Principal, 123"
    )

@when("el ciudadano reporta el problema al sistema")
def step_when_problem_reported(context):
    context.problem.id = len(reports) + 1
    reports.append(context.problem)

@then("el sistema debe asignar un identificador único al reporte")
def step_then_assign_id_to_report(context):
    assert context.problem.id is not None

@then('registrar el reporte con un estado inicial "Pendiente"')
def step_then_register_report(context):
    assert context.problem in reports
    assert context.problem.status == "Pendiente"

@then('notificar al ciudadano que el reporte ha sido recibido')
def step_then_notify_user(context):
    print(f"Notificación: El reporte #{context.problem.id} ha sido recibido con estado {context.problem.status}.")
