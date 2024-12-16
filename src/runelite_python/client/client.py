from py4j.java_gateway import JavaGateway, GatewayParameters
from runelite_python.java.api.world_view import WorldView
from runelite_python.java.api.player import Player
from runelite_python.java.clickqueue import ClickQueue
from runelite_python.java.helpers import wrap_getter
from runelite_python.java.api.client import Client
from runelite_python.java.api.enum_manager import EnumManager

class ClientGateway:
    def __init__(self):
        self.gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
        self.instance = self.gateway.entry_point
        self.enum_manager = EnumManager(self.gateway)

    @wrap_getter(Client)
    def get_client(self) -> Client:
        return self.instance.getClient()

    def get_client_ui(self):
        return self.instance.getClientUI()

    def get_world_view(self) -> WorldView:
        return self.get_client().get_top_level_world_view()
    
    def get_player(self) -> Player:
        return self.get_client().get_local_player()

    def get_player_location(self):
        return self.get_player().get_local_location()

    @wrap_getter(ClickQueue)
    def get_click_queue(self) -> ClickQueue:
        return self.instance.getClickQueue()
    
    def get_image(self):
        return self.instance.lastImage
    
    def get_game_tick(self) -> int:
        return self.instance.tickCount
    
    def get_enum(self, enum_name: str):
        return self.enum_manager.get_enum(enum_name)
