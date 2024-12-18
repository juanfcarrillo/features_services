# Created by carla at 12/17/2024
  #language: es

# Para las 3 primeras features seria conveniente elegir un formulario para hacer mas flexible la presentacion de datos y la forma en la que se puede utilizar un esquema de escenario

Característica: Enviar reporte por parte de un ciudadano
  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que las instituciones municipales lo reciban y puedan gestionarlo de manera eficiente.

  Esquema del escenario: Enviar un reporte personalmente
    Dado que un ciudadano ha proporcionado los siguientes datos:
      | Campo       | Valor            |
      | Tipo        | <tipo>           |
      | Descripcion | <descripcion>    |
      | Ubicacion   | <ubicacion>      |
      | Foto        | <foto>           |
    Cuando el ciudadano envía el reporte a la entidad municipal
    Entonces la entidad municipal debe procesar el reporte según los datos proporcionados
    Y notificar al ciudadano el "<estado_registro>"

    Ejemplos:
    | tipo         | descripcion               | ubicacion       | foto               |estado_registro|
    |--------------|---------------------------|-----------------|--------------------|------------|
    | Bache        | Un bache grande           | Calle 123       | foto_bache.jpg     |registrado  |
    | Basura       | Monton de basura          | Parque central  |                    |registrado  |
    |              | Problema no identificado  | Avenida 456     |                    |no_registrado|

#  Escenario: Reportar un problema utilizando geolocalización automática
#    Dado que un ciudadano ha identificado un problema con tipo "<tipo>" y descripción "<descripción>"
#    Y ha permitido al sistema capturar su ubicación automáticamente
#    Cuando el ciudadano envía el reporte al sistema
#    Entonces el sistema debe capturar la ubicación geolocalizada del dispositivo
#    Y registrar el reporte con un estado inicial "Pendiente de Revisión"
#    Y notificar al ciudadano que el reporte ha sido recibido
#
#  Escenario: Enviar un reporte de forma asistida
#    Dado que un ciudadano llamado "<nombre_ciudadano>" con correo "<correo>" e identificación "<ci>" está en comunicación con un asistente
#    Y el ciudadano proporciona un un problema de tipo "<tipo>"
#    Y detalla la descripción "<descripcion>"
#    Y proporciona la ubicación "<ubicacion>"
#    Cuando el cidudadano termina de dar los detalles y se envía el reporte
#    Entonces se notifica al ciudadano que el reporte fue enviado con éxito


