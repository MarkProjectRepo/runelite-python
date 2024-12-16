from runelite_python.java.api.tileobject import TileObject

class GroundObject(TileObject):
    def __init__(self, instance):
        self.instance = instance

        # Inherit functions from the instance dynamically
        for attr in dir(instance):
            if callable(getattr(instance, attr)) and not attr.startswith("__"):
                setattr(self, attr, getattr(instance, attr))

    def get_renderable(self):
        """
        Gets the renderable of the object.
        """
        return self.instance.getRenderable()

    def get_convex_hull(self):
        """
        Gets the convex hull of the object.
        """
        return self.instance.getConvexHull()

    def get_config(self):
        """
        Gets the config of the object.
        A bitfield containing various flags:
        <pre>{@code
            object type id = bits & 0x20
            orientation (0-3) = bits >>> 6 & 3
            supports items = bits >>> 8 & 1
        }</pre>
        """
        return self.instance.getConfig()
