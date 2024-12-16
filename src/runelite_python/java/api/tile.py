from runelite_python.java.api.gameobject import GameObject
from runelite_python.java.api.groundobject import GroundObject
from runelite_python.java.helpers import wrap_iterator, wrap_getter
# from runelite_python.java.api.item import Item

class Tile:
    def __init__(self, instance):
        self.instance = instance

        # Dynamically inherit methods from the instance
        for attr in dir(instance):
            if callable(getattr(instance, attr)) and not attr.startswith("__"):
                setattr(self, attr, getattr(instance, attr))

    def get_decorative_object(self):
        return self.instance.getDecorativeObject()
    
    @wrap_iterator(GameObject)
    def get_game_objects(self):
        return self.instance.getGameObjects()

    def get_item_layer(self):
        return self.instance.getItemLayer()

    @wrap_getter(GroundObject)
    def get_ground_object(self):
        return self.instance.getGroundObject()

    def set_ground_object(self, ground_object):
        self.instance.setGroundObject(ground_object)

    def get_wall_object(self):
        return self.instance.getWallObject()

    def get_scene_tile_paint(self):
        return self.instance.getSceneTilePaint()

    def get_scene_tile_model(self):
        return self.instance.getSceneTileModel()

    def get_world_location(self):
        return self.instance.getWorldLocation()

    def get_scene_location(self):
        return self.instance.getSceneLocation()

    def get_local_location(self):
        return self.instance.getLocalLocation()

    def get_plane(self):
        return self.instance.getPlane()

    def get_render_level(self):
        return self.instance.getRenderLevel()

    # @wrap_iterator(Item)
    def get_ground_items(self):
        return self.instance.getGroundItems()

    def get_bridge(self):
        return self.instance.getBridge()