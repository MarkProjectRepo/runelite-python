from .npc import NPC
from typing import List, Optional
from runelite_python.java.api.scene import Scene
from runelite_python.java.helpers import wrap_getter, wrap_iterator
from runelite_python.java.api.player import Player

class WorldView:
    """
    Represents the world view in the game.
    """
    def __init__(self, worldview_instance):
        self.world_view = worldview_instance

    def get_id(self) -> int:
        """
        Get the world view id
        :return: the id, or -1 if this is the top level worldview
        """
        return self.world_view.getId()

    def is_top_level(self) -> bool:
        """
        Test if this worldview is the top level world view.
        :return: True if this is the top level world view, False otherwise
        """
        return self.world_view.isTopLevel()

    @wrap_getter(Scene)
    def get_scene(self) -> Scene:
        """
        Gets the worldview's scene
        :return: The Scene object
        """
        return self.world_view.getScene()

    @wrap_iterator(Player)
    def players(self):
        """
        Gets all of the Players in this view
        :return: An iterator of Player objects
        """
        return self.world_view.players()

    @wrap_iterator(NPC)
    def npcs(self):
        """
        Gets all the Non Player Characters in this view
        :return: An iterator of NPC objects
        """
        return self.world_view.npcs()

    def world_entities(self):
        """
        Gets all the WorldEntities in this view
        :return: An iterator of WorldEntity objects
        """
        return self.world_view.worldEntities()

    def get_collision_maps(self):
        """
        Gets an array of tile collision data.
        The index into the array is the plane/z-axis coordinate.
        :return: the collision data, or None if not available
        """
        return self.world_view.getCollisionMaps()

    def get_plane(self) -> int:
        """
        Gets the current plane the player is on.
        This value indicates the current map level above ground level, where
        ground level is 0. For example, going up a ladder in Lumbridge castle
        will put the player on plane 1.
        Note: This value will never be below 0. Basements and caves below ground
        level use a tile offset and are still considered plane 0 by the game.
        :return: the plane
        """
        return self.world_view.getPlane()

    def get_tile_heights(self):
        """
        Gets a 3D array containing the heights of tiles in the
        current scene.
        :return: the tile heights
        """
        return self.world_view.getTileHeights()

    def get_tile_settings(self):
        """
        Gets a 3D array containing the settings of tiles in the
        current scene.
        :return: the tile settings
        """
        return self.world_view.getTileSettings()

    def get_size_x(self) -> int:
        """
        Get the size of the world view, x-axis
        :return: The size of the world view on the x-axis
        """
        return self.world_view.getSizeX()

    def get_size_y(self) -> int:
        """
        Get the size of the world view, y-axis
        :return: The size of the world view on the y-axis
        """
        return self.world_view.getSizeY()

    def get_base_x(self) -> int:
        """
        Returns the x-axis base coordinate.
        This value is the x-axis world coordinate of tile (0, 0) in
        the current scene (ie. the bottom-left most coordinates in the scene).
        :return: the base x-axis coordinate
        """
        return self.world_view.getBaseX()

    def get_base_y(self) -> int:
        """
        Returns the y-axis base coordinate.
        This value is the y-axis world coordinate of tile (0, 0) in
        the current scene (ie. the bottom-left most coordinates in the scene).
        :return: the base y-axis coordinate
        """
        return self.world_view.getBaseY()

    def create_projectile(self, id: int, plane: int, startX: int, startY: int, startZ: int, startCycle: int, endCycle: int, slope: int, startHeight: int, endHeight: int, target: Optional['Actor'], targetX: int, targetY: int):
        """
        Create a projectile.
        :param id: projectile/spotanim id
        :param plane: plane the projectile is on
        :param startX: local x coordinate the projectile starts at
        :param startY: local y coordinate the projectile starts at
        :param startZ: local z coordinate the projectile starts at - includes tile height
        :param startCycle: cycle the project starts
        :param endCycle: cycle the projectile ends
        :param slope: slope of the projectile
        :param startHeight: start height of projectile - excludes tile height
        :param endHeight: end height of projectile - excludes tile height
        :param target: optional actor target
        :param targetX: target x - if an actor target is supplied should be the target x
        :param targetY: target y - if an actor target is supplied should be the target y
        :return: the new projectile
        """
        return self.world_view.createProjectile(id, plane, startX, startY, startZ, startCycle, endCycle, slope, startHeight, endHeight, target, targetX, targetY)

    def get_projectiles(self):
        """
        Gets a list of all projectiles currently spawned.
        :return: all projectiles
        """
        return self.world_view.getProjectiles()

    def get_graphics_objects(self):
        """
        Gets a list of all graphics objects currently drawn.
        :return: all graphics objects
        """
        return self.world_view.getGraphicsObjects()

    def get_selected_scene_tile(self):
        """
        Gets the currently selected tile. (ie. last right clicked tile)
        :return: the selected tile, or None if no tile is selected
        """
        return self.world_view.getSelectedSceneTile()

    def is_instance(self) -> bool:
        """
        Check if this scene is an instance
        :return: True if this scene is an instance, False otherwise
        """
        return self.world_view.isInstance()

    def get_instance_template_chunks(self):
        """
        Contains a 3D array of template chunks for instanced areas.
        The array returned is of format [z][x][y], where z is the
        plane, x and y the x-axis and y-axis coordinates of a tile
        divided by the size of a chunk.
        The bits of the int value held by the coordinates are -1 if there is no data,
        structured in the following format:
         0                   1                   2                   3
         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | |rot|     y chunk coord     |    x chunk coord    |pln|       |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        :return: the array of instance template chunks
        """
        return self.world_view.getInstanceTemplateChunks()
