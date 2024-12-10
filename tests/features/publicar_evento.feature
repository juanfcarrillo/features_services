# Created by Mateo at 09/12/2024

# language: es

Característica: Publicar eventos

  Como ciudadano
  quiero publicar eventos locales
  para promover actividades comunitarias y mantener informados a los demás ciudadanos

  Escenario: Publicar un evento exitosamente
    Dado que un ciudadano desea crear un nuevo evento
    Y proporciona el título del evento "Campeonato de Baloncesto"
    Y establece la fecha del evento "2024-12-15"
    Y selecciona la ubicación del evento "Parque Central"
    Y escribe una descripción para el evento "Un evento para fomentar la actividad deportiva local"
    Cuando publica el evento
    Entonces el evento "Campeonato de Baloncesto" aparecerá en la lista de eventos públicos