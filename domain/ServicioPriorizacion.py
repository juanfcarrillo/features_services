from app import Reporte

class PrioritizationService:
    @staticmethod
    def determine_priority(reporte: Reporte):
        asunto = reporte.get_tipo_reporte().get_asunto()
        if "Inundación recurrente" in asunto:
            reporte.set_prioridad(1)
        elif "Árbol caído" in asunto:
            reporte.set_prioridad(3)
        else:
            reporte.set_prioridad(5)

    @staticmethod
    def determine_frequency(reporte: Reporte):
        asunto = reporte.get_tipo_reporte().get_asunto()
        if "Inundación recurrente" in asunto:
            reporte.set_frecuencia("Recurrente")
        elif "Árbol caído" in asunto:
            reporte.set_frecuencia("Único")
        else:
            reporte.set_frecuencia("Ocasional")