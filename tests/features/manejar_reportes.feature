# language: es

Característica: : Manejar reportes de problemas ciudadanos
  Como ciudadano
  Quiero reportar problemas en mi comunidad
  Para que las instituciones municipales puedan solucionarlos de manera eficiente.

  Escenario: : Reportar un problema en la comunidad
    Dado un problema ha sido identificado con un tipo, descripción y ubicación
    Cuando el ciudadano reporta el problema al sistema
    Entonces el sistema debe asignar un identificador único al reporte
    Y registrar el reporte con un estado inicial "Pendiente"
    Y notificar al ciudadano que el reporte ha sido recibido
