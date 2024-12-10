class PublicReport:
    def __init__(self, report_type, description, location, photo=None):
        self.report_type = report_type
        self.description = description
        self.location = location
        self.photo = photo
        self.id = None
        self.status = None

    def is_valid(self):
        return self.report_type and self.description and self.location

    def auto_geolocate(self):
        # Simulación de captura de ubicación
        self.location = "Ubicación geolocalizada automáticamente"
