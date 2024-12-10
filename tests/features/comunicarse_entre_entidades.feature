# language: es

Característica: Comunicación entre instituciones municipales
  Como institución municipal
  Quiero comunicarme con otras instituciones relevantes sobre problemas reportados
  Para resolver problemas que requieren colaboración interinstitucional de manera eficiente.

  Escenario: Identificar la necesidad de colaboración interinstitucional
    Dado que un problema ha sido reportado con un tipo y ubicación específica
    Y el sistema detecta que el problema requiere la intervención de más de una institución
    Cuando una institución principal toma la responsabilidad del problema
    Entonces el sistema debe notificar a las instituciones involucradas
    Y permitir a la institución principal asignar tareas específicas a las otras instituciones

  Escenario: Seguimiento de la colaboración interinstitucional
    Dado que un problema ha sido asignado a múltiples instituciones
    Y cada institución tiene tareas pendientes asignadas
    Cuando una institución actualiza el progreso de su tarea en el sistema
    Entonces el sistema debe registrar el progreso de esa tarea
    Y notificar a las otras instituciones involucradas sobre la actualización