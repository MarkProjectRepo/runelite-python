from runelite_python.client.publisher import Publisher
from runelite_python.java.api.player import Player
from runelite_python.java.api.actor import Actor

class PlayerPublisher(Publisher):
    def __init__(self, player: Player, publisher_name: str = None, delay=1):
        super().__init__(delay)
        self.player = player
        self.publisher_name = publisher_name if publisher_name else player.__class__.__name__
    
    def get_message(self):
        return {
                "combat_level": self.player.get_combat_level(),
                "is_dead": self.player.is_dead(),
                "is_interacting": self.player.is_interacting(),
                "interacting_actor": self.player.get_interacting(),
                "health_ratio": self.player.get_health_ratio(),
                "health_scale": self.player.get_health_scale(),
                "world_location": (self.player.get_world_location().get_x(), self.player.get_world_location().get_y()),
                "overhead_text": self.player.get_overhead_text(),
            }

    def get_combat_level(self):
        """Returns the combat level of the player."""
        return self.player.get_combat_level()

    def is_player_dead(self):
        """Checks if the player is dead."""
        return self.player.is_dead()

    def is_player_interacting(self):
        """Checks if the player is interacting with another actor."""
        return self.player.is_interacting()

    def get_interacting_actor(self) -> Actor:
        """Returns the actor that the player is interacting with."""
        return self.player.get_interacting()

    def get_health_ratio(self):
        """Returns the health ratio of the player."""
        return self.player.get_health_ratio()

    def get_health_scale(self):
        """Returns the health scale of the player."""
        return self.player.get_health_scale()

    def get_world_location(self):
        """Returns the world location of the player."""
        return self.player.get_world_location()
    
    def get_overhead_text(self) -> str:
        """Returns the overhead text of the player."""
        return self.player.get_overhead_text()
    