from py4j.java_gateway import JavaGateway


class ItemID:
    def __init__(self):
        gateway = JavaGateway()
        self.item_id = gateway.jvm.net.runelite.api.ItemID
        self.item_lookup = {getattr(self.item_id, a):a for a in dir(self.item_id) if not a.startswith("_")}
    
    def is_item_id(self, id: int) -> bool:
        return id in self.item_lookup.values()
    
    def get_name(self, id: int) -> str:
        return self.item_lookup.get(id)
