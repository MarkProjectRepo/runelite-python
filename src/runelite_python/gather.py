from runelite_python.collection.npc import get_npcs_by_proximity
from runelite_python.client.client import ClientGateway
from runelite_python.java.api.actor import Actor
from runelite_python.java.clickqueue import ClickQueue
from runelite_python.java.api.ids.nullobjectid import NullObjectID
from runelite_python.java.api.npc import NPC
from runelite_python.java.api.ids.id import IDManager
from runelite_python.collection.scene import get_scene_ground_objects
from runelite_python.java.screenshot import get_screenshot

from typing import List
class Gather:
    def __init__(self):
        self.client = ClientGateway()
        self.world_view = self.client.get_world_view()
        self.player = self.client.get_player()
        self.click_queue = self.client.get_click_queue()
        # self.id_manager = IDManager()

    def get_closest_npcs(self) -> List[Actor]:
        return get_npcs_by_proximity(self.world_view, self.player)
    
    def get_click_queue(self) -> ClickQueue:
        return ClickQueue(self.click_queue)


if __name__ == "__main__":
    gather = Gather()
    scene = gather.world_view.get_scene()
    tick = gather.client.get_game_tick()
    client = gather.client.get_client()
    import time
    while True:
        start = time.time()
        game_tick = gather.client.get_game_tick()
        if game_tick == tick:
            continue
        
        click_queue = gather.get_click_queue()
        print("First: ", {(obj.get_name(), obj.get_id(), obj.get_id()) for obj in click_queue.iterator(NPC)})
        # print("First: ", {(obj.get_name(), obj.get_id(), tuple(gather.id_manager.identify_id(obj.get_id()))) for obj in click_queue.iterator(NPC)})
        click_queue.clear()
        # scene_objects = get_scene_ground_objects(scene, gather.world_view.get_plane())
        # if tick % 10 == 0:
        #     print(get_screenshot(gather.client))
        
        tick = game_tick
        time.sleep(0.5)
        print(f"Loop: {time.time() - start}")