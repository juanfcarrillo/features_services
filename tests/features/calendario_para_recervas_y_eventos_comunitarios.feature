# Created by shander at 10/12/2024
# language: es

Característica: : Calendario para recervas y eventos comunitarios

  Como ciudadano
  cuando necesite recervar un espacio comunitario o programar un evento
  necesito un calendario para poder hacerlo de manera eficiente.

  Escenario: : Reservar un espacio disponible en el calendario para un evento comunitario.
    Dado un ciudadano visualiza los espacios disponibles en el calendario comunitario
    Cuando selecciona una fecha, horario y completa los detalles del evento
    Entonces el sistema registra la reserva como "Pendiente de Aprobación"
    Y bloquea el horario en el calendario como "En Proceso"
    Y notifica al ciudadano sobre la reserva.


