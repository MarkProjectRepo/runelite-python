from typing import Callable, Optional
from runelite_python.java.helpers import wrap_getter
from runelite_python.java.api.menu import Menu
# from runelite_python.java.api.widget import Widget
from runelite_python.java.api.npc import NPC
from runelite_python.java.api.player import Player
from runelite_python.java.api.actor import Actor

class MenuEntry:
    """
    A menu entry in a right-click menu.

    `net.runelite.api.MenuEntry <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/MenuEntry.java>`_

    Methods:
        - get_option()
        - set_option(option)
        - get_target()
        - set_target(target)
        - get_identifier()
        - set_identifier(identifier)
        - get_type()
        - set_type(type)
        - get_param0()
        - set_param0(param0)
        - get_param1()
        - set_param1(param1)
        - is_force_left_click()
        - set_force_left_click(force_left_click)
        - get_world_view_id()
        - set_world_view_id(world_view_id)
        - is_deprioritized()
        - set_deprioritized(deprioritized)
        - on_click(callback)
        - is_item_op()
        - get_item_op()
        - get_item_id()
        - set_item_id(item_id)
        - get_widget()
        - get_npc()
        - get_player()
        - get_actor()
        - get_sub_menu()
        - create_sub_menu()
        - delete_sub_menu()
    """

    def __init__(self, entry_instance):
        self.instance = entry_instance

    def get_option(self) -> str:
        """
        The option text added to the menu. (ie. "Walk here", "Use")

        Returns:
            str: The menu option text
        """
        return self.instance.getOption()

    def set_option(self, option: str) -> 'MenuEntry':
        """
        Set the option text for the menu entry.

        Args:
            option (str): The menu option text

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setOption(option)
        return self

    def get_target(self) -> str:
        """
        The target of the action. (ie. Item or Actor name)
        If the option does not apply to any target, this field will be set to empty string.

        Returns:
            str: The target text
        """
        return self.instance.getTarget()

    def set_target(self, target: str) -> 'MenuEntry':
        """
        Set the target text for the menu entry.

        Args:
            target (str): The target text

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setTarget(target)
        return self

    def get_identifier(self) -> int:
        """
        An identifier value for the target of the action.

        Returns:
            int: The identifier value
        """
        return self.instance.getIdentifier()

    def set_identifier(self, identifier: int) -> 'MenuEntry':
        """
        Set the identifier value for the menu entry.

        Args:
            identifier (int): The identifier value

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setIdentifier(identifier)
        return self

    def get_type(self):
        """
        The action the entry will trigger.

        Returns:
            MenuAction: The menu action type
        """
        return self.instance.getType()

    def set_type(self, type) -> 'MenuEntry':
        """
        Set the action type for the menu entry.

        Args:
            type (MenuAction): The menu action type

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setType(type)
        return self

    def get_param0(self) -> int:
        """
        An additional parameter for the action.

        Returns:
            int: The first parameter value
        """
        return self.instance.getParam0()

    def set_param0(self, param0: int) -> 'MenuEntry':
        """
        Set the first parameter value for the menu entry.

        Args:
            param0 (int): The first parameter value

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setParam0(param0)
        return self

    def get_param1(self) -> int:
        """
        A second additional parameter for the action.

        Returns:
            int: The second parameter value
        """
        return self.instance.getParam1()

    def set_param1(self, param1: int) -> 'MenuEntry':
        """
        Set the second parameter value for the menu entry.

        Args:
            param1 (int): The second parameter value

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setParam1(param1)
        return self

    def is_force_left_click(self) -> bool:
        """
        If this is true and you have single mouse button on and this entry is
        the top entry the right click menu will not be opened when you left click.
        This is used for shift click.

        Returns:
            bool: True if force left click is enabled
        """
        return self.instance.isForceLeftClick()

    def set_force_left_click(self, force_left_click: bool) -> 'MenuEntry':
        """
        Set whether to force left click for this menu entry.

        Args:
            force_left_click (bool): Whether to force left click

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setForceLeftClick(force_left_click)
        return self

    def get_world_view_id(self) -> int:
        """
        Get the world view ID for this menu entry.

        Returns:
            int: The world view ID
        """
        return self.instance.getWorldViewId()

    def set_world_view_id(self, world_view_id: int) -> 'MenuEntry':
        """
        Set the world view ID for this menu entry.

        Args:
            world_view_id (int): The world view ID

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setWorldViewId(world_view_id)
        return self

    def is_deprioritized(self) -> bool:
        """
        Deprioritized menus are sorted in the menu to be below the other menu entries.

        Returns:
            bool: True if the menu entry is deprioritized
        """
        return self.instance.isDeprioritized()

    def set_deprioritized(self, deprioritized: bool) -> 'MenuEntry':
        """
        Set whether this menu entry should be deprioritized.

        Args:
            deprioritized (bool): Whether to deprioritize this entry

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setDeprioritized(deprioritized)
        return self

    def on_click(self, callback: Callable[['MenuEntry'], None]) -> 'MenuEntry':
        """
        Set a callback to be called when this menu option is clicked.

        Args:
            callback (Callable[[MenuEntry], None]): The callback function

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.onClick(lambda entry: callback(MenuEntry(entry)))
        return self

    def is_item_op(self) -> bool:
        """
        Test if this menu entry is an item op. "Use" and "Examine" are not considered item ops.

        Returns:
            bool: True if this is an item operation
        """
        return self.instance.isItemOp()

    def get_item_op(self) -> int:
        """
        If this menu entry is an item op, get the item op id.

        Returns:
            int: 1-5
        """
        return self.instance.getItemOp()

    def get_item_id(self) -> int:
        """
        Get the item id.

        Returns:
            int: The item ID
        """
        return self.instance.getItemId()

    def set_item_id(self, item_id: int) -> 'MenuEntry':
        """
        Set the item id.

        Args:
            item_id (int): The item ID

        Returns:
            MenuEntry: This menu entry instance
        """
        self.instance.setItemId(item_id)
        return self

    # @wrap_getter(Widget) TODO
    def get_widget(self):# -> Optional[Widget]:
        """
        Get the widget this menu entry is on, if this is a menu entry
        with an associated widget. Such as eg, CC_OP.

        Returns:
            Optional[Widget]: The associated widget, or None
        """
        return self.instance.getWidget()

    @wrap_getter(NPC)
    def get_npc(self) -> Optional[NPC]:
        """
        Get the NPC this menu entry is targeting, if any.

        Returns:
            Optional[NPC]: The targeted NPC, or None
        """
        return self.instance.getNpc()

    @wrap_getter(Player)
    def get_player(self) -> Optional[Player]:
        """
        Get the Player this menu entry is targeting, if any.

        Returns:
            Optional[Player]: The targeted Player, or None
        """
        return self.instance.getPlayer()

    @wrap_getter(Actor)
    def get_actor(self) -> Optional[Actor]:
        """
        Get the Actor this menu entry is targeting, if any.

        Returns:
            Optional[Actor]: The targeted Actor, or None
        """
        return self.instance.getActor()

    @wrap_getter(Menu)
    def get_sub_menu(self) -> Optional[Menu]:
        """
        Get the submenu for this menu entry.

        Returns:
            Optional[Menu]: The submenu, or None if one doesn't exist
        """
        return self.instance.getSubMenu()

    @wrap_getter(Menu)
    def create_sub_menu(self) -> Menu:
        """
        Create a new submenu for this menu entry.
        This will erase any previous submenu.

        Returns:
            Menu: The new submenu
        """
        return self.instance.createSubMenu()

    def delete_sub_menu(self) -> None:
        """
        Remove the submenu from this menu entry.
        """
        self.instance.deleteSubMenu()
