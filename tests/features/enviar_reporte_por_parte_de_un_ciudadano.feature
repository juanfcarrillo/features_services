# language: es

Característica: Enviar y gestionar reporte por parte de un ciudadano

  Como ciudadano
  Quiero enviar un reporte de un problema en mi comunidad
  Para que el sistema determine la frecuencia del problema y asigne una prioridad automáticamente en una escala del 1 al 5.

  Escenario: Enviar un reporte con registro previo del problema
    Dado que un ciudadano llamado "Juan Pérez" con correo "juan@example.com" e identificación "1234567890" está en comunicación con un asistente
    Y el ciudadano proporciona un reporte con asunto "Inundación recurrente", descripción "Inundaciones frecuentes en la calle principal" y ubicación "Calle Principal 123"
    Cuando el ciudadano revisa y confirma los detalles del reporte
    Entonces el reporte se envía con éxito
    Y el sistema encuentra registros previos del problema, determina que es recurrente y asigna una prioridad 1
    Y el ciudadano recibe una confirmación del envío, la frecuencia "Recurrente" y la prioridad "1" del reporte

  Escenario: Enviar un reporte sin registro previo del problema
    Dado que un ciudadano llamado "Ana Fernández" con correo "ana@example.com" e identificación "9988776655" está en comunicación con un asistente
    Y el ciudadano proporciona un reporte con asunto "Árbol caído único", descripción "Un árbol cayó por primera vez en la calle" y ubicación "Calle Secundaria 89"
    Cuando el ciudadano revisa y confirma los detalles del reporte
    Entonces el reporte se envía con éxito
    Y el sistema no encuentra registros previos del problema, determina que es único y asigna una prioridad 5
    Y el ciudadano recibe una confirmación del envío, la frecuencia "Único" y la prioridad "5" del reporte