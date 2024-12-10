# language: es

Característica: Comunicación entre instituciones municipales
  Como institución municipal
  Quiero comunicarme con otras instituciones relevantes sobre problemas reportados
  Para resolver problemas que requieren colaboración interinstitucional de manera eficiente.

  Escenario: Identificar la necesidad de colaboración interinstitucional
    Dado que un problema ha sido reportado con un tipo y ubicación específica
    Y el sistema detecta que el problema requiere la intervención de más de una institución
    Cuando el problema es revisado por una institución principal responsable
    Entonces el sistema debe notificar a las instituciones involucradas
    Y debe permitir a la institución principal asignar tareas específicas a las otras instituciones

  Escenario: Seguimiento de la colaboración interinstitucional
    Dado que un problema ha sido asignado a múltiples instituciones
    Y cada institución tiene tareas pendientes asignadas
    Cuando una institución actualiza el progreso de su tarea en el sistema
    Entonces el sistema debe registrar el progreso de esa tarea
    Y notificar a las otras instituciones involucradas sobre la actualización

  Escenario: Resolución colaborativa del problema
    Dado que todas las tareas asignadas a las instituciones han sido completadas
    Cuando la institución principal marca el problema como "Resuelto"
    Entonces el sistema debe actualizar el estado del problema a "Resuelto"
    Y notificar al ciudadano que el problema ha sido solucionado con la colaboración de múltiples instituciones

  Escenario: Escalar problemas no resueltos a tiempo
    Dado que un problema asignado a múltiples instituciones no ha sido resuelto en el tiempo establecido
    Cuando el tiempo límite expira
    Entonces el sistema debe enviar alertas a las instituciones involucradas
    Y notificar al ciudadano que el problema está en proceso, pero ha requerido más tiempo

