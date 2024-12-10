# language: es

Característica: Enviar reporte como ciudadano
  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo.

  Escenario: Reportar un problema con detalles mínimos
    Dado que un ciudadano identifica un problema con un tipo, descripción y ubicación
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe asignar un identificador único al reporte
    Y registrar el reporte con un estado inicial "Pendiente de Revisión"
    Y notificar al ciudadano que el reporte ha sido recibido

  Escenario: Reportar un problema con evidencia fotográfica
    Dado que un ciudadano identifica un problema con un tipo, descripción, ubicación y adjunta una foto
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe asignar un identificador único al reporte
    Y registrar el reporte con un estado inicial "Pendiente de Revisión"
    Y almacenar la evidencia fotográfica adjunta junto al reporte
    Y notificar al ciudadano que el reporte ha sido recibido

  Escenario: Validar los campos requeridos para enviar un reporte
    Dado que un ciudadano intenta enviar un reporte con campos incompletos
    Cuando el sistema valida los datos ingresados
    Entonces el sistema debe rechazar el reporte
    Y mostrar un mensaje al ciudadano indicando que complete los campos obligatorios


  #Escenario: Enviar reporte desde una ubicación geolocalizada
   # Dado que un ciudadano identifica un problema y permite al sistema obtener su ubicación automáticamente
    #Cuando el ciudadano envía el reporte al sistema
    #Entonces el sistema debe capturar la ubicación geolocalizada del dispositivo
    #Y registrar el reporte con un estado inicial "Pendiente de Revisión"
    #Y notificar al ciudadano que el reporte ha sido recibido
