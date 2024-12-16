from runelite_python.java.api.tile import Tile
from typing import List
from runelite_python.java.api.groundobject import GroundObject
from runelite_python.java.helpers import wrap_getter, wrap_iterator
class Scene:
    def __init__(self, instance):
        self.instance = instance

        # Inherit functions from the instance dynamically
        for attr in dir(instance):
            if callable(getattr(instance, attr)) and not attr.startswith("__"):
                setattr(self, attr, getattr(instance, attr))

    @wrap_iterator(Tile)
    def get_tiles(self) -> List[List[List[Tile]]]:
        """
        Gets the tiles in the scene.

        Returns:
            List[List[List[Tile]]]: a 4x104x104 array of tiles in [plane][x][y]
        """
        return self.instance.getTiles()
    
    def get_current_level_tiles(self, level: int, limit=10) -> List[List[Tile]]:
        """
        Gets the tiles for the current level, limited by the specified limit.

        Args:
            level (int): The level to get tiles for.
            limit (int): The maximum number of tiles to return.

        Returns:
            List[List[Tile]]: A list of tiles for the specified level, limited by the specified limit.
        """
        tiles = self.get_tiles()[level]
        middle_x = len(tiles) // 2
        middle_y = len(tiles[0]) // 2
        limited_tiles = [row[max(0, middle_y - limit // 2):middle_y + limit // 2] for row in tiles[max(0, middle_x - limit // 2):middle_x + limit // 2]]
        return [[Tile(tile) for tile in row] for row in limited_tiles]
    
    def get_tiles_with_objects(self):
        """
        Gets the tiles with objects in the scene.
        """
        tiles = self.get_tiles()[0]
        return sum([[tile for tile in row if tile.get_game_objects()] for row in tiles], [])
    
    def get_tiles_with_ground_items(self):
        """
        Gets the tiles with ground items in the scene.
        """
        tiles = self.get_tiles()[0]
        return sum([[tile for tile in row if tile.get_ground_items()] for row in tiles], [])

    def get_extended_tiles(self):
        return self.instance.getExtendedTiles()
        
    def get_extended_tile_settings(self):
        return self.instance.getExtendedTileSettings()

    def get_instance_template_chunks(self):
        return self.instance.getInstanceTemplateChunks()
    
    def get_draw_distance(self):
        return self.instance.getDrawDistance()
    
    def set_draw_distance(self, draw_distance: int):
        self.instance.setDrawDistance(draw_distance)
    
    def get_world_view_id(self):
        return self.instance.getWorldViewId()
    
    def get_min_level(self):
        """
        Gets the minimum level for this scene.
        """
        return self.instance.getMinLevel()
    
    def set_min_level(self, min_level: int):
        """
        Sets the minimum level for this scene.
        """
        self.instance.setMinLevel(min_level)
    
    def remove_tile(self, tile):
        """
        Removes a tile from this scene.
        """
        self.instance.removeTile(tile)
    
    def remove_game_object(self, game_object):
        """
        Removes a game object from this scene.
        """
        self.instance.removeGameObject(game_object)
    
    def generate_houses(self):
        """
        Generates houses for this scene.
        """
        self.instance.generateHouses()
    
    def set_roof_removal_mode(self, flags: int):
        """
        Sets the roof removal mode for this scene.
        """
        self.instance.setRoofRemovalMode(flags)
    
    def get_underlay_ids(self):
        """
        Gets the underlay IDs for this scene.
        """
        return self.instance.getUnderlayIds()
    
    def get_overlay_ids(self):
        """
        Gets the overlay IDs for this scene.
        """
        return self.instance.getOverlayIds()
    
    def get_tile_shapes(self):
        """
        Gets the tile shapes for this scene.
        """
        return self.instance.getTileShapes()
    
    def get_tile_heights(self):
        """
        Gets the tile heights for this scene.
        """
        return self.instance.getTileHeights()
    
    def get_base_x(self):
        """
        Gets the base X for this scene.
        """
        return self.instance.getBaseX()
    
    def get_base_y(self):
        """
        Gets the base Y for this scene.
        """
        return self.instance.getBaseY()
    
    def is_instance(self):
        """
        Checks if this scene is an instance.
        """
        return self.instance.isInstance()
    
    