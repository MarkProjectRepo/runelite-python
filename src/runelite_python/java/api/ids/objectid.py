from py4j.java_gateway import JavaGateway


class ObjectID:
    def __init__(self):
        gateway = JavaGateway()
        self.object_id = gateway.jvm.net.runelite.api.ObjectID
        self.object_lookup = {a:getattr(self.object_id, a) for a in dir(self.object_id)}
    
    def is_object_id(self, id: int) -> bool:
        return id in self.object_lookup.values()
    
    def get_name(self, id: int) -> str:
        return self.object_lookup.get(id)
