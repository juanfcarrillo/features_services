class CollaborativeRequest:
    def __init__(self, request_type, description, location):
        self.request_type = request_type
        self.description = description
        self.location = location
        self.id = None
        self.primary_entity = None
        self.involved_entities = []
        self.tasks = {}
        self.status = "Pendiente"
