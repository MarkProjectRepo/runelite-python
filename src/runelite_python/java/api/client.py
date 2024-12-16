from typing import List, Optional, Dict, Tuple

from runelite_python.java.api.player import Player
from runelite_python.java.api.npc import NPC
from runelite_python.java.api.scene import Scene
from runelite_python.java.api.tile import Tile
from runelite_python.java.api.world_view import WorldView
from runelite_python.java.api.world import World
from runelite_python.java.api.grandexchange import GrandExchangeOffer
from runelite_python.java.api.coord.localpoint import LocalPoint
from runelite_python.java.api.coord.worldpoint import WorldPoint
from runelite_python.java.helpers import wrap_getter

class Client:
    """
    Wrapper for the RuneScape client.
    """

    def __init__(self, client):
        self.client = client

    def get_callbacks(self):
        """
        The injected client invokes these callbacks to send events to us.

        Returns:
            Callbacks: The client callbacks.
        """
        return self.client.getCallbacks()

    def get_draw_callbacks(self):
        """
        The injected client invokes these callbacks for scene drawing, which is
        used by the gpu plugin to override the client's normal scene drawing code.

        Returns:
            DrawCallbacks: The draw callbacks.
        """
        return self.client.getDrawCallbacks()

    def set_draw_callbacks(self, draw_callbacks):
        """
        Sets the draw callbacks.

        Args:
            draw_callbacks (DrawCallbacks): The draw callbacks to set.
        """
        self.client.setDrawCallbacks(draw_callbacks)

    def get_build_id(self):
        """
        Gets the build ID of the client.

        Returns:
            str: The build ID.
        """
        return self.client.getBuildID()

    def get_boosted_skill_level(self, skill):
        """
        Gets the current modified level of a skill.

        Args:
            skill (Skill): The skill to get the boosted level for.

        Returns:
            int: The modified skill level.
        """
        return self.client.getBoostedSkillLevel(skill)

    def get_real_skill_level(self, skill):
        """
        Gets the real level of a skill.

        Args:
            skill (Skill): The skill to get the real level for.

        Returns:
            int: The real skill level.
        """
        return self.client.getRealSkillLevel(skill)

    def get_total_level(self):
        """
        Calculates the total level from real skill levels.

        Returns:
            int: The total level.
        """
        return self.client.getTotalLevel()

    def add_chat_message(self, type, name, message, sender, post_event=True):
        """
        Adds a new chat message to the chatbox.

        Args:
            type (ChatMessageType): The type of message.
            name (str): The name of the player that sent the message.
            message (str): The message contents.
            sender (str): The sender/channel name.
            post_event (bool, optional): Whether to post the chat message event. Defaults to True.

        Returns:
            MessageNode: The message node for the message.
        """
        return self.client.addChatMessage(type, name, message, sender, post_event)

    def get_game_state(self):
        """
        Gets the current game state.

        Returns:
            GameState: The current game state.
        """
        return self.client.getGameState()

    def set_game_state(self, game_state):
        """
        Sets the current game state.

        Args:
            game_state (GameState): The game state to set.
        """
        self.client.setGameState(game_state)

    def stop_now(self):
        """
        Causes the client to shutdown. It is faster than
        java.applet.Applet.stop() because it doesn't wait for 4000ms.
        This will call System.exit() when it is done.
        """
        self.client.stopNow()

    def get_launcher_display_name(self) -> Optional[str]:
        """
        Gets the display name of the active account when launched from the Jagex launcher.

        Returns:
            Optional[str]: The active account's display name, or None if not launched from the Jagex launcher.
        """
        return self.client.getLauncherDisplayName()

    def get_username(self) -> str:
        """
        DEPRECATED. See get_account_hash instead.
        Gets the current logged in username.

        Returns:
            str: The logged in username.
        """
        return self.client.getUsername()

    def set_username(self, name: str):
        """
        Sets the current logged in username.

        Args:
            name (str): The logged in username.
        """
        self.client.setUsername(name)

    def set_password(self, password: str):
        """
        Sets the password on login screen.

        Args:
            password (str): The login screen password.
        """
        self.client.setPassword(password)

    def set_otp(self, otp: str):
        """
        Sets the 6 digit pin used for authenticator on login screen.

        Args:
            otp (str): One time password.
        """
        self.client.setOtp(otp)

    def get_current_login_field(self) -> int:
        """
        Gets currently selected login field. 0 is username, and 1 is password.

        Returns:
            int: Currently selected login field.
        """
        return self.client.getCurrentLoginField()

    def get_login_index(self) -> int:
        """
        Gets index of current login state. 2 is username/password form, 4 is authenticator form.

        Returns:
            int: Current login state index.
        """
        return self.client.getLoginIndex()

    def get_account_type(self):
        """
        Gets the account type of the logged in player.

        Returns:
            AccountType: The account type.

        Deprecated:
            See Varbits.ACCOUNT_TYPE
        """
        return self.client.getAccountType()

    def get_canvas(self):
        """
        Gets the game canvas.

        Returns:
            Canvas: The game canvas.
        """
        return self.client.getCanvas()

    def get_fps(self) -> int:
        """
        Gets the current FPS (frames per second).

        Returns:
            int: The FPS.
        """
        return self.client.getFPS()

    def get_camera_x(self) -> int:
        """
        Gets the x-axis coordinate of the camera.
        This value is a local coordinate value similar to get_local_destination_location().

        Returns:
            int: The camera x coordinate.
        """
        return self.client.getCameraX()

    def get_camera_fp_x(self) -> float:
        """
        Floating point camera position, x-axis.

        Returns:
            float: The camera x coordinate as a float.
        """
        return self.client.getCameraFpX()

    def get_camera_y(self) -> int:
        """
        Gets the y-axis coordinate of the camera.
        This value is a local coordinate value similar to get_local_destination_location().

        Returns:
            int: The camera y coordinate.
        """
        return self.client.getCameraY()

    def get_camera_fp_y(self) -> float:
        """
        Floating point camera position, y-axis.

        Returns:
            float: The camera y coordinate as a float.
        """
        return self.client.getCameraFpY()

    def get_camera_z(self) -> int:
        """
        Gets the z-axis coordinate of the camera.
        This value is a local coordinate value similar to get_local_destination_location().

        Returns:
            int: The camera z coordinate.
        """
        return self.client.getCameraZ()

    def get_camera_fp_z(self) -> float:
        """
        Floating point camera position, z-axis.

        Returns:
            float: The camera z coordinate as a float.
        """
        return self.client.getCameraFpZ()

    def get_camera_pitch(self) -> int:
        """
        Gets the pitch of the camera.
        The value returned by this method is measured in JAU, or Jagex Angle Unit, which is 1/1024 of a revolution.

        Returns:
            int: The camera pitch.
        """
        return self.client.getCameraPitch()

    def get_camera_fp_pitch(self) -> float:
        """
        Floating point camera pitch.

        Returns:
            float: The camera pitch as a float.
        """
        return self.client.getCameraFpPitch()

    def get_camera_yaw(self) -> int:
        """
        Gets the yaw of the camera.

        Returns:
            int: The camera yaw.
        """
        return self.client.getCameraYaw()

    def get_camera_fp_yaw(self) -> float:
        """
        Floating point camera yaw.

        Returns:
            float: The camera yaw as a float.
        """
        return self.client.getCameraFpYaw()

    def get_world(self) -> int:
        """
        Gets the current world number of the logged in player.

        Returns:
            int: The logged in world number.
        """
        return self.client.getWorld()

    def get_canvas_height(self) -> int:
        """
        Gets the canvas height.

        Returns:
            int: The canvas height.
        """
        return self.client.getCanvasHeight()

    def get_canvas_width(self) -> int:
        """
        Gets the canvas width.

        Returns:
            int: The canvas width.
        """
        return self.client.getCanvasWidth()

    def get_viewport_height(self) -> int:
        """
        Gets the height of the viewport.

        Returns:
            int: The viewport height.
        """
        return self.client.getViewportHeight()

    def get_viewport_width(self) -> int:
        """
        Gets the width of the viewport.

        Returns:
            int: The viewport width.
        """
        return self.client.getViewportWidth()

    def get_viewport_x_offset(self) -> int:
        """
        Gets the x-axis offset of the viewport.

        Returns:
            int: The x-axis offset.
        """
        return self.client.getViewportXOffset()

    def get_viewport_y_offset(self) -> int:
        """
        Gets the y-axis offset of the viewport.

        Returns:
            int: The y-axis offset.
        """
        return self.client.getViewportYOffset()

    def get_scale(self) -> int:
        """
        Gets the scale of the world (zoom value).

        Returns:
            int: The world scale.
        """
        return self.client.getScale()

    def get_mouse_canvas_position(self) -> Tuple[int, int]:
        """
        Gets the current position of the mouse on the canvas.

        Returns:
            Tuple[int, int]: The mouse canvas position as (x, y).
        """
        point = self.client.getMouseCanvasPosition()
        return (point.getX(), point.getY())

    def get_local_player(self) -> Optional[Player]:
        """
        Gets the logged in player instance.

        Returns:
            Optional[Player]: The logged in player, or None if not logged in.
        """
        player = self.client.getLocalPlayer()
        return Player(player) if player else None

    def get_follower(self) -> Optional[NPC]:
        """
        Get the local player's follower, such as a pet.

        Returns:
            Optional[NPC]: The follower NPC, or None if no follower.
        """
        npc = self.client.getFollower()
        return NPC(npc) if npc else None

    def get_item_definition(self, id: int):
        """
        Gets the item composition corresponding to an item's ID.

        Args:
            id (int): The item ID.

        Returns:
            ItemComposition: The corresponding item composition.
        """
        return self.client.getItemDefinition(id)

    # def create_item_sprite(self, item_id: int, quantity: int, border: int, shadow_color: int, 
    #                        stackable: int, noted: bool, scale: int) -> Optional[SpritePixels]:
    #     """
    #     Creates an item icon sprite with passed variables.

    #     Args:
    #         item_id (int): The item ID.
    #         quantity (int): The item quantity.
    #         border (int): Whether to draw a border.
    #         shadow_color (int): The shadow color.
    #         stackable (int): Whether the item is stackable.
    #         noted (bool): Whether the item is noted.
    #         scale (int): The scale of the sprite.

    #     Returns:
    #         Optional[SpritePixels]: The created sprite, or None if creation failed.
    #     """
    #     sprite = self.client.createItemSprite(item_id, quantity, border, shadow_color, stackable, noted, scale)
    #     return SpritePixels(sprite) if sprite else None

    def get_item_model_cache(self):
        """
        Get the item model cache. These models are used for drawing widgets of type MODEL
        and inventory item icons.

        Returns:
            NodeCache: The item model cache.
        """
        return self.client.getItemModelCache()

    def get_item_sprite_cache(self):
        """
        Get the item sprite cache. These are 2d SpritePixels which are used to raster item images on the inventory and
        on widgets of type GRAPHIC.

        Returns:
            NodeCache: The item sprite cache.
        """
        return self.client.getItemSpriteCache()

    # def get_sprites(self, source, archive_id: int, file_id: int) -> Optional[List[SpritePixels]]:
    #     """
    #     Loads and creates the sprite images of the passed archive and file IDs.

    #     Args:
    #         source: The sprite index.
    #         archive_id (int): The sprites archive ID.
    #         file_id (int): The sprites file ID.

    #     Returns:
    #         Optional[List[SpritePixels]]: The sprite images of the file, or None if not found.
    #     """
    #     sprites = self.client.getSprites(source, archive_id, file_id)
    #     return [SpritePixels(sprite) for sprite in sprites] if sprites else None

    def get_index_sprites(self):
        """
        Gets the sprite index.

        Returns:
            IndexDataBase: The sprite index.
        """
        return self.client.getIndexSprites()

    def get_index_scripts(self):
        """
        Gets the script index.

        Returns:
            IndexDataBase: The script index.
        """
        return self.client.getIndexScripts()

    def get_index_config(self):
        """
        Gets the config index.

        Returns:
            IndexDataBase: The config index.
        """
        return self.client.getIndexConfig()

    def get_index(self, id: int):
        """
        Gets an index by id.

        Args:
            id (int): The index id.

        Returns:
            IndexDataBase: The index.
        """
        return self.client.getIndex(id)

    def get_mouse_current_button(self) -> int:
        """
        Gets the current mouse button that is pressed.

        Returns:
            int: The pressed mouse button.
        """
        return self.client.getMouseCurrentButton()

    def is_dragging_widget(self) -> bool:
        """
        Checks whether a widget is currently being dragged.

        Returns:
            bool: True if dragging a widget, False otherwise.
        """
        return self.client.isDraggingWidget()

    # def get_dragged_widget(self) -> Optional[Widget]:
    #     """
    #     Gets the widget currently being dragged.

    #     Returns:
    #         Optional[Widget]: The dragged widget, or None if not dragging any widget.
    #     """
    #     widget = self.client.getDraggedWidget()
    #     return Widget(widget) if widget else None

    # def get_dragged_on_widget(self) -> Optional[Widget]:
    #     """
    #     Gets the widget that is being dragged on.
    #     The widget being dragged has the DRAG flag set, and is the widget currently under the dragged widget.

    #     Returns:
    #         Optional[Widget]: The dragged on widget, or None if not dragging any widget.
    #     """
    #     widget = self.client.getDraggedOnWidget()
    #     return Widget(widget) if widget else None

    # def set_dragged_on_widget(self, widget: Widget):
    #     """
    #     Sets the widget that is being dragged on.

    #     Args:
    #         widget (Widget): The new dragged on widget.
    #     """
    #     self.client.setDraggedOnWidget(widget.widget_instance)

    def get_drag_time(self) -> int:
        """
        Get the number of client cycles the current dragged widget has been dragged for.

        Returns:
            int: The number of cycles the widget has been dragged.
        """
        return self.client.getDragTime()

    def get_top_level_interface_id(self) -> int:
        """
        Gets Interface ID of the root widget.

        Returns:
            int: The top level interface ID.
        """
        return self.client.getTopLevelInterfaceId()

    # def get_widget_roots(self) -> List[Widget]:
    #     """
    #     Gets the root widgets.

    #     Returns:
    #         List[Widget]: The root widgets.
    #     """
    #     return [Widget(widget) for widget in self.client.getWidgetRoots()]

    # def get_widget(self, group_id: int, child_id: int) -> Optional[Widget]:
    #     """
    #     Gets a widget by its raw group ID and child ID.

    #     Args:
    #         group_id (int): The group ID.
    #         child_id (int): The child widget ID.

    #     Returns:
    #         Optional[Widget]: The widget corresponding to the group and child pair, or None if not found.
    #     """
    #     widget = self.client.getWidget(group_id, child_id)
    #     return Widget(widget) if widget else None

    # def get_widget_by_component_id(self, component_id: int) -> Optional[Widget]:
    #     """
    #     Gets a widget by its component id.

    #     Args:
    #         component_id (int): The component id.

    #     Returns:
    #         Optional[Widget]: The widget, or None if not found.
    #     """
    #     widget = self.client.getWidget(component_id)
    #     return Widget(widget) if widget else None

    def get_widget_positions_x(self) -> List[int]:
        """
        Gets an array containing the x-axis canvas positions of all widgets.

        Returns:
            List[int]: Array of x-axis widget coordinates.
        """
        return self.client.getWidgetPositionsX()

    def get_widget_positions_y(self) -> List[int]:
        """
        Gets an array containing the y-axis canvas positions of all widgets.

        Returns:
            List[int]: Array of y-axis widget coordinates.
        """
        return self.client.getWidgetPositionsY()

    def get_energy(self) -> int:
        """
        Gets the current run energy of the logged in player.

        Returns:
            int: The run energy in units of 1/100th of an percentage.
        """
        return self.client.getEnergy()

    def get_weight(self) -> int:
        """
        Gets the current weight of the logged in player.

        Returns:
            int: The weight.
        """
        return self.client.getWeight()

    def get_player_options(self) -> List[str]:
        """
        Gets an array of options that can currently be used on other players.

        Returns:
            List[str]: An array of options.
        """
        return self.client.getPlayerOptions()

    def get_player_options_priorities(self) -> List[bool]:
        """
        Gets an array of whether an option is enabled or not.

        Returns:
            List[bool]: The option priorities.
        """
        return self.client.getPlayerOptionsPriorities()

    def get_player_menu_types(self) -> List[int]:
        """
        Gets an array of player menu types.

        Returns:
            List[int]: The player menu types.
        """
        return self.client.getPlayerMenuTypes()

    def get_world_list(self) -> List[World]:
        """
        Gets a list of all RuneScape worlds.

        Returns:
            List[World]: World list.
        """
        return [World(world) for world in self.client.getWorldList()]

    def get_menu(self):
        """
        Get the client menu.

        Returns:
            Menu: The client menu.
        """
        return self.client.getMenu()

    # def create_menu_entry(self, idx: int):
    #     """
    #     Create a new menu entry.

    #     Args:
    #         idx (int): The index to create the menu entry at. Accepts negative indexes eg. -1 inserts at the end.

    #     Returns:
    #         MenuEntry: The newly created menu entry.
    #     """
    #     return MenuEntry(self.client.createMenuEntry(idx))

    # def get_menu_entries(self) -> List[MenuEntry]:
    #     """
    #     Gets an array of currently open right-click menu entries that can be clicked and activated.

    #     Returns:
    #         List[MenuEntry]: Array of open menu entries.
    #     """
    #     return [MenuEntry(entry) for entry in self.client.getMenuEntries()]

    # def set_menu_entries(self, entries: List[MenuEntry]):
    #     """
    #     Sets the array of open menu entries.

    #     Args:
    #         entries (List[MenuEntry]): New array of open menu entries.
    #     """
    #     self.client.setMenuEntries([entry.menu_entry_instance for entry in entries])

    def is_menu_open(self) -> bool:
        """
        Checks whether a right-click menu is currently open.

        Returns:
            bool: True if a menu is open, False otherwise.
        """
        return self.client.isMenuOpen()

    def is_menu_scrollable(self) -> bool:
        """
        Returns whether the currently open menu is scrollable.

        Returns:
            bool: True if the menu is scrollable, False otherwise.
        """
        return self.client.isMenuScrollable()

    def get_menu_scroll(self) -> int:
        """
        Get the number of entries the currently open menu has been scrolled down.

        Returns:
            int: The number of entries scrolled.
        """
        return self.client.getMenuScroll()

    def set_menu_scroll(self, scroll: int):
        """
        Set the number of entries the currently open menu has been scrolled down.

        Args:
            scroll (int): The number of entries to scroll.
        """
        self.client.setMenuScroll(scroll)

    def get_menu_x(self) -> int:
        """
        Get the menu x location. Only valid if the menu is open.

        Returns:
            int: The menu x location.
        """
        return self.client.getMenuX()

    def get_menu_y(self) -> int:
        """
        Get the menu y location. Only valid if the menu is open.

        Returns:
            int: The menu y location.
        """
        return self.client.getMenuY()

    def get_menu_height(self) -> int:
        """
        Get the menu height. Only valid if the menu is open.

        Returns:
            int: The menu height.
        """
        return self.client.getMenuHeight()

    def get_menu_width(self) -> int:
        """
        Get the menu width. Only valid if the menu is open.

        Returns:
            int: The menu width.
        """
        return self.client.getMenuWidth()

    def get_map_angle(self) -> int:
        """
        Gets the angle of the map, or target camera yaw.

        Returns:
            int: The map angle.
        """
        return self.client.getMapAngle()

    def is_resized(self) -> bool:
        """
        Checks whether the client window is currently resized.

        Returns:
            bool: True if resized, False otherwise.
        """
        return self.client.isResized()

    def get_revision(self) -> int:
        """
        Gets the client revision number.

        Returns:
            int: The revision.
        """
        return self.client.getRevision()

    def get_varps(self) -> List[int]:
        """
        Gets an array of all client varplayers.

        Returns:
            List[int]: Local player variables.
        """
        return self.client.getVarps()

    def get_server_varps(self) -> List[int]:
        """
        Get an array of all server varplayers. These vars are only
        modified by the server, and so represent the server's idea of
        the varp values.

        Returns:
            List[int]: The server varps.
        """
        return self.client.getServerVarps()

    def get_varc_map(self) -> Dict[int, object]:
        """
        Gets an array of all client variables.

        Returns:
            Dict[int, object]: The client variables.
        """
        return self.client.getVarcMap()

    def get_var(self, varbit: int) -> int:
        """
        Gets a value corresponding to the passed varbit.

        Args:
            varbit (int): The varbit id.

        Returns:
            int: The value.
        """
        return self.client.getVar(varbit)

    def get_varbit_value(self, varbit: int) -> int:
        """
        Gets the value of the given varbit.

        Args:
            varbit (int): The varbit id.

        Returns:
            int: The value.
        """
        return self.client.getVarbitValue(varbit)

    def get_server_varbit_value(self, varbit: int) -> int:
        """
        Gets the value of the given varbit.
        This returns the server's idea of the value, not the client's. This is
        specifically the last value set by the server regardless of changes to
        the var by the client.

        Args:
            varbit (int): The varbit id.

        Returns:
            int: The value.
        """
        return self.client.getServerVarbitValue(varbit)

    def get_varp_value(self, varp_id: int) -> int:
        """
        Gets the value of a given VarPlayer.

        Args:
            varp_id (int): The VarPlayer id.

        Returns:
            int: The value.
        """
        return self.client.getVarpValue(varp_id)

    def get_server_varp_value(self, varp_id: int) -> int:
        """
        Gets the value of a given VarPlayer.
        This returns the server's idea of the value, not the client's. This is
        specifically the last value set by the server regardless of changes to
        the var by the client.

        Args:
            varp_id (int): The VarPlayer id.

        Returns:
            int: The value.
        """
        return self.client.getServerVarpValue(varp_id)

    def get_varc_int_value(self, var: int) -> int:
        """
        Gets the value of a given VarClientInt.

        Args:
            var (int): The VarClientInt.

        Returns:
            int: The value.
        """
        return self.client.getVarcIntValue(var)

    def get_varc_str_value(self, var: int) -> str:
        """
        Gets the value of a given VarClientStr.

        Args:
            var (int): The VarClientStr.

        Returns:
            str: The value.
        """
        return self.client.getVarcStrValue(var)

    def set_varc_str_value(self, var: int, value: str):
        """
        Sets a VarClientString to the passed value.

        Args:
            var (int): The VarClientStr.
            value (str): The new value.
        """
        self.client.setVarcStrValue(var, value)

    def set_varc_int_value(self, var: int, value: int):
        """
        Sets a VarClientInt to the passed value.

        Args:
            var (int): The VarClientInt.
            value (int): The new value.
        """
        self.client.setVarcIntValue(var, value)

    def set_varbit(self, varbit: int, value: int):
        """
        Sets the value of a varbit.

        Args:
            varbit (int): The varbit id.
            value (int): The new value.
        """
        self.client.setVarbit(varbit, value)

    def get_varbit(self, id: int):
        """
        Gets the varbit composition for a given varbit id.

        Args:
            id (int): The varbit id.

        Returns:
            VarbitComposition: The varbit composition.
        """
        return self.client.getVarbit(id)

    def get_varbit_value(self, varps: List[int], varbit_id: int) -> int:
        """
        Gets the value of a given variable.

        Args:
            varps (List[int]): Passed varbits.
            varbit_id (int): The variable ID.

        Returns:
            int: The value.
        """
        return self.client.getVarbitValue(varps, varbit_id)

    def set_varbit_value(self, varps: List[int], varbit: int, value: int):
        """
        Sets the value of a given variable.

        Args:
            varps (List[int]): Passed varbits.
            varbit (int): The variable.
            value (int): The value.
        """
        self.client.setVarbitValue(varps, varbit, value)

    def queue_changed_varp(self, varp: int):
        """
        Mark the given varp as changed, causing var listeners to be
        triggered next tick.

        Args:
            varp (int): The varp to mark as changed.
        """
        self.client.queueChangedVarp(varp)

    def open_interface(self, component_id: int, interface_id: int, modal_mode: int):
        """
        Open an interface.

        Args:
            component_id (int): Component id to open the interface at.
            interface_id (int): The interface to open.
            modal_mode (int): See WidgetModalMode.

        Returns:
            WidgetNode: The WidgetNode for the interface.

        Raises:
            IllegalStateException: If the component does not exist or it not a layer, or the interface is already
            open on a different component.
        """
        return self.client.openInterface(component_id, interface_id, modal_mode)

    def close_interface(self, interface_node, unload: bool):
        """
        Close an interface.

        Args:
            interface_node (WidgetNode): The WidgetNode linking the interface into the component tree.
            unload (bool): Whether to null the client's widget table.

        Raises:
            IllegalArgumentException: If the interfaceNode is not linked into the component tree.
        """
        self.client.closeInterface(interface_node, unload)

    def get_widget_flags(self):
        """
        Gets the widget flags table.

        Returns:
            HashTable: The widget flags table.
        """
        return self.client.getWidgetFlags()

    def get_component_table(self):
        """
        Gets the widget node component table.

        Returns:
            HashTable: The widget node component table.
        """
        return self.client.getComponentTable()

    def get_grand_exchange_offers(self) -> List[GrandExchangeOffer]:
        """
        Gets an array of current grand exchange offers.

        Returns:
            List[GrandExchangeOffer]: All grand exchange offers.
        """
        return [GrandExchangeOffer(offer) for offer in self.client.getGrandExchangeOffers()]

    def is_prayer_active(self, prayer) -> bool:
        """
        Checks whether or not a prayer is currently active.

        Args:
            prayer (gateway.jvm.net.runelite.api.Prayer): The prayer.

        Returns:
            bool: True if the prayer is active, False otherwise.
        """
        return self.client.isPrayerActive(prayer)

    # def get_skill_experience(self, skill: Skill) -> int:
    #     """
    #     Gets the current experience towards a skill.

    #     Args:
    #         skill (Skill): The skill.

    #     Returns:
    #         int: The experience.
    #     """
    #     return self.client.getSkillExperience(skill)

    def get_overall_experience(self) -> int:
        """
        Get the total experience of the player.

        Returns:
            int: The total experience.
        """
        return self.client.getOverallExperience()

    def refresh_chat(self):
        """
        Refreshes the chat.
        """
        self.client.refreshChat()

    # def get_chat_line_map(self) -> Dict[int, ChatLineBuffer]:
    #     """
    #     Gets the map of chat buffers.

    #     Returns:
    #         Dict[int, ChatLineBuffer]: The chat buffers.
    #     """
    #     return self.client.getChatLineMap()

    def get_messages(self):
        """
        Map of message node id to message node.

        Returns:
            IterableHashTable: The map.
        """
        return self.client.getMessages()

    def get_object_definition(self, object_id: int):
        """
        Gets the object composition corresponding to an objects ID.

        Args:
            object_id (int): The object ID.

        Returns:
            ObjectComposition: The corresponding object composition.
        """
        return self.client.getObjectDefinition(object_id)

    def get_npc_definition(self, npc_id: int):
        """
        Gets the NPC composition corresponding to an NPCs ID.

        Args:
            npc_id (int): The NPC ID.

        Returns:
            NPCComposition: The corresponding NPC composition.
        """
        return self.client.getNpcDefinition(npc_id)

    def get_struct_composition(self, struct_id: int):
        """
        Gets the StructComposition for a given struct ID.

        Args:
            struct_id (int): The struct ID.

        Returns:
            StructComposition: The corresponding struct composition.
        """
        return self.client.getStructComposition(struct_id)

    def get_struct_composition_cache(self):
        """
        Gets the client's cache of in memory struct compositions.

        Returns:
            NodeCache: The struct composition cache.
        """
        return self.client.getStructCompositionCache()

    def get_db_table_field(self, row_id: int, column: int, tuple_index: int) -> List[object]:
        """
        Gets a entry out of a DBTable Row.

        Args:
            row_id (int): The row ID.
            column (int): The column.
            tuple_index (int): The tuple index.

        Returns:
            List[object]: The DB table field.
        """
        return self.client.getDBTableField(row_id, column, tuple_index)

    def get_db_row_config(self, row_id: int):
        """
        Gets the DBRowConfig for a given row ID.

        Args:
            row_id (int): The row ID.

        Returns:
            DBRowConfig: The corresponding DB row config.
        """
        return self.client.getDBRowConfig(row_id)

    def get_db_rows_by_value(self, table: int, column: int, tuple_index: int, value: object) -> List[int]:
        """
        Uses an index to find rows containing a certain value in a column.
        An index must exist for this column.

        Args:
            table (int): The table.
            column (int): The column.
            tuple_index (int): The tuple index.
            value (object): The value to search for.

        Returns:
            List[int]: The list of row IDs matching the value.
        """
        return self.client.getDBRowsByValue(table, column, tuple_index, value)

    def get_map_element_config(self, id: int):
        """
        Get a map element config by id.

        Args:
            id (int): The id.

        Returns:
            MapElementConfig: The map element config.
        """
        return self.client.getMapElementConfig(id)

    # def get_map_scene(self) -> List[IndexedSprite]:
    #     """
    #     Gets a sprite of the map scene.

    #     Returns:
    #         List[IndexedSprite]: The sprite.
    #     """
    #     return [IndexedSprite(sprite) for sprite in self.client.getMapScene()]

    # def get_map_dots(self) -> List[SpritePixels]:
    #     """
    #     Gets an array of currently drawn mini-map dots.

    #     Returns:
    #         List[SpritePixels]: All mini-map dots.
    #     """
    #     return [SpritePixels(sprite) for sprite in self.client.getMapDots()]

    def get_game_cycle(self) -> int:
        """
        Gets the local clients game cycle.
        Note: This value is incremented every 20ms.

        Returns:
            int: The game cycle.
        """
        return self.client.getGameCycle()

    # def get_map_icons(self) -> List[SpritePixels]:
    #     """
    #     Gets an array of current map icon sprites.

    #     Returns:
    #         List[SpritePixels]: The map icons.
    #     """
    #     return [SpritePixels(sprite) for sprite in self.client.getMapIcons()]

    # def get_mod_icons(self) -> List[IndexedSprite]:
    #     """
    #     Gets an array of mod icon sprites.

    #     Returns:
    #         List[IndexedSprite]: The mod icons.
    #     """
    #     return [IndexedSprite(sprite) for sprite in self.client.getModIcons()]

    # def set_mod_icons(self, mod_icons: List[IndexedSprite]):
    #     """
    #     Replaces the current mod icons with a new array.

    #     Args:
    #         mod_icons (List[IndexedSprite]): The new mod icons.
    #     """
    #     self.client.setModIcons([icon.indexed_sprite_instance for icon in mod_icons])

    # def create_indexed_sprite(self) -> IndexedSprite:
    #     """
    #     Creates an empty indexed sprite.

    #     Returns:
    #         IndexedSprite: The sprite.
    #     """
    #     return IndexedSprite(self.client.createIndexedSprite())

    # def create_sprite_pixels(self, pixels: List[int], width: int, height: int) -> SpritePixels:
    #     """
    #     Creates a sprite image with given width and height containing the pixels.

    #     Args:
    #         pixels (List[int]): The pixels.
    #         width (int): The width.
    #         height (int): The height.

    #     Returns:
    #         SpritePixels: The sprite image.
    #     """
    #     return SpritePixels(self.client.createSpritePixels(pixels, width, height))

    def get_local_destination_location(self) -> Optional[LocalPoint]:
        """
        Gets the location of the local player.

        Returns:
            Optional[LocalPoint]: The local player location.
        """
        local_point = self.client.getLocalDestinationLocation()
        return LocalPoint(local_point) if local_point else None

    def create_runelite_object(self):
        """
        Creates a RuneLiteObject, which is a modified GraphicsObject.

        Returns:
            RuneLiteObject: The created RuneLiteObject.
        """
        return self.client.createRuneLiteObject()

    # def load_model_data(self, id: int):
    #     """
    #     Loads an unlit model from the cache.

    #     Args:
    #         id (int): The ID of the model.

    #     Returns:
    #         ModelData: The model or None if it is loading or nonexistent.
    #     """
    #     model_data = self.client.loadModelData(id)
    #     return ModelData(model_data) if model_data else None

    # def merge_models(self, models: List[ModelData]) -> ModelData:
    #     """
    #     Merges multiple models.

    #     Args:
    #         models (List[ModelData]): The models to merge.

    #     Returns:
    #         ModelData: The merged model.
    #     """
    #     return ModelData(self.client.mergeModels([model.model_data_instance for model in models]))

    # def load_model(self, id: int):
    #     """
    #     Loads and lights a model from the cache.

    #     Args:
    #         id (int): The ID of the model.

    #     Returns:
    #         Model: The model or None if it is loading or nonexistent.
    #     """
    #     model = self.client.loadModel(id)
    #     return Model(model) if model else None

    # def load_model_with_recolor(self, id: int, color_to_find: List[int], color_to_replace: List[int]):
    #     """
    #     Loads a model from the cache and also recolors it.

    #     Args:
    #         id (int): The ID of the model.
    #         color_to_find (List[int]): Array of hsl color values to find in the model to replace.
    #         color_to_replace (List[int]): Array of hsl color values to replace in the model.

    #     Returns:
    #         Model: The model or None if it is loading or nonexistent.
    #     """
    #     model = self.client.loadModel(id, color_to_find, color_to_replace)
    #     return Model(model) if model else None

    def load_animation(self, id: int):
        """
        Loads an animation from the cache.

        Args:
            id (int): The ID of the animation.

        Returns:
            Animation: The loaded animation.
        """
        return self.client.loadAnimation(id)

    def get_music_volume(self) -> int:
        """
        Gets the music volume.

        Returns:
            int: Volume 0-255 inclusive.
        """
        return self.client.getMusicVolume()

    def set_music_volume(self, volume: int):
        """
        Sets the music volume.

        Args:
            volume (int): Volume 0-255 inclusive.
        """
        self.client.setMusicVolume(volume)

    def play_sound_effect(self, id: int, volume: int = None):
        """
        Play a sound effect at the player's current location.

        Args:
            id (int): The ID of the sound to play.
            volume (int, optional): The volume to play the sound effect at.
        """
        if volume is None:
            self.client.playSoundEffect(id)
        else:
            self.client.playSoundEffect(id, volume)

    def play_sound_effect_at_position(self, id: int, x: int, y: int, range: int, delay: int = 0):
        """
        Play a sound effect from some point in the world.

        Args:
            id (int): The ID of the sound to play.
            x (int): The ground coordinate on the x axis.
            y (int): The ground coordinate on the y axis.
            range (int): The number of tiles away that the sound can be heard from.
            delay (int, optional): The amount of frames before the sound starts playing.
        """
        self.client.playSoundEffect(id, x, y, range, delay)

    def get_buffer_provider(self):
        """
        Gets the clients graphic buffer provider.

        Returns:
            BufferProvider: The buffer provider.
        """
        return self.client.getBufferProvider()

    def get_mouse_idle_ticks(self) -> int:
        """
        Gets the amount of client ticks since the last mouse movement occurred.

        Returns:
            int: Amount of idle mouse ticks.
        """
        return self.client.getMouseIdleTicks()

    def get_mouse_last_pressed_millis(self) -> int:
        """
        Gets the time at which the last mouse press occurred in milliseconds since
        the UNIX epoch.

        Returns:
            int: The time of last mouse press.
        """
        return self.client.getMouseLastPressedMillis()

    def get_keyboard_idle_ticks(self) -> int:
        """
        Gets the amount of client ticks since the last keyboard press occurred.

        Returns:
            int: Amount of idle keyboard ticks.
        """
        return self.client.getKeyboardIdleTicks()

    def change_memory_mode(self, low_memory: bool):
        """
        Changes how game behaves based on memory mode. Low memory mode skips
        drawing of all floors and renders ground textures in low quality.

        Args:
            low_memory (bool): If we are running in low memory mode or not.
        """
        self.client.changeMemoryMode(low_memory)

    # def get_item_container(self, inventory_id: int) -> Optional[ItemContainer]:
    #     """
    #     Get the item container for an inventory.

    #     Args:
    #         inventory_id (int): The inventory ID.

    #     Returns:
    #         Optional[ItemContainer]: The item container, or None if not found.
    #     """
    #     container = self.client.getItemContainer(inventory_id)
    #     return ItemContainer(container) if container else None

    # def get_item_containers(self) -> Dict[int, ItemContainer]:
    #     """
    #     Get all item containers.

    #     Returns:
    #         Dict[int, ItemContainer]: A dictionary of all item containers.
    #     """
    #     return {k: ItemContainer(v) for k, v in self.client.getItemContainers().items()}

    def get_int_stack_size(self) -> int:
        """
        Gets the length of the cs2 vm's int stack.

        Returns:
            int: The int stack size.
        """
        return self.client.getIntStackSize()

    def set_int_stack_size(self, stack_size: int):
        """
        Sets the length of the cs2 vm's int stack.

        Args:
            stack_size (int): The new stack size.
        """
        self.client.setIntStackSize(stack_size)

    def get_int_stack(self) -> List[int]:
        """
        Gets the cs2 vm's int stack.

        Returns:
            List[int]: The int stack.
        """
        return self.client.getIntStack()

    def get_string_stack_size(self) -> int:
        """
        Gets the length of the cs2 vm's string stack.

        Returns:
            int: The string stack size.
        """
        return self.client.getStringStackSize()

    def set_string_stack_size(self, stack_size: int):
        """
        Sets the length of the cs2 vm's string stack.

        Args:
            stack_size (int): The new stack size.
        """
        self.client.setStringStackSize(stack_size)

    def get_string_stack(self) -> List[str]:
        """
        Gets the cs2 vm's string stack.

        Returns:
            List[str]: The string stack.
        """
        return self.client.getStringStack()

    def get_array_sizes(self, array_id: int) -> int:
        """
        Get the size of one of the cs2 vm's arrays.

        Args:
            array_id (int): The array id.

        Returns:
            int: The size of the array.
        """
        return self.client.getArraySizes(array_id)

    def get_array(self, array_id: int) -> List[int]:
        """
        Get one of the cs2 vm's arrays.

        Args:
            array_id (int): The array id.

        Returns:
            List[int]: The array.
        """
        return self.client.getArray(array_id)

    # def get_script_active_widget(self) -> Optional[Widget]:
    #     """
    #     Gets the cs2 vm's active widget.

    #     Returns:
    #         Optional[Widget]: The active widget, or None if not set.
    #     """
    #     widget = self.client.getScriptActiveWidget()
    #     return Widget(widget) if widget else None

    # def get_script_dot_widget(self) -> Optional[Widget]:
    #     """
    #     Gets the cs2 vm's "dot" widget.

    #     Returns:
    #         Optional[Widget]: The "dot" widget, or None if not set.
    #     """
    #     widget = self.client.getScriptDotWidget()
    #     return Widget(widget) if widget else None

    def is_friended(self, name: str, must_be_logged_in: bool) -> bool:
        """
        Checks whether a player is on the friends list.

        Args:
            name (str): The name of the player.
            must_be_logged_in (bool): If the player is online.

        Returns:
            bool: True if the player is friends, False otherwise.
        """
        return self.client.isFriended(name, must_be_logged_in)

    def get_friends_chat_manager(self):
        """
        Retrieve the friends chat manager.

        Returns:
            FriendsChatManager: The friends chat manager, or None if not available.
        """
        return self.client.getFriendsChatManager()

    def get_friend_container(self):
        """
        Retrieve the nameable container containing friends.

        Returns:
            FriendContainer: The friend container.
        """
        return self.client.getFriendContainer()

    def get_ignore_container(self):
        """
        Retrieve the nameable container containing ignores.

        Returns:
            NameableContainer: The ignore container.
        """
        return self.client.getIgnoreContainer()

    def get_preferences(self):
        """
        Gets the clients saved preferences.

        Returns:
            Preferences: The client preferences.
        """
        return self.client.getPreferences()

    def get_camera_yaw_target(self) -> int:
        """
        Get the target camera yaw.

        Returns:
            int: The target camera yaw.
        """
        return self.client.getCameraYawTarget()

    def get_camera_pitch_target(self) -> int:
        """
        Get the target camera pitch.

        Returns:
            int: The target camera pitch.
        """
        return self.client.getCameraPitchTarget()

    def set_camera_yaw_target(self, camera_yaw_target: int):
        """
        Set the target camera yaw.

        Args:
            camera_yaw_target (int): Target camera yaw.
        """
        self.client.setCameraYawTarget(camera_yaw_target)

    def set_camera_pitch_target(self, camera_pitch_target: int):
        """
        Set the target camera pitch.

        Args:
            camera_pitch_target (int): Target camera pitch.
        """
        self.client.setCameraPitchTarget(camera_pitch_target)
    def set_camera_speed(self, speed: float):
        """
        Sets the camera speed.

        Args:
            speed (float): The new camera speed.
        """
        self.client.setCameraSpeed(speed)

    def set_camera_mouse_button_mask(self, mask: int):
        """
        Sets the mask for which mouse buttons control the camera.

        Args:
            mask (int): The new mouse button mask.
        """
        self.client.setCameraMouseButtonMask(mask)

    def set_camera_pitch_relaxer_enabled(self, enabled: bool):
        """
        Sets whether the camera pitch can exceed the normal limits set
        by the RuneScape client.

        Args:
            enabled (bool): New camera pitch relaxer value.
        """
        self.client.setCameraPitchRelaxerEnabled(enabled)

    def set_invert_yaw(self, invert_yaw: bool):
        """
        Sets if the moving the camera horizontally should be backwards.

        Args:
            invert_yaw (bool): Whether to invert yaw.
        """
        self.client.setInvertYaw(invert_yaw)

    def set_invert_pitch(self, invert_pitch: bool):
        """
        Sets if the moving the camera vertically should be backwards.

        Args:
            invert_pitch (bool): Whether to invert pitch.
        """
        self.client.setInvertPitch(invert_pitch)

    def get_render_overview(self):
        """
        Gets the world map overview.

        Returns:
            RenderOverview: The world map overview.
        """
        return self.client.getRenderOverview()

    def get_world_map(self):
        """
        Get the world map.

        Returns:
            WorldMap: The world map.
        """
        return self.client.getWorldMap()

    def is_stretched_enabled(self) -> bool:
        """
        Checks whether the client is in stretched mode.

        Returns:
            bool: True if the client is in stretched mode, False otherwise.
        """
        return self.client.isStretchedEnabled()

    def set_stretched_enabled(self, state: bool):
        """
        Sets the client stretched mode state.

        Args:
            state (bool): New stretched mode state.
        """
        self.client.setStretchedEnabled(state)

    def is_stretched_fast(self) -> bool:
        """
        Checks whether the client is using fast rendering techniques when stretching the canvas.

        Returns:
            bool: True if stretching is fast rendering, False otherwise.
        """
        return self.client.isStretchedFast()

    def set_stretched_fast(self, state: bool):
        """
        Sets whether to use fast rendering techniques when stretching the canvas.

        Args:
            state (bool): New fast rendering state.
        """
        self.client.setStretchedFast(state)

    def set_stretched_integer_scaling(self, state: bool):
        """
        Sets whether to force integer scale factor by rounding scale
        factors towards zero when stretching.

        Args:
            state (bool): New integer scaling state.
        """
        self.client.setStretchedIntegerScaling(state)

    def set_stretched_keep_aspect_ratio(self, state: bool):
        """
        Sets whether to keep aspect ratio when stretching.

        Args:
            state (bool): New keep aspect ratio state.
        """
        self.client.setStretchedKeepAspectRatio(state)

    def set_scaling_factor(self, factor: int):
        """
        Sets the scaling factor when scaling resizable mode.

        Args:
            factor (int): New scaling factor.
        """
        self.client.setScalingFactor(factor)

    def invalidate_stretching(self, resize: bool):
        """
        Invalidates cached dimensions that are used for stretching and scaling.

        Args:
            resize (bool): True to tell the game to resize the canvas on the next frame, False otherwise.
        """
        self.client.invalidateStretching(resize)

    def get_stretched_dimensions(self) -> Tuple[int, int]:
        """
        Gets the current stretched dimensions of the client.

        Returns:
            Tuple[int, int]: The stretched dimensions (width, height).
        """
        dim = self.client.getStretchedDimensions()
        return (dim.width, dim.height)

    def get_real_dimensions(self) -> Tuple[int, int]:
        """
        Gets the real dimensions of the client before being stretched.

        Returns:
            Tuple[int, int]: The real dimensions (width, height).
        """
        dim = self.client.getRealDimensions()
        return (dim.width, dim.height)

    def change_world(self, world: World):
        """
        Changes the selected world to log in to.

        Args:
            world (World): The world to switch to.
        """
        self.client.changeWorld(world)

    def create_world(self) -> World:
        """
        Creates a new instance of a world.

        Returns:
            World: The newly created world.
        """
        return World(self.client.createWorld())

    # def draw_instance_map(self, z: int) -> SpritePixels:
    #     """
    #     Draws an instance map for the current viewed plane.

    #     Args:
    #         z (int): The plane.

    #     Returns:
    #         SpritePixels: The map sprite.
    #     """
    #     return SpritePixels(self.client.drawInstanceMap(z))

    def run_script(self, *args):
        """
        Executes a client script from the cache.

        Args:
            *args: The script id, then any additional arguments to execute the script with.
        """
        self.client.runScript(*args)

    def create_script_event(self, *args):
        """
        Creates a blank ScriptEvent for executing a ClientScript2 script.

        Args:
            *args: The script id, then any additional arguments to execute the script with.

        Returns:
            ScriptEvent: The created ScriptEvent.
        """
        return self.client.createScriptEvent(*args)

    def has_hint_arrow(self) -> bool:
        """
        Checks whether or not there is any active hint arrow.

        Returns:
            bool: True if there is a hint arrow, False otherwise.
        """
        return self.client.hasHintArrow()

    def get_hint_arrow_type(self) -> int:
        """
        Gets the type of hint arrow currently displayed.

        Returns:
            int: The hint arrow type.
        """
        return self.client.getHintArrowType()

    def clear_hint_arrow(self):
        """
        Clears the current hint arrow.
        """
        self.client.clearHintArrow()

    def set_hint_arrow(self, point_or_player_or_npc):
        """
        Sets a hint arrow to point to the passed location.

        Args:
            point_or_player_or_npc (Union[WorldPoint, LocalPoint, Player, NPC]): The target to point to.
        """
        if isinstance(point_or_player_or_npc, WorldPoint):
            self.client.setHintArrow(point_or_player_or_npc)
        elif isinstance(point_or_player_or_npc, LocalPoint):
            self.client.setHintArrow(point_or_player_or_npc)
        elif isinstance(point_or_player_or_npc, Player):
            self.client.setHintArrow(point_or_player_or_npc.player_instance)
        elif isinstance(point_or_player_or_npc, NPC):
            self.client.setHintArrow(point_or_player_or_npc.npc_instance)
        else:
            raise ValueError("Invalid argument type for set_hint_arrow")

    def get_hint_arrow_point(self) -> Optional[WorldPoint]:
        """
        Gets the world point that the hint arrow is directed at.

        Returns:
            Optional[WorldPoint]: Hint arrow target, or None if not set.
        """
        point = self.client.getHintArrowPoint()
        return WorldPoint(point) if point else None

    def get_hint_arrow_player(self) -> Optional[Player]:
        """
        Gets the player that the hint arrow is directed at.

        Returns:
            Optional[Player]: Hint arrow target, or None if not set.
        """
        player = self.client.getHintArrowPlayer()
        return Player(player) if player else None

    def get_hint_arrow_npc(self) -> Optional[NPC]:
        """
        Gets the NPC that the hint arrow is directed at.

        Returns:
            Optional[NPC]: Hint arrow target, or None if not set.
        """
        npc = self.client.getHintArrowNpc()
        return NPC(npc) if npc else None

    def get_animation_interpolation_filter(self):
        """
        Gets the animation interpolation filter.

        Returns:
            IntPredicate: The animation interpolation filter.
        """
        return self.client.getAnimationInterpolationFilter()

    def set_animation_interpolation_filter(self, filter):
        """
        Sets the animation interpolation filter.

        Args:
            filter (IntPredicate): The new animation interpolation filter.
        """
        self.client.setAnimationInterpolationFilter(filter)

    def get_boosted_skill_levels(self) -> List[int]:
        """
        Gets the boosted skill levels.

        Returns:
            List[int]: The boosted skill levels.
        """
        return self.client.getBoostedSkillLevels()

    def get_real_skill_levels(self) -> List[int]:
        """
        Gets the real skill levels.

        Returns:
            List[int]: The real skill levels.
        """
        return self.client.getRealSkillLevels()

    def get_skill_experiences(self) -> List[int]:
        """
        Gets the skill experiences.

        Returns:
            List[int]: The skill experiences.
        """
        return self.client.getSkillExperiences()

    # def queue_changed_skill(self, skill: Skill):
    #     """
    #     Queue a changed skill.

    #     Args:
    #         skill (Skill): The skill that changed.
    #     """
    #     self.client.queueChangedSkill(skill)

    # def get_sprite_overrides(self) -> Dict[int, SpritePixels]:
    #     """
    #     Gets a mapping of sprites to override.

    #     Returns:
    #         Dict[int, SpritePixels]: A mapping of sprite IDs to override sprites.
    #     """
    #     return {k: SpritePixels(v) for k, v in self.client.getSpriteOverrides().items()}

    # def get_widget_sprite_overrides(self) -> Dict[int, SpritePixels]:
    #     """
    #     Gets a mapping of widget sprites to override.

    #     Returns:
    #         Dict[int, SpritePixels]: A mapping of packed widget IDs to override sprites.
    #     """
    #     return {k: SpritePixels(v) for k, v in self.client.getWidgetSpriteOverrides().items()}

    # def set_compass(self, sprite_pixels: SpritePixels):
        """
        Sets the compass sprite.

        Args:
            sprite_pixels (SpritePixels): The new sprite.
        """
        self.client.setCompass(sprite_pixels.sprite_pixels_instance)

    def get_widget_sprite_cache(self):
        """
        Returns widget sprite cache, to be used with getSpriteOverrides().

        Returns:
            NodeCache: The cache.
        """
        return self.client.getWidgetSpriteCache()

    def get_tick_count(self) -> int:
        """
        Gets the current server tick count.

        Returns:
            int: The tick count.
        """
        return self.client.getTickCount()

    def set_tick_count(self, tick_count: int):
        """
        Sets the current server tick count.

        Args:
            tick_count (int): The new tick count.
        """
        self.client.setTickCount(tick_count)

    # def get_world_type(self) -> Set[WorldType]:
    #     """
    #     Gets a set of current world types that apply to the logged in world.

    #     Returns:
    #         Set[WorldType]: The types for current world.
    #     """
    #     return set(self.client.getWorldType())

    def get_camera_mode(self) -> int:
        """
        Get the camera mode.

        Returns:
            int: 0 for normal, 1 for free camera.
        """
        return self.client.getCameraMode()

    def set_camera_mode(self, mode: int):
        """
        Set the camera mode.

        Args:
            mode (int): 0 for normal, 1 for free camera.
        """
        self.client.setCameraMode(mode)

    def get_camera_focal_point_x(self) -> float:
        """
        Get the camera focus point x.

        Returns:
            float: The camera focus point x.
        """
        return self.client.getCameraFocalPointX()

    def set_camera_focal_point_x(self, x: float):
        """
        Sets the camera focus point x. Requires the getCameraMode() to be free camera.

        Args:
            x (float): The new camera focus point x.
        """
        self.client.setCameraFocalPointX(x)

    def get_camera_focal_point_y(self) -> float:
        """
        Get the camera focus point y.

        Returns:
            float: The camera focus point y.
        """
        return self.client.getCameraFocalPointY()

    def set_camera_focal_point_y(self, y: float):
        """
        Sets the camera focus point y. Requires the getCameraMode() to be free camera.

        Args:
            y (float): The new camera focus point y.
        """
        self.client.setCameraFocalPointY(y)

    def get_camera_focal_point_z(self) -> float:
        """
        Get the camera focus point z.

        Returns:
            float: The camera focus point z.
        """
        return self.client.getCameraFocalPointZ()

    def set_camera_focal_point_z(self, z: float):
        """
        Sets the camera focus point z. Requires the getCameraMode() to be free camera.

        Args:
            z (float): The new camera focus point z.
        """
        self.client.setCameraFocalPointZ(z)

    def set_free_camera_speed(self, speed: int):
        """
        Sets the normal moving speed when using oculus orb (default value is 12).

        Args:
            speed (int): The new camera speed.
        """
        self.client.setFreeCameraSpeed(speed)

    def open_world_hopper(self):
        """
        Opens in-game world hopper interface.
        """
        self.client.openWorldHopper()

    def hop_to_world(self, world: World):
        """
        Hops using in-game world hopper widget to another world.

        Args:
            world (World): Target world to hop to.
        """
        self.client.hopToWorld(world)

    def set_skybox_color(self, skybox_color: int):
        """
        Sets the RGB color of the skybox.

        Args:
            skybox_color (int): The RGB color of the skybox.
        """
        self.client.setSkyboxColor(skybox_color)

    def get_skybox_color(self) -> int:
        """
        Gets the RGB color of the skybox.

        Returns:
            int: The RGB color of the skybox.
        """
        return self.client.getSkyboxColor()

    def is_gpu(self) -> bool:
        """
        Checks if GPU is enabled.

        Returns:
            bool: True if GPU is enabled, False otherwise.
        """
        return self.client.isGpu()

    def set_gpu_flags(self, gpu_flags: int):
        """
        Sets GPU flags.

        Args:
            gpu_flags (int): The GPU flags to set.
        """
        self.client.setGpuFlags(gpu_flags)

    def set_expanded_map_loading(self, chunks: int):
        """
        Sets the expanded map loading.

        Args:
            chunks (int): The number of chunks to load.
        """
        self.client.setExpandedMapLoading(chunks)

    def get_expanded_map_loading(self) -> int:
        """
        Gets the expanded map loading.

        Returns:
            int: The number of chunks being loaded.
        """
        return self.client.getExpandedMapLoading()

    def get_3d_zoom(self) -> int:
        """
        Gets the 3D zoom value.

        Returns:
            int: The 3D zoom value.
        """
        return self.client.get3dZoom()

    def get_center_x(self) -> int:
        """
        Gets the center X coordinate.

        Returns:
            int: The center X coordinate.
        """
        return self.client.getCenterX()

    def get_center_y(self) -> int:
        """
        Gets the center Y coordinate.

        Returns:
            int: The center Y coordinate.
        """
        return self.client.getCenterY()

    def get_texture_provider(self):
        """
        Gets the texture provider.

        Returns:
            TextureProvider: The texture provider.
        """
        return self.client.getTextureProvider()

    def get_rasterizer_3d_clip_mid_x2(self) -> int:
        """
        Gets the Rasterizer3D clip mid X2 value.

        Returns:
            int: The Rasterizer3D clip mid X2 value.
        """
        return self.client.getRasterizer3D_clipMidX2()

    def get_rasterizer_3d_clip_negative_mid_x(self) -> int:
        """
        Gets the Rasterizer3D clip negative mid X value.

        Returns:
            int: The Rasterizer3D clip negative mid X value.
        """
        return self.client.getRasterizer3D_clipNegativeMidX()

    def get_rasterizer_3d_clip_negative_mid_y(self) -> int:
        """
        Gets the Rasterizer3D clip negative mid Y value.

        Returns:
            int: The Rasterizer3D clip negative mid Y value.
        """
        return self.client.getRasterizer3D_clipNegativeMidY()

    def get_rasterizer_3d_clip_mid_y2(self) -> int:
        """
        Gets the Rasterizer3D clip mid Y2 value.

        Returns:
            int: The Rasterizer3D clip mid Y2 value.
        """
        return self.client.getRasterizer3D_clipMidY2()

    def check_click_box(self, projection, model, orientation: int, x: int, y: int, z: int, hash: int):
        """
        Checks the clickbox of a model.

        Args:
            projection: The projection to use.
            model: The model to check.
            orientation (int): The orientation of the model.
            x (int): The x coordinate.
            y (int): The y coordinate.
            z (int): The z coordinate.
            hash (int): The hash of the model.
        """
        self.client.checkClickbox(projection, model, orientation, x, y, z, hash)

    def is_widget_selected(self) -> bool:
        """
        Checks if a widget is in target mode.

        Returns:
            bool: True if a widget is selected, False otherwise.
        """
        return self.client.isWidgetSelected()

    def set_widget_selected(self, selected: bool):
        """
        Sets if a widget is in target mode.

        Args:
            selected (bool): True to set widget as selected, False otherwise.
        """
        self.client.setWidgetSelected(selected)

    # def get_selected_widget(self) -> Optional[Widget]:
    #     """
    #     Get the selected widget, such as a selected spell or selected item (eg. "Use").

    #     Returns:
    #         Optional[Widget]: The selected widget, or None if no widget is selected.
    #     """
    #     widget = self.client.getSelectedWidget()
    #     return Widget(widget) if widget else None

    def get_item_composition_cache(self):
        """
        Returns client item composition cache.

        Returns:
            NodeCache: The item composition cache.
        """
        return self.client.getItemCompositionCache()

    def get_object_composition_cache(self):
        """
        Returns client object composition cache.

        Returns:
            NodeCache: The object composition cache.
        """
        return self.client.getObjectCompositionCache()

    def get_animation_cache(self):
        """
        Returns the client Animation cache.

        Returns:
            NodeCache: The animation cache.
        """
        return self.client.getAnimationCache()

    # def get_cross_sprites(self) -> List[SpritePixels]:
    #     """
    #     Returns the array of cross sprites that appear and animate when left-clicking.

    #     Returns:
    #         List[SpritePixels]: The cross sprites.
    #     """
    #     return [SpritePixels(sprite) for sprite in self.client.getCrossSprites()]

    def get_enum(self, id: int):
        """
        Gets the EnumComposition for a given enum ID.

        Args:
            id (int): The enum ID.

        Returns:
            EnumComposition: The corresponding enum composition.
        """
        return self.client.getEnum(id)

    def draw_2010_menu(self, alpha: int):
        """
        Draws a menu in the 2010 interface style.

        Args:
            alpha (int): Background transparency of the menu.
        """
        self.client.draw2010Menu(alpha)

    def draw_original_menu(self, alpha: int):
        """
        Draws a menu in the OSRS interface style.

        Args:
            alpha (int): Background transparency of the menu.
        """
        self.client.drawOriginalMenu(alpha)

    def reset_health_bar_caches(self):
        """
        Resets the health bar caches.
        """
        self.client.resetHealthBarCaches()

    def get_item_count(self) -> int:
        """
        Returns the max item index + 1 from cache.

        Returns:
            int: The max item index + 1.
        """
        return self.client.getItemCount()

    def set_all_widgets_are_op_targetable(self, value: bool):
        """
        Makes all widgets behave as if they are WIDGET_USE_TARGET.

        Args:
            value (bool): True to make all widgets targetable, False otherwise.
        """
        self.client.setAllWidgetsAreOpTargetable(value)

    def set_ge_search_result_count(self, count: int):
        """
        Sets the result count for GE search.

        Args:
            count (int): The result count to set.
        """
        self.client.setGeSearchResultCount(count)

    def set_ge_search_result_ids(self, ids: List[int]):
        """
        Sets the array of item ids for GE search.

        Args:
            ids (List[int]): The array of item ids to set.
        """
        self.client.setGeSearchResultIds(ids)

    def set_ge_search_result_index(self, index: int):
        """
        Sets the starting index in the item id array for GE search.

        Args:
            index (int): The starting index to set.
        """
        self.client.setGeSearchResultIndex(index)

    # def set_login_screen(self, pixels: SpritePixels):
    #     """
    #     Sets the image to be used for the login screen, provided as SpritePixels.
    #     If the image is larger than half the width of fixed mode,
    #     it won't get mirrored to the other side of the screen.

    #     Args:
    #         pixels (SpritePixels): The image to set for the login screen.
    #     """
    #     self.client.setLoginScreen(pixels.sprite_pixels_instance)

    def set_should_render_login_screen_fire(self, val: bool):
        """
        Sets whether the flames on the login screen should be rendered.

        Args:
            val (bool): True to render the flames, False otherwise.
        """
        self.client.setShouldRenderLoginScreenFire(val)

    def is_key_pressed(self, keycode: int) -> bool:
        """
        Test if a key is pressed.

        Args:
            keycode (int): The keycode.

        Returns:
            bool: True if the key is pressed, False otherwise.
        """
        return self.client.isKeyPressed(keycode)

    def get_cross_world_message_ids(self) -> List[int]:
        """
        Get the list of message ids for the recently received cross-world messages.
        The upper 32 bits of the id is the world id, the lower is a sequence number per-world.

        Returns:
            List[int]: The list of message ids.
        """
        return self.client.getCrossWorldMessageIds()

    def get_cross_world_message_ids_index(self) -> int:
        """
        Get the index of the next message to be inserted in the cross world message id list.

        Returns:
            int: The index of the next message.
        """
        return self.client.getCrossWorldMessageIdsIndex()

    def get_clan_channel(self):
        """
        Get the primary clan channel the player is in.

        Returns:
            ClanChannel: The clan channel, or None if not in a clan.
        """
        return self.client.getClanChannel()

    def get_guest_clan_channel(self):
        """
        Get the guest clan channel the player is in.

        Returns:
            ClanChannel: The guest clan channel, or None if not in a guest clan.
        """
        return self.client.getGuestClanChannel()

    def get_clan_settings(self):
        """
        Get clan settings for the clan the user is in.

        Returns:
            ClanSettings: The clan settings, or None if not in a clan.
        """
        return self.client.getClanSettings()

    def get_guest_clan_settings(self):
        """
        Get the guest clan's settings.

        Returns:
            ClanSettings: The guest clan settings, or None if not in a guest clan.
        """
        return self.client.getGuestClanSettings()

    def get_clan_channel_by_id(self, clan_id: int):
        """
        Get clan channel by id.

        Args:
            clan_id (int): The clan id.

        Returns:
            ClanChannel: The clan channel, or None if not found.
        """
        return self.client.getClanChannel(clan_id)

    def get_clan_settings_by_id(self, clan_id: int):
        """
        Get clan settings by id.

        Args:
            clan_id (int): The clan id.

        Returns:
            ClanSettings: The clan settings, or None if not found.
        """
        return self.client.getClanSettings(clan_id)

    def set_unlocked_fps(self, unlock: bool):
        """
        Sets whether the FPS should be unlocked.

        Args:
            unlock (bool): True to unlock FPS, False otherwise.
        """
        self.client.setUnlockedFps(unlock)

    def set_unlocked_fps_target(self, fps: int):
        """
        Sets the target FPS when FPS is unlocked.

        Args:
            fps (int): The target FPS.
        """
        self.client.setUnlockedFpsTarget(fps)

    # def get_ambient_sound_effects(self) -> List[AmbientSoundEffect]:
    #     """
    #     Gets the ambient sound effects.

    #     Returns:
    #         List[AmbientSoundEffect]: The ambient sound effects.
    #     """
    #     return list(self.client.getAmbientSoundEffects())

    def set_idle_timeout(self, ticks: int):
        """
        Set the amount of time until the client automatically logs out due to idle input.

        Args:
            ticks (int): Client ticks.
        """
        self.client.setIdleTimeout(ticks)

    def get_idle_timeout(self) -> int:
        """
        Get the amount of time until the client automatically logs out due to idle input.

        Returns:
            int: Client ticks.
        """
        return self.client.getIdleTimeout()

    def is_minimap_zoom(self) -> bool:
        """
        Get whether minimap zoom is enabled.

        Returns:
            bool: True if minimap zoom is enabled, False otherwise.
        """
        return self.client.isMinimapZoom()

    def set_minimap_zoom(self, minimap_zoom: bool):
        """
        Set whether minimap zoom is enabled.

        Args:
            minimap_zoom (bool): True to enable minimap zoom, False to disable.
        """
        self.client.setMinimapZoom(minimap_zoom)

    def get_minimap_zoom(self) -> float:
        """
        Gets the number of pixels per tile on the minimap. The default is 4.

        Returns:
            float: The number of pixels per tile on the minimap.
        """
        return self.client.getMinimapZoom()

    def set_minimap_zoom(self, zoom: float):
        """
        Set the number of pixels per tile on the minimap. The default is 4.

        Args:
            zoom (float): The new number of pixels per tile on the minimap.
        """
        self.client.setMinimapZoom(zoom)

    def set_minimap_tile_drawer(self, draw_tile):
        """
        Sets a callback to override the drawing of tiles on the minimap.
        Will be called per tile per frame.

        Args:
            draw_tile: The callback function to set.
        """
        self.client.setMinimapTileDrawer(draw_tile)

    def get_rasterizer(self):
        """
        Gets the rasterizer.

        Returns:
            Rasterizer: The rasterizer.
        """
        return self.client.getRasterizer()

    # def menu_action(self, p0: int, p1: int, action: MenuAction, id: int, item_id: int, option: str, target: str):
    #     """
    #     Perform an action on a menu.

    #     Args:
    #         p0 (int): First parameter.
    #         p1 (int): Second parameter.
    #         action (MenuAction): The action to perform.
    #         id (int): The ID.
    #         item_id (int): The item ID.
    #         option (str): The option.
    #         target (str): The target.
    #     """
    #     self.client.menuAction(p0, p1, action, id, item_id, option, target)

    def get_world_view(self, id: int) -> WorldView:
        """
        Get worldview by id.

        Args:
            id (int): id, or -1 for top level worldview

        Returns:
            WorldView: The world view for the given id.
        """
        return self.client.getWorldView(id)

    @wrap_getter(WorldView)
    def get_top_level_world_view(self) -> WorldView:
        """
        Get the top level world view.

        Returns:
            WorldView: The top level world view.
        """
        return self.client.getTopLevelWorldView()

    def is_camera_shake_disabled(self) -> bool:
        """
        Whether camera shaking effects are disabled at e.g. Barrows, ToA.

        Returns:
            bool: True if camera shake is disabled, False otherwise.
        """
        return self.client.isCameraShakeDisabled()

    def set_camera_shake_disabled(self, disabled: bool):
        """
        Set whether to disable camera shaking effects at e.g. Barrows, ToA.

        Args:
            disabled (bool): True to disable camera shake, False to enable.
        """
        self.client.setCameraShakeDisabled(disabled)

    def get_instance_template_chunks(self) -> List[List[List[int]]]:
        """
        Contains a 3D array of template chunks for instanced areas.

        Returns:
            List[List[List[int]]]: The array of instance template chunks.
        """
        return self.client.getInstanceTemplateChunks()

    def get_xtea_keys(self) -> List[List[int]]:
        """
        Returns a 2D array containing XTEA encryption keys used to decrypt map region files.

        Returns:
            List[List[int]]: The XTEA encryption keys.
        """
        return self.client.getXteaKeys()

    def is_in_instanced_region(self) -> bool:
        """
        Checks whether the scene is in an instanced region.

        Returns:
            bool: True if in an instanced region, False otherwise.
        """
        return self.client.isInInstancedRegion()

    def get_map_regions(self) -> List[int]:
        """
        Gets an array of map region IDs that are currently loaded.

        Returns:
            List[int]: The map regions.
        """
        return self.client.getMapRegions()

    @wrap_getter(Scene)
    def get_scene(self) -> Scene:
        """
        Gets the current scene.

        Returns:
            Scene: The current scene.
        """
        return self.client.getScene()

    def get_players(self) -> List[Player]:
        """
        Gets a list of all valid players from the player cache.

        Returns:
            List[Player]: A list of all players.
        """
        return self.client.getPlayers()

    def get_npcs(self) -> List[NPC]:
        """
        Gets a list of all valid NPCs from the NPC cache.

        Returns:
            List[NPC]: A list of all NPCs.
        """
        return self.client.getNpcs()

    def get_cached_npcs(self) -> List[NPC]:
        """
        Gets an array of all cached NPCs.

        Returns:
            List[NPC]: Cached NPCs.
        """
        return self.client.getCachedNPCs()

    def get_cached_players(self) -> List[Player]:
        """
        Gets an array of all cached players.

        Returns:
            List[Player]: Cached players.
        """
        return self.client.getCachedPlayers()

    # def get_collision_maps(self) -> List[CollisionData]:
    #     """
    #     Gets an array of tile collision data.

    #     Returns:
    #         List[CollisionData]: The collision data.
    #     """
    #     return self.client.getCollisionMaps()

    def get_plane(self) -> int:
        """
        Gets the current plane the player is on.

        Returns:
            int: The plane.
        """
        return self.client.getPlane()

    def get_tile_heights(self) -> List[List[List[int]]]:
        """
        Gets a 3D array containing the heights of tiles in the current scene.

        Returns:
            List[List[List[int]]]: The tile heights.
        """
        return self.client.getTileHeights()

    def get_tile_settings(self) -> List[List[List[int]]]:
        """
        Gets a 3D array containing the settings of tiles in the current scene.

        Returns:
            List[List[List[int]]]: The tile settings.
        """
        return self.client.getTileSettings()

    def get_base_x(self) -> int:
        """
        Returns the x-axis base coordinate.

        Returns:
            int: The base x-axis coordinate.
        """
        return self.client.getBaseX()

    def get_base_y(self) -> int:
        """
        Returns the y-axis base coordinate.

        Returns:
            int: The base y-axis coordinate.
        """
        return self.client.getBaseY()

    # def create_projectile(self, id: int, plane: int, start_x: int, start_y: int, start_z: int, start_cycle: int, 
    #                       end_cycle: int, slope: int, start_height: int, end_height: int, target: Actor, 
    #                       target_x: int, target_y: int) -> Projectile:
    #     """
    #     Create a projectile.

    #     Args:
    #         id (int): projectile/spotanim id
    #         plane (int): plane the projectile is on
    #         start_x (int): local x coordinate the projectile starts at
    #         start_y (int): local y coordinate the projectile starts at
    #         start_z (int): local z coordinate the projectile starts at - includes tile height
    #         start_cycle (int): cycle the project starts
    #         end_cycle (int): cycle the projectile ends
    #         slope (int): slope
    #         start_height (int): start height of projectile - excludes tile height
    #         end_height (int): end height of projectile - excludes tile height
    #         target (Actor): optional actor target
    #         target_x (int): target x - if an actor target is supplied should be the target x
    #         target_y (int): target y - if an actor target is supplied should be the target y

    #     Returns:
    #         Projectile: The new projectile.
    #     """
    #     return self.client.createProjectile(id, plane, start_x, start_y, start_z, start_cycle, end_cycle,
    #                                                  slope, start_height, end_height, target, target_x, target_y)

    # def get_projectiles(self) -> Deque[Projectile]:
    #     """
    #     Gets a list of all projectiles currently spawned.

    #     Returns:
    #         Deque[Projectile]: All projectiles.
    #     """
    #     return self.client.getProjectiles()

    # def get_graphics_objects(self) -> Deque[GraphicsObject]:
    #     """
    #     Gets a list of all graphics objects currently drawn.

    #     Returns:
    #         Deque[GraphicsObject]: All graphics objects.
    #     """
    #     return self.client.getGraphicsObjects()

    def get_selected_scene_tile(self) -> Optional[Tile]:
        """
        Gets the currently selected tile. (ie. last right clicked tile)

        Returns:
            Optional[Tile]: The selected tile, or None if no tile is selected.
        """
        return self.client.getSelectedSceneTile()