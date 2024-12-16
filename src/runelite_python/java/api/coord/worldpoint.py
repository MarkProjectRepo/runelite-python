class WorldPoint:
    """
    Represents a three-dimensional point in the world coordinate space of the game.
    This class provides methods to manipulate and interact with world coordinates.

    `net.runelite.api.coords.WorldPoint <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/coords/WorldPoint.java>`_

    Methods:
        - get_x()
        - get_y()
        - get_plane()
        - dx()
        - dy()
        - dz()
        - distance_to()
        - distance_to_2d()
        - is_in_scene()
        - from_local()
        - from_scene()
        - get_region_id()
        - get_region_x()
        - get_region_y()
        - to_world_area()
    """

    def __init__(self, world_point_instance):
        """
        Initializes a new instance of the WorldPoint class.

        Args:
            world_point_instance: The Java WorldPoint instance.
        """
        self.world_point_instance = world_point_instance

    def get_x(self) -> int:
        """
        Gets the x-axis coordinate of the WorldPoint.
        
        Returns:
            int: The x-axis coordinate.
        """
        return self.world_point_instance.getX()

    def get_y(self) -> int:
        """
        Gets the y-axis coordinate of the WorldPoint.
        
        Returns:
            int: The y-axis coordinate.
        """
        return self.world_point_instance.getY()

    def get_plane(self) -> int:
        """
        Gets the plane (z-axis) coordinate of the WorldPoint.
        
        Returns:
            int: The plane coordinate.
        """
        return self.world_point_instance.getPlane()

    def dx(self, dx: int):
        """
        Returns a new WorldPoint instance with the x-axis offset by the given amount.
        
        Args:
            dx (int): The amount to offset the x-axis.

        Returns:
            WorldPoint: A new WorldPoint instance with the updated x-axis.
        """
        return WorldPoint(self.world_point_instance.dx(dx))

    def dy(self, dy: int):
        """
        Returns a new WorldPoint instance with the y-axis offset by the given amount.
        
        Args:
            dy (int): The amount to offset the y-axis.

        Returns:
            WorldPoint: A new WorldPoint instance with the updated y-axis.
        """
        return WorldPoint(self.world_point_instance.dy(dy))

    def dz(self, dz: int):
        """
        Returns a new WorldPoint instance with the plane (z-axis) offset by the given amount.
        
        Args:
            dz (int): The amount to offset the plane.

        Returns:
            WorldPoint: A new WorldPoint instance with the updated plane.
        """
        return WorldPoint(self.world_point_instance.dz(dz))

    def distance_to(self, other):
        """
        Calculates the distance to another WorldPoint. If the other point is on a different plane,
        the distance will be considered as Integer.MAX_VALUE.

        Args:
            other (WorldPoint): The other WorldPoint to calculate the distance to.

        Returns:
            int: The distance to the other point, or Integer.MAX_VALUE if on a different plane.
        """
        return self.world_point_instance.distanceTo(other.world_point_instance)

    def distance_to_2d(self, other):
        """
        Calculates the 2D distance to another WorldPoint, ignoring the plane.

        Args:
            other (WorldPoint): The other WorldPoint to calculate the 2D distance to.

        Returns:
            int: The 2D distance to the other point.
        """
        return self.world_point_instance.distanceTo2D(other.world_point_instance)

    def is_in_scene(self, client):
        """
        Checks if this WorldPoint is within the current scene in the game.

        Args:
            client: The game client instance.

        Returns:
            bool: True if the WorldPoint is in the scene, False otherwise.
        """
        return self.world_point_instance.isInScene(client.client_instance)

    def from_local(self, client, local_point):
        """
        Converts a LocalPoint to a WorldPoint based on the client's current world view.

        Args:
            client: The game client instance.
            local_point (LocalPoint): The local point to convert.

        Returns:
            WorldPoint: The corresponding WorldPoint.
        """
        return WorldPoint(WorldPoint.fromLocal(client.client_instance, local_point.local_point_instance))

    def from_scene(self, client, x, y, plane):
        """
        Converts scene coordinates to a WorldPoint.

        Args:
            client: The game client instance.
            x (int): The x-axis scene coordinate.
            y (int): The y-axis scene coordinate.
            plane (int): The plane of the scene coordinate.

        Returns:
            WorldPoint: The corresponding WorldPoint.
        """
        return WorldPoint(WorldPoint.fromScene(client.client_instance, x, y, plane))

    def get_region_id(self):
        """
        Retrieves the region ID that this WorldPoint belongs to.

        Returns:
            int: The region ID.
        """
        return self.world_point_instance.getRegionID()

    def get_region_x(self):
        """
        Retrieves the x-axis coordinate within its region.

        Returns:
            int: The region x-axis coordinate.
        """
        return self.world_point_instance.getRegionX()

    def get_region_y(self):
        """
        Retrieves the y-axis coordinate within its region.

        Returns:
            int: The region y-axis coordinate.
        """
        return self.world_point_instance.getRegionY()

    # def to_world_area(self):
    #     """
    #     Converts this WorldPoint into a WorldArea of size 1x1.

    #     Returns:
    #         WorldArea: A WorldArea encompassing only this WorldPoint.
    #     """
    #     return WorldArea(self.world_point_instance.toWorldArea())

    
