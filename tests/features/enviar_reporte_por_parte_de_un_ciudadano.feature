# Created by shander at 18/12/2024

# language: es

Característica: Enviar reporte por parte de un ciudadano

  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.

  Escenario: Enviar un reporte de forma asistida
    Dado que un ciudadano llamado "Juan Pérez" con correo "juan@example.com" e identificación "1234567890" está en comunicación con un asistente
    Y una institución municipal llamada "Obras Públicas" con email "obraspublicas@example.com"
    Y el ciudadano proporciona un reporte con asunto "Fuga de agua", descripción "Hay una fuga de agua en la calle principal" y ubicación "Calle Principal 123"
    Cuando el cidudadano termina de dar los detalles y se envía el reporte
    Entonces se notifica al ciudadano que el reporte fue enviado con éxito
    Y la institución municipal recibe y guarda el reporte