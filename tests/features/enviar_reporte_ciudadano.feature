# Created by carla at 12/17/2024
# language: es
Característica: Enviar reporte por parte de un ciudadano
  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.

  Esquema del escenario: Enviar un reporte personalmente
    Dado que un ciudadano ha proporcionado los siguientes datos: tipo "<tipo>", descripcion "<descripcion>", ubicacion "<ubicacion>", foto "<foto>"
    Cuando el ciudadano envía el reporte a la entidad municipal
    Entonces la entidad municipal debe procesar el reporte según los datos proporcionados
    Y notificar al ciudadano el "<estado_registro>"

    Ejemplos:
      | tipo   | descripcion              | ubicacion      | foto           | estado_registro |
      | Bache  | Un bache grande          | Calle 123      | foto_bache.jpg | registrado      |
      | Basura | Montón de basura         | Parque central | None           | registrado      |
      | None   | Problema no identificado | Avenida 456    | None           | no_registrado   |
