# Created by carla at 12/17/2024
  #language: es

Característica: Enviar reporte por parte de un ciudadano
  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.


Escenario: Enviar un reporte exitosamente con todos los detalles

  Dado que un ciudadano ha identificado un problema con tipo "<tipo>", descripción "<descripción>" y ubicación "<ubicación>"
  Y ha adjuntado una foto como evidencia "<foto>"
  Cuando el ciudadano envía el reporte al sistema
  Entonces el sistema debe asignar un identificador único al reporte
  Y registrar el reporte con un estado inicial "Pendiente de Revisión"
  Y notificar al ciudadano que el reporte ha sido recibido