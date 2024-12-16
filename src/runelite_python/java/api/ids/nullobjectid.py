from py4j.java_gateway import JavaGateway

OBJECT_PREFIX = "NULL_"
class NullObjectID:
    def __init__(self):
        gateway = JavaGateway()
        self.null_object_id = gateway.jvm.net.runelite.api.NullObjectID
        self.object_ids = {int(a.split("_")[-1]) for a in dir(self.null_object_id) if a.startswith(OBJECT_PREFIX)}
    
    def is_null_object_id(self, id: int) -> bool:
        return id in self.object_ids

    def get_name(self, id: int) -> str:
        return f"{OBJECT_PREFIX}{id}"
