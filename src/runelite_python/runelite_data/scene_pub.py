from runelite_python.runelite_data.publisher import Publisher
from runelite_python.java.api.scene import Scene
from runelite_python.java.api.tile import Tile
from typing import List

class ScenePublisher(Publisher):
    def __init__(self, scene: Scene, publisher_name: str = None, delay=1):
        super().__init__(delay)
        self.scene = scene
        self.publisher_name = publisher_name if publisher_name else scene.__class__.__name__
    
    def get_message(self):
        # tiles_with_objects = self.get_tiles_with_objects()
        # tile_objects = [self.get_tile_objects(tile) for tile in tiles_with_objects]
        return {
                # "tiles": self.scene.get_tiles(),
                # "tiles_with_objects": tiles_with_objects,
                # "tile_objects": tile_objects,
                "tiles_with_ground_items": self.get_tiles_with_ground_items(),
            }
    
    def get_tiles_with_objects(self):
        return self.scene.get_tiles_with_objects()
    
    def get_tiles_with_ground_items(self):
        return self.scene.get_tiles_with_ground_items()
    
    def get_tile_objects(self, tile: List[Tile]):
        return [obj.get_ground_items() for obj in tile]