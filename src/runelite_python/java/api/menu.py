from runelite_python.java.helpers import wrap_getter, wrap_iterator
from runelite_python.java.api.menu_entry import MenuEntry

class Menu:
    """
    Represents the client minimenu.

    `net.runelite.api.Menu <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/Menu.java>`_

    Methods:
        - create_menu_entry(idx)
        - get_menu_entries()
        - set_menu_entries(entries)
        - remove_menu_entry(entry)
        - get_menu_x()
        - get_menu_y()
        - get_menu_width()
        - get_menu_height()
    """

    def __init__(self, menu_instance):
        self.instance = menu_instance

    @wrap_getter(MenuEntry)
    def create_menu_entry(self, idx: int):
        """
        Create a new menu entry.

        Args:
            idx (int): the index to create the menu entry at. Accepts negative indexes eg. -1 inserts at the end.

        Returns:
            MenuEntry: the newly created menu entry
        """
        return self.instance.createMenuEntry(idx)

    @wrap_iterator(MenuEntry)
    def get_menu_entries(self):
        """
        Gets the current mini menu entries.

        Returns:
            list[MenuEntry]: array of menu entries
        """
        return self.instance.getMenuEntries()

    def set_menu_entries(self, entries):
        """
        Sets the array of menu entries.

        This method should typically be used in the context of the MenuOpened event,
        since setting the menu entries will be overwritten the next frame.

        Args:
            entries (list[MenuEntry]): new array of open menu entries
        """
        # Unwrap the MenuEntry instances to get the Java objects
        java_entries = [entry.instance for entry in entries]
        self.instance.setMenuEntries(java_entries)

    def remove_menu_entry(self, entry):
        """
        Remove a menu entry.

        Args:
            entry (MenuEntry): the menu entry to remove
        """
        self.instance.removeMenuEntry(entry.instance)

    def get_menu_x(self) -> int:
        """
        Get the menu x location. Only valid if the menu is open.

        Returns:
            int: the menu x location
        """
        return self.instance.getMenuX()

    def get_menu_y(self) -> int:
        """
        Get the menu y location. Only valid if the menu is open.

        Returns:
            int: the menu y location
        """
        return self.instance.getMenuY()

    def get_menu_width(self) -> int:
        """
        Get the menu width. Only valid if the menu is open.

        Returns:
            int: the menu width
        """
        return self.instance.getMenuWidth()

    def get_menu_height(self) -> int:
        """
        Get the menu height. Only valid if the menu is open.

        Returns:
            int: the menu height
        """
        return self.instance.getMenuHeight()
