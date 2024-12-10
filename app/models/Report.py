from datetime import datetime

class Report:
    def __init__(self, report_type, description, location):
        self.id = None  # Será asignado cuando se guarde
        self.report_type = report_type
        self.description = description
        self.location = location
        self.status = "Pendiente"
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.report_type,
            "description": self.description,
            "location": self.location,
            "status": self.status,
            "created_at": self.created_at,
        }