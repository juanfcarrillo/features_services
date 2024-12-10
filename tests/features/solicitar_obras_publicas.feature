Feature: Solicitar obras públicas
  Como ciudadano
  Quiero solicitar obras públicas para mejorar mi entorno
  Para promover el desarrollo de infraestructura en mi comunidad.

  Scenario: Realizar una solicitud de obra pública
    Given una necesidad de infraestructura ha sido identificada con un tipo, descripción y ubicación
    When un ciudadano realiza la solicitud al sistema
    Then el sistema debe asignar un identificador único a la solicitud
    And registrar la solicitud con un estado inicial "Pendiente de Revisión"
    And notificar al ciudadano que la solicitud ha sido recibida
