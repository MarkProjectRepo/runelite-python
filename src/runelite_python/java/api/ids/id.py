from runelite_python.java.api.ids.itemid import ItemID
from runelite_python.java.api.ids.objectid import ObjectID
from runelite_python.java.api.ids.nullobjectid import NullObjectID
from runelite_python.java.api.ids.npcid import NpcID
class IDManager:
    def __init__(self):
        self.id_managers = [
            (ItemID, ItemID()),
            (ObjectID, ObjectID()),
            (NullObjectID, NullObjectID()),
            (NpcID, NpcID())
        ]

    def identify_id(self, id: int):
        results = []    
        
        for id_class, id_manager in self.id_managers:
            name = id_manager.get_name(id)
            if name:
                results.append((id_class, name))
        
        # Return all matches or unknown if no matches found
        return results
    
    def is_item_id(self, id: int) -> bool:
        return self.item_id_manager.is_item_id(id)
    
    def is_object_id(self, id: int) -> bool:
        return self.object_id_manager.is_object_id(id)
    
    def is_null_object_id(self, id: int) -> bool:
        return self.null_object_id_manager.is_null_object_id(id)
