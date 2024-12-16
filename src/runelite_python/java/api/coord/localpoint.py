class LocalPoint:
    """
    Represents a two-dimensional point in the local coordinate space of the game.
    The unit of a LocalPoint is 1/128th of a tile, making it a fine-grained coordinate system relative to the game's tiles.

    `net.runelite.api.coords.LocalPoint <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/coords/LocalPoint.java>`_

    Methods:
        - get_x()
        - get_y()
        - get_world_view_id()
        - distance_to()
        - is_in_scene()
        - get_scene_x()
        - get_scene_y()
        - dx()
        - dy()
        - plus()
    """

    def __init__(self, local_point_instance):
        self.local_point_instance = local_point_instance

    def get_x(self) -> int:
        """
        Gets the x-axis coordinate of the LocalPoint.
        
        Returns:
            int: The x-axis coordinate.
        """
        return self.local_point_instance.getX()

    def get_y(self) -> int:
        """
        Gets the y-axis coordinate of the LocalPoint.
        
        Returns:
            int: The y-axis coordinate.
        """
        return self.local_point_instance.getY()

    def get_world_view_id(self) -> int:
        """
        Gets the identifier for the world view associated with this LocalPoint.
        
        Returns:
            int: The world view identifier.
        """
        return self.local_point_instance.getWorldViewId()

    def distance_to(self, other) -> int:
        """
        Calculates the distance to another LocalPoint.
        
        Args:
            other (LocalPoint): The other LocalPoint to calculate the distance to.
        
        Returns:
            int: The distance between this LocalPoint and the other LocalPoint.
        """
        return self.local_point_instance.distanceTo(other.local_point_instance)

    def is_in_scene(self) -> bool:
        """
        Checks if this LocalPoint is within the basic 104x104 tile scene.
        
        Returns:
            bool: True if the LocalPoint is within the scene, otherwise False.
        """
        return self.local_point_instance.isInScene()

    def get_scene_x(self) -> int:
        """
        Gets the x-axis coordinate in scene space (tiles).
        
        Returns:
            int: The x-axis coordinate in scene space.
        """
        return self.local_point_instance.getSceneX()

    def get_scene_y(self) -> int:
        """
        Gets the y-axis coordinate in scene space (tiles).
        
        Returns:
            int: The y-axis coordinate in scene space.
        """
        return self.local_point_instance.getSceneY()

    def dx(self, dx: int):
        """
        Moves the point along the x-axis by a specified distance.
        
        Args:
            dx (int): The distance to move along the x-axis.
        
        Returns:
            LocalPoint: A new LocalPoint shifted along the x-axis.
        """
        return LocalPoint(self.local_point_instance.dx(dx))

    def dy(self, dy: int):
        """
        Moves the point along the y-axis by a specified distance.
        
        Args:
            dy (int): The distance to move along the y-axis.
        
        Returns:
            LocalPoint: A new LocalPoint shifted along the y-axis.
        """
        return LocalPoint(self.local_point_instance.dy(dy))

    def plus(self, dx: int, dy: int):
        """
        Moves the point by specified distances along the x and y axes.
        
        Args:
            dx (int): The distance to move along the x-axis.
            dy (int): The distance to move along the y-axis.
        
        Returns:
            LocalPoint: A new LocalPoint shifted by the specified distances.
        """
        return LocalPoint(self.local_point_instance.plus(dx, dy))