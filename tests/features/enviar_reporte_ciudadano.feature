# Created by carla at 12/17/2024
  #language: es

# Para las 3 primeras features seria conveniente elegir un formulario para hacer mas flexible la presentacion de datos y la forma en la que se puede utilizar un esquema de escenario

Característica: Enviar reporte por parte de un ciudadano
  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.


  Escenario: Enviar un reporte exitosamente con todos los detalles

    Dado que un ciudadano ha identificado un problema de tipo "<tipo>", descripción "<descripción>" y ubicación "<ubicación>"
    Y ha adjuntado una foto como evidencia "<foto>"
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe asignar un identificador único al reporte
    Y registrar el reporte con un estado inicial "Pendiente de Revisión"
    Y notificar al ciudadano que el reporte ha sido recibido


  Escenario: Reportar un problema sin evidencia fotográfica

    Dado que un ciudadano ha identificado un problema de tipo "<tipo>", descripción "<descripción>" y ubicación "<ubicación>"
    Y no ha adjuntado ninguna foto como evidencia
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe asignar un identificador único al reporte
    Y notificar al ciudadano que el reporte ha sido recibido


  Escenario: Enviar un reporte con datos incompletos

    Dado que un ciudadano intenta enviar un reporte con descripción "<descripción>" y ubicación "<ubicación>" pero sin tipo
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe rechazar el reporte
    Y mostrar un mensaje al ciudadano indicando que complete los campos obligatorios

  Escenario: Reportar un problema utilizando geolocalización automática

    Dado que un ciudadano ha identificado un problema con tipo "<tipo>" y descripción "<descripción>"
    Y ha permitido al sistema capturar su ubicación automáticamente
    Cuando el ciudadano envía el reporte al sistema
    Entonces el sistema debe capturar la ubicación geolocalizada del dispositivo
    Y registrar el reporte con un estado inicial "Pendiente de Revisión"
    Y notificar al ciudadano que el reporte ha sido recibido

