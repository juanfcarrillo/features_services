class PrioritizationService:
    @staticmethod
    def determine_frequency_and_priority(report):
        # Simulate checking for existing records
        if report.tipo == "Inundación recurrente":
            report.frecuencia = "Recurrente"
            report.prioridad = 1
        elif report.tipo == "Árbol caído único":
            report.frecuencia = "Único"
            report.prioridad = 5
        else:
            report.frecuencia = "Ocasional"
            report.prioridad = 3
    @staticmethod
    def determine_frequency_and_priority(report):
        # Simulate checking for existing records
        if report.tipo == "Inundación recurrente":
            report.frecuencia = "Recurrente"
            report.prioridad = 1
        elif report.tipo == "Árbol caído único":
            report.frecuencia = "Único"
            report.prioridad = 5
        else:
            report.frecuencia = "Ocasional"
            report.prioridad = 3
