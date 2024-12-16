from runelite_python.java.api.scene import Scene
from runelite_python.java.api.groundobject import GroundObject
from typing import List
from runelite_python.java.api.tile import Tile

def get_scene_ground_objects(scene: Scene, desired_plane: int) -> List[Tile]:
    tiles: List[List[Tile]] = scene.get_current_level_tiles(desired_plane)
    flattened_tiles = [tile for row in tiles for tile in row]

    return [tile.get_ground_object() for tile in flattened_tiles]