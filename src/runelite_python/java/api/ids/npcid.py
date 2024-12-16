from py4j.java_gateway import JavaGateway


class NpcID:
    def __init__(self):
        gateway = JavaGateway()
        self.npc_id = gateway.jvm.net.runelite.api.NpcID
        self.npc_lookup = {getattr(self.npc_id, a):a for a in dir(self.npc_id) if not a.startswith("_")}
    
    def is_npc_id(self, id: int) -> bool:
        return id in self.npc_lookup.values()
    
    def get_name(self, id: int) -> str:
        return self.npc_lookup.get(id)
