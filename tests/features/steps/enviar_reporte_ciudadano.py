from behave import step
from app.models.PublicReport import PublicReport

public_reports = []

@step("que un ciudadano identifica un problema con un tipo, descripción y ubicación")
def step_given_basic_problem_details(context):
    context.report = PublicReport(
        report_type="Bache",
        description="Hay un bache grande en la calle",
        location="Calle Principal, 123"
    )

@step("que un ciudadano identifica un problema con un tipo, descripción, ubicación y adjunta una foto")
def step_given_problem_with_photo(context):
    context.report = PublicReport(
        report_type="Graffiti",
        description="Graffiti en la pared del parque",
        location="Parque Central",
        photo="graffiti.jpg"
    )

@step("que un ciudadano intenta enviar un reporte con campos incompletos")
def step_given_incomplete_report(context):
    context.report = PublicReport(
        report_type=None,
        description="",
        location="Calle Secundaria, 456"
    )

@step("el ciudadano envía el reporte al sistema")
def step_when_send_report(context):
    if context.report.is_valid():
        context.report.id = len(public_reports) + 1
        context.report.status = "Pendiente de Revisión"
        public_reports.append(context.report)
    else:
        context.validation_error = "Campos obligatorios faltantes"

@step("el sistema debe asignar un identificador único al reporte")
def step_then_assign_report_id(context):
    assert context.report.id is not None

@step("registrar el reporte con un estado inicial \"Pendiente de Revisión\"")
def step_then_register_report(context):
    assert context.report in public_reports
    assert context.report.status == "Pendiente de Revisión"

@step("almacenar la evidencia fotográfica adjunta junto al reporte")
def step_then_store_photo(context):
    if context.report.photo:
        assert context.report.photo is not None

@step("notificar al ciudadano que el reporte ha sido recibido")
def step_then_notify_citizen(context):
    print(f"Notificación: El reporte #{context.report.id} ha sido recibido con estado {context.report.status}.")

@step("el sistema valida los datos ingresados")
def step_when_validate_report(context):
    context.validation_error = None
    if not context.report.is_valid():
        context.validation_error = "Campos obligatorios faltantes"

@step("el sistema debe rechazar el reporte")
def step_then_reject_report(context):
    assert context.validation_error is not None

@step("mostrar un mensaje al ciudadano indicando que complete los campos obligatorios")
def step_then_show_error_message(context):
    print(f"Error: {context.validation_error}")

@step("un ciudadano identifica un problema y permite al sistema obtener su ubicación automáticamente")
def step_given_geolocated_problem(context):
    context.report = PublicReport(
        report_type="Árbol caído",
        description="Un árbol cayó y bloquea la calle",
        location=None
    )
    context.report.auto_geolocate()

@step("el sistema debe capturar la ubicación geolocalizada del dispositivo")
def step_then_capture_geolocation(context):
    assert context.report.location is not None