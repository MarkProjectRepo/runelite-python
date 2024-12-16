class TileObject:
    def __init__(self, instance):
        self.instance = instance

        # Inherit functions from the instance dynamically
        for attr in dir(instance):
            if callable(getattr(instance, attr)) and not attr.startswith("_"):
                setattr(self, attr, getattr(instance, attr))

    def get_hash(self):
        """Gets a bitfield containing various flags."""
        return self.instance.getHash()

    def get_x(self):
        """Gets the x-axis coordinate of the object in local context."""
        return self.instance.getX()

    def get_y(self):
        """Gets the y-axis coordinate of the object in local context."""
        return self.instance.getY()

    def get_z(self):
        """Gets the vertical coordinate of this object."""
        return self.instance.getZ()

    def get_plane(self):
        """Gets the plane of the tile that the object is on."""
        return self.instance.getPlane()

    def get_world_view(self):
        """Gets the WorldView this TileObject is a part of."""
        return self.instance.getWorldView()

    def get_id(self):
        """Gets the ID of the object."""
        return self.instance.getId()

    def get_world_location(self):
        """Get the world location for this object. For objects which are larger than 1 tile, this is the center most tile, rounded to the south-west."""
        return self.instance.getWorldLocation()

    def get_local_location(self):
        """Get the local location for this object. This point is the center point of the object."""
        return self.instance.getLocalLocation()

    def get_canvas_location(self, z_offset=None):
        """Calculates the position of the center of this tile on the canvas."""
        if z_offset is None:
            return self.instance.getCanvasLocation()
        else:
            return self.instance.getCanvasLocation(z_offset)

    def get_canvas_tile_poly(self):
        """Creates a polygon outlining the tile this object is on."""
        return self.instance.getCanvasTilePoly()

    def get_canvas_text_location(self, graphics, text, z_offset):
        """Calculates the canvas point to center `text` above the tile this object is on."""
        return self.instance.getCanvasTextLocation(graphics, text, z_offset)

    def get_minimap_location(self):
        """Gets a point on the canvas of where this objects mini-map indicator should appear."""
        return self.instance.getMinimapLocation()

    def get_clickbox(self):
        """Calculate the on-screen clickable area of the object."""
        return self.instance.getClickbox()
    
    def __bool__(self):
        return self.instance is not None
