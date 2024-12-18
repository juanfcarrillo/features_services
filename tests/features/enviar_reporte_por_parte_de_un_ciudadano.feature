# Created by shander at 18/12/2024

# language: es

Característica: Enviar reporte por parte de un ciudadano

  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.

  Escenario: Enviar un reporte de forma asistida
    Dado que un ciudadano llamado "Juan Pérez" con correo "juan@example.com" e identificación "1234567890" está en comunicación con un asistente
    Y el ciudadano proporciona un asunto "Fuga de agua"
    Y detalla la descripción "Hay una fuga de agua en la calle principal"
    Y proporciona la ubicación "Calle Principal 123"
    Cuando el cidudadano termina de dar los detalles y se envía el reporte
    Entonces se notifica al ciudadano que el reporte fue enviado con éxito