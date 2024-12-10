from datetime import datetime

class PublicWorkRequest:
    def __init__(self, request_type, description, location):
        self.id = None  # Será asignado cuando se guarde
        self.request_type = request_type
        self.description = description
        self.location = location
        self.status = "Pendiente de Revisión"
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.request_type,
            "description": self.description,
            "location": self.location,
            "status": self.status,
            "created_at": self.created_at,
        }