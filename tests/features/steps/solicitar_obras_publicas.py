from behave import step

from app.models.PublicWorkRequest import PublicWorkRequest

public_works_requests = []

@step("una necesidad de infraestructura ha sido identificada con un tipo, descripción y ubicación")
def step_given_infrastructure_need(context):
    context.request = PublicWorkRequest(
        request_type="Parque infantil",
        description="Necesitamos un parque infantil en este terreno vacío",
        location="Calle Secundaria, 456"
    )

@step("un ciudadano realiza la solicitud al sistema")
def step_when_public_work_requested(context):
    context.request.id = len(public_works_requests) + 1
    public_works_requests.append(context.request)

@step("el sistema debe asignar un identificador único a la solicitud")
def step_then_assign_id_to_request(context):
    assert context.request.id is not None

@step('registrar la solicitud con un estado inicial "Pendiente de Revisión"')
def step_then_register_request(context):
    assert context.request in public_works_requests
    assert context.request.status == "Pendiente de Revisión"

@step("notificar al ciudadano que la solicitud ha sido recibida")
def step_then_notify_citizen(context):
    print(f"Notificación: La solicitud #{context.request.id} ha sido recibida con estado {context.request.status}.")
