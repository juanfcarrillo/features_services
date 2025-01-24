from app import Reporte


class GestorReportes:
    reportes: Reporte = []

    @staticmethod
    def agregar_reporte(reporte: Reporte):
        GestorReportes.reportes.append(reporte)

    @staticmethod
    def buscar_por_asunto(asunto):
        return [reporte for reporte in GestorReportes.reportes if reporte.get_tipo_reporte().get_asunto() == asunto]

    @staticmethod
    def actualizar_reporte(reporte: Reporte):
        for i in range(len(GestorReportes.reportes)):
            if GestorReportes.reportes[i].get_estado_registro() == "pendiente":
                GestorReportes.reportes[i] = reporte
                break

    @staticmethod
    def enviar_reporte(reporte: Reporte):
        if reporte.validar_reporte():
            reporte.set_estado_registro("registrado")
            GestorReportes.agregar_reporte(reporte)
            print("Reporte enviado y registrado.")
        else:
            reporte.set_estado_registro("no_registrado")
            print("El reporte no es válido y no se pudo enviar.")
