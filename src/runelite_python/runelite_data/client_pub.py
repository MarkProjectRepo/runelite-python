from runelite_python.runelite_data.publisher import Publisher
from runelite_python.client.client import ClientGateway
from runelite_python.java.api.world_view import WorldView
from runelite_python.java.clickqueue import ClickQueue
from runelite_python.java.api.npc import NPC
from runelite_python.java.api.client import Client

class ClientPublisher(Publisher):
    def __init__(self, client: ClientGateway, publisher_name: str = None):
        super().__init__()
        self.client = client
        self.publisher_name = publisher_name if publisher_name else client.__class__.__name__
    
    def get_message(self):
        client = self.client.get_client()
        world_view = self.client.get_world_view()
        click_queue = self.client.get_click_queue()

        return {
            **self._get_click_queue_info(click_queue),
            **self._get_world_info(client, world_view),
        }

    def _get_click_queue_info(self, click_queue: ClickQueue) -> dict:
        return {
            "size": click_queue.size(),
            "is_empty": click_queue.is_empty(),
            "object_ids": {obj.get_id() for obj in click_queue.iterator(NPC)},
            "object_names": {obj.get_name() for obj in click_queue.iterator(NPC)},
        }

    def _get_world_info(self, client: Client, world_view: WorldView) -> dict:
        return {
            "plane": client.get_plane(),
            "base_x": client.get_base_x(),
            "base_y": client.get_base_y(),
            "camera_x": client.get_camera_x(),
            "camera_y": client.get_camera_y(),
            "camera_z": client.get_camera_z(),
            "camera_pitch": client.get_camera_pitch(),
            "camera_yaw": client.get_camera_yaw(),
            "npcs": [npc.get_id() for npc in world_view.npcs()],
            "players": [player.get_id() for player in world_view.players()],
            "instanced": world_view.is_instance(),
            "viewport_width": client.get_viewport_width(),
            "viewport_height": client.get_viewport_height(),
            # Add more world details as needed
        }
