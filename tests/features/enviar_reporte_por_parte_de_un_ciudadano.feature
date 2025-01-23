# language: es

  # Enviar respecto a la base de datos

Característica: Enviar y gestionar reporte por parte de un ciudadano

  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que el sistema determine la frecuencia del problema y asigne una prioridad automáticamente en una escala del 1 al 5.

  Escenario: Enviar un reporte con registro previo del problema
    Dado que un ciudadano llamado "Juan Pérez" con correo "juan@example.com" e identificación "1234567890" ha identificado un problema
    Y proporciona sus detalles en un reporte con asunto "Inundación recurrente", descripción "Inundaciones frecuentes en la calle principal" y ubicación "Calle Principal 123"
    Cuando se envía el reporte descrito
    Y se encuentra registros previos del problema
    Entonces el reporte se asigna con frecuencia "Recurrente" y prioridad "1"
    Y el ciudadano recibe una confirmación del envío del reporte

  Escenario: Enviar un reporte sin registro previo del problema
    Dado que un ciudadano llamado "Ana Fernández" con correo "ana@example.com" e identificación "9988776655" ha identificado un problema
    Y proporciona sus detalles en un reporte con asunto "Árbol caído único", descripción "Un árbol cayó hoy en la calle" y ubicación "Calle Secundaria 89"
    Cuando se envía el reporte descrito
    Y no se encuentra registros previos del problema
    Entonces el reporte se asigna con frecuencia "Único" y prioridad "5"
    Y el ciudadano recibe una confirmación del envío del reporte


#    Escenario: Enviar un reporte sin registro previo del problema
#    Dado que un ciudadano llamado "Ana Fernández" con correo "ana@example.com" e identificación "9988776655" ha identificado un problema
#    Y proporciona sus detalles en un reporte con asunto "Árbol caído único", descripción "Un árbol cayó hoy en la calle" y ubicación "Calle Secundaria 89"
#    Cuando el ciudadano completa y confirma los detalles del reporte
#    Y no se encuentra registros previos del problema
#    Entonces el reporte se asigna con frecuencia "Único" y prioridad "5"
#    Y el ciudadano recibe una confirmación del envío del reporte