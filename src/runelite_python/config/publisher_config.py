from dataclasses import dataclass
from typing import List, Type
from runelite_python.runelite_data.publisher import Publisher
from runelite_python.runelite_data.player_pub import PlayerPublisher
from runelite_python.runelite_data.client_pub import ClientPublisher
from runelite_python.runelite_data.message_pub import MessagePublisher

@dataclass
class PublisherConfig:
    name: str
    enabled: bool = True
    
    @classmethod
    def all_publishers(cls) -> List['PublisherConfig']:
        return [
            cls(name="player"),
            cls(name="client"),
            cls(name="message")
        ]
    
    @classmethod
    def get_publisher_class(cls, name: str) -> Type[Publisher]:
        publisher_map = {
            "player": PlayerPublisher,
            "client": ClientPublisher,
            "message": MessagePublisher
        }
        return publisher_map.get(name) 