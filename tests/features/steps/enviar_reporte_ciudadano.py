from behave import step
from app.models.PublicReport import PublicReport

public_reports = []

@step('un ciudadano ha identificado un problema con tipo "{tipo}", descripción "{descripcion}" y ubicación "{ubicacion}"')
def step_given_problem_details(context, tipo, descripcion, ubicacion):
    context.report = PublicReport(
        report_type=tipo,
        description=descripcion,
        location=ubicacion
    )

@step('un ciudadano intenta enviar un reporte con descripción "{descripcion}" y ubicación "{ubicacion}" pero sin tipo')
def step_given_incomplete_problem_details(context, descripcion, ubicacion):
    context.report = PublicReport(
        report_type=None,
        description=descripcion,
        location=ubicacion
    )

@step('un ciudadano ha permitido al sistema capturar su ubicación automáticamente')
def step_given_auto_geolocation(context):
    context.report.location = "Ubicación geolocalizada automáticamente"

@step('no ha adjuntado ninguna foto como evidencia')
def step_given_no_photo_attached(context):
    context.report.photo = None

@step('ha adjuntado una foto como evidencia "{foto}"')
def step_given_photo_attached(context, foto):
    context.report.photo = foto

@step('el ciudadano envía el reporte al sistema')
def step_when_send_report(context):
    if context.report.is_valid():
        context.report.id = len(public_reports) + 1
        context.report.status = "Pendiente de Revisión"
        public_reports.append(context.report)
    else:
        context.validation_error = "Campos obligatorios faltantes"

@step('el sistema debe asignar un identificador único al reporte')
def step_then_assign_unique_id(context):
    assert context.report.id is not None

@step('registrar el reporte con un estado inicial "Pendiente de Revisión"')
def step_then_register_report(context):
    assert context.report in public_reports
    assert context.report.status == "Pendiente de Revisión"

@step('notificar al ciudadano que el reporte ha sido recibido')
def step_then_notify_citizen(context):
    print(f"Notificación: El reporte #{context.report.id} ha sido recibido con estado {context.report.status}.")

@step('el sistema debe rechazar el reporte')
def step_then_reject_report(context):
    assert context.report not in public_reports

@step('mostrar un mensaje al ciudadano indicando que complete los campos obligatorios')
def step_then_show_error_message(context):
    print(f"Error: {context.validation_error}")

@step('el sistema debe capturar la ubicación geolocalizada del dispositivo')
def step_then_capture_geolocation(context):
    assert context.report.location is not None

@step('un ciudadano ha enviado previamente un reporte con identificador "{id_reporte}"')
def step_given_existing_report(context, id_reporte):
    context.report = next((r for r in public_reports if r.id == int(id_reporte)), None)
    assert context.report is not None

@step('el ciudadano consulta el estado del reporte')
def step_when_check_report_status(context):
    context.report_status = context.report.status

@step('el sistema debe mostrar el estado actual "{estado}"')
def step_then_display_current_status(context, estado):
    assert context.report_status == estado

@step('el reporte ha pasado de "Pendiente de Revisión" a "En Proceso"')
def step_given_report_status_change(context):
    context.report.status = "En Proceso"

@step('el sistema debe notificar al ciudadano sobre el cambio de estado')
def step_then_notify_status_change(context):
    print(f"Notificación: El estado del reporte #{context.report.id} ha cambiado a {context.report.status}.")

@step('mostrar información relevante sobre el progreso del problema')
def step_then_show_progress_info(context):
    print(f"Progreso: El reporte #{context.report.id} está ahora {context.report.status}.")
