Feature: Manejar reportes de problemas ciudadanos
  Como ciudadano
  Quiero reportar problemas en mi comunidad
  Para que las instituciones municipales puedan solucionarlos de manera eficiente.

  Scenario: Reportar un problema en la comunidad
    Given un problema ha sido identificado con un tipo, descripción y ubicación
    When el ciudadano reporta el problema al sistema
    Then el sistema debe asignar un identificador único al reporte
    And registrar el reporte con un estado inicial "Pendiente"
    And notificar al ciudadano que el reporte ha sido recibido
