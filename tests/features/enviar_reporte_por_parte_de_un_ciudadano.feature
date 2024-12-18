# Created by shander at 18/12/2024

# language: es

Característica: Enviar reporte por parte de un ciudadano

  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.

  Esquema del escenario: Enviar un reporte de forma asistida
    Dado que un ciudadano llamado "<nombre_ciudadano>" con correo "<correo>" e identificación "<identificacion>" está en comunicación con un asistente
    Y una institución municipal llamada "<nombre_municipio>" con email "<email>"
    Y el ciudadano proporciona un reporte con asunto "<asunto>", descripción "<descripcion>" y ubicación "<ubicacion>"
    Cuando el cidudadano termina de dar los detalles y se envía el reporte
    Entonces se notifica al ciudadano que el reporte fue enviado con éxito
    Y la institución municipal recibe y guarda el reporte
    Ejemplos:
      | nombre_ciudadano | correo             | identificacion | nombre_municipio  | email                     | asunto         | descripcion                                | ubicacion           |
      | Juan Pérez       | juan@example.com   | 1234567890     | Obras Públicas    | obraspublicas@example.com | Fuga de agua   | Hay una fuga de agua en la calle principal | Calle Principal 123 |
      | María García     | maria@example.com  | 0987654321     | Alumbrado Público | alumbrado@example.com     | Lámpara rota   | Una lámpara de la calle está rota          | Avenida Central 45  |
      | Ana Fernández    | ana@example.com    | 9988776655     | Obras Públicas    | obraspublicas@example.com | Calle inundada | Hay una calle inundada tras la lluvia      | Calle Secundaria 89 |