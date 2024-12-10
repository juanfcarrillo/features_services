# language: es

Característica: : Solicitar obras públicas
  Como ciudadano
  Quiero solicitar obras públicas para mejorar mi entorno
  Para promover el desarrollo de infraestructura en mi comunidad.

  Escenario: : Realizar una solicitud de obra pública
    Dado una necesidad de infraestructura ha sido identificada con un tipo, descripción y ubicación
    Cuando un ciudadano realiza la solicitud al sistema
    Entonces el sistema debe asignar un identificador único a la solicitud
    Y registrar la solicitud con un estado inicial "Pendiente de Revisión"
    Y notificar al ciudadano que la solicitud ha sido recibida
