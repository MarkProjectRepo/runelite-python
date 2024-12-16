from typing import Set
from py4j.java_gateway import JavaObject, JavaGateway

class World:
    """
    Holds data of a RuneScape world.

    `net.runelite.api.World <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/World.java>`_

    Methods:
        - get_types()
        - set_types(types)
        - get_player_count()
        - set_player_count(player_count)
        - get_location()
        - set_location(location)
        - get_index()
        - set_index(index)
        - get_id()
        - set_id(id)
        - get_activity()
        - set_activity(activity)
        - get_address()
        - set_address(address)
    """

    def __init__(self, world_instance):
        """
        Initializes a new instance of the World class.

        Args:
            world_instance: The Java World instance.
        """
        self.world_instance = world_instance
        gateway = JavaGateway()
        self.world_type = WorldType(gateway)

    def get_types(self) -> Set[JavaObject]:
        """
        Gets all applicable world types for this world.

        Returns:
            Set[JavaObject]: The world types.
        """
        return set(self.world_instance.getTypes())

    def set_types(self, types: Set[JavaObject]):
        """
        Sets world types.

        Args:
            types (Set[JavaObject]): The types.
        """
        java_types = self.world_type.from_mask(self.world_type.to_mask(types))
        for t in types:
            java_types.add(t)
        self.world_instance.setTypes(java_types)

    def get_player_count(self) -> int:
        """
        Gets the current number of players logged in the world.

        Returns:
            int: The player count.
        """
        return self.world_instance.getPlayerCount()

    def set_player_count(self, player_count: int):
        """
        Sets the player count of the world.

        Args:
            player_count (int): The new player count.
        """
        self.world_instance.setPlayerCount(player_count)

    def get_location(self) -> int:
        """
        Gets the world location value.

        Returns:
            int: The world location.
        """
        return self.world_instance.getLocation()

    def set_location(self, location: int):
        """
        Sets the world location value.

        Args:
            location (int): The location.
        """
        self.world_instance.setLocation(location)

    def get_index(self) -> int:
        """
        Gets the world's index.

        Returns:
            int: The index.
        """
        return self.world_instance.getIndex()

    def set_index(self, index: int):
        """
        Sets the world's index.

        Args:
            index (int): The index.
        """
        self.world_instance.setIndex(index)

    def get_id(self) -> int:
        """
        Gets the world number.

        Returns:
            int: The world number.
        """
        return self.world_instance.getId()

    def set_id(self, id: int):
        """
        Sets the world number.

        Args:
            id (int): The world number.
        """
        self.world_instance.setId(id)

    def get_activity(self) -> str:
        """
        Gets the world activity description.
        For example, world 2 would return "Trade - Members".

        Returns:
            str: The world activity.
        """
        return self.world_instance.getActivity()

    def set_activity(self, activity: str):
        """
        Sets the world activity description.

        Args:
            activity (str): The activity.
        """
        self.world_instance.setActivity(activity)

    def get_address(self) -> str:
        """
        Gets the address of the world.

        Returns:
            str: The world address.
        """
        return self.world_instance.getAddress()

    def set_address(self, address: str):
        """
        Sets the address of the world.

        Args:
            address (str): The address.
        """
        self.world_instance.setAddress(address)

class WorldType:
    """
    Wrapper for the Java WorldType enum.

    `net.runelite.api.WorldType <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/WorldType.java>`_

    Methods:
        - from_mask(mask)
        - to_mask(types)
        - is_pvp_world(world_types)
    """

    def __init__(self, gateway):
        """
        Initializes a new instance of the WorldType class.

        Args:
            gateway: The py4j gateway.
        """
        self.gateway = gateway
        self.world_type = gateway.jvm.net.runelite.api.WorldType
    
    def from_mask(self, mask: int) -> Set[JavaObject]:
        """
        Create set of world types from mask.

        Args:
            gateway: The py4j gateway.
            mask (int): The mask.

        Returns:
            Set[JavaObject]: The set of world types.
        """
        return set(self.world_type.from_mask(mask))

    def to_mask(self, types: Set[JavaObject]) -> int:
        """
        Create mask from set of world types.

        Args:
            gateway: The py4j gateway.
            types (Set[JavaObject]): The types.

        Returns:
            int: The int containing all mask.
        """
        java_types = self.gateway.jvm.java.util.EnumSet.noneOf(self.world_type.class_)
        for t in types:
            java_types.add(t)
        return self.to_mask(java_types)

    def is_pvp_world(self, world_types: Set[JavaObject]) -> bool:
        """
        Checks whether a world having a set of WorldTypes is a PVP world.

        Args:
            gateway: The py4j gateway.
            world_types (Set[JavaObject]): A set of WorldTypes describing the given world.

        Returns:
            bool: True if the given worldtypes of the world are a PVP world, false otherwise.
        """
        return self.world_type.is_pvp_world(world_types)
