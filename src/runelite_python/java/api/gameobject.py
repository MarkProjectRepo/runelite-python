from runelite_python.java.api.tileobject import TileObject

class GameObject(TileObject):
    def __init__(self, instance):
        super().__init__(instance)

        # Inherit functions from the instance dynamically
        for attr in dir(instance):
            if callable(getattr(instance, attr)) and not attr.startswith("__"):
                setattr(self, attr, getattr(instance, attr))

    def size_x(self):
        """Get the size of this object, in tiles, on the x axis"""
        return self.instance.sizeX()

    def size_y(self):
        """Get the size of this object, in tiles, on the y axis"""
        return self.instance.sizeY()

    def get_scene_min_location(self):
        """
        Gets the minimum x and y scene coordinate pair for this game object.
        """
        return self.instance.getSceneMinLocation()

    def get_scene_max_location(self):
        """
        Gets the maximum x and y scene coordinate pair for this game object.
        This value differs from get_scene_min_location() when the size
        of the object is more than 1 tile.
        """
        return self.instance.getSceneMaxLocation()

    def get_convex_hull(self):
        """
        Gets the convex hull of the object's model.
        """
        return self.instance.getConvexHull()

    def get_orientation(self):
        """
        Get the orientation of the object
        """
        return self.instance.getOrientation()

    def get_renderable(self):
        """
        Get the renderable component of the object
        """
        return self.instance.getRenderable()

    def get_model_orientation(self):
        """
        Gets the orientation of the model in JAU.
        This is typically 0 for non-actors, since
        most object's models are oriented prior to
        lighting during scene loading.
        """
        return self.instance.getModelOrientation()

    def get_config(self):
        """
        A bitfield containing various flags:
        object type = bits & 31
        orientation = bits >>> 6 & 3
        supports items = bits >>> 8 & 1
        """
        return self.instance.getConfig()