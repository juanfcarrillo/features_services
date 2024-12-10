# Created by shander at 10/12/2024
Feature: Calendario para recervas y eventos comunitarios

  Como ciudadano
  cuando necesite recervar un espacio comunitario o programar un evento
  necesito un calendario para poder hacerlo de manera eficiente.

  Scenario: Reservar un espacio disponible en el calendario para un evento comunitario.
    Given un ciudadano visualiza los espacios disponibles en el calendario comunitario
    When selecciona una fecha, horario y completa los detalles del evento
    Then el sistema registra la reserva como "Pendiente de Aprobación"
    And bloquea el horario en el calendario como "En Proceso"
    And notifica al ciudadano sobre la reserva.


