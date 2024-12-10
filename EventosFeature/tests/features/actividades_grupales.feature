# Created by Mateo at 09/12/2024

# language: es

Característica: Actividades grupales por ciudadano

  Como ciudadano
  quiero organizar actividades grupales
  para promover la colaboración y participación comunitaria

  Escenario: Crear una actividad grupal exitosamente
    Dado que un ciudadano desea organizar una nueva actividad grupal
    Y proporciona el título de la actividad "Clase de Yoga al Aire Libre"
    Y selecciona la ubicación de la actividad grupal "Parque Central"
    Y establece la fecha de la actividad grupal "2024-12-20"
    Y envía invitaciones para la actividad a "10" personas
    Cuando publica la actividad grupal
    Entonces la actividad grupal "Clase de Yoga al Aire Libre" aparecerá en la lista de actividades disponibles
