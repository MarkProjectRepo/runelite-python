from runelite_python.java.api.actor import Actor

class Player(Actor):  # Inherit from Actor
    """
    Represents a player entity in the game.

    `net.runelite.api.Player <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/Player.java>`_

    Methods:
        - get_id()
        - get_combat_level()
        - get_player_composition()
        - get_polygons()
        - get_team()
        - is_friends_chat_member()
        - is_friend()
        - is_clan_member()
        - get_overhead_icon()
        - get_skull_icon()
    """

    def __init__(self, player_instance):
        super().__init__(player_instance)
        self.instance = player_instance

    def get_id(self) -> int:
        """
        Gets the ID of the player.
        
        Returns:
            int: the ID of the player
        """
        return self.instance.getId()

    def get_combat_level(self) -> int:
        """
        Gets the combat level of the player.
        
        Returns:
            int: the combat level of the player
        """
        return self.instance.getCombatLevel()

    def get_player_composition(self):
        """
        Gets the composition of this player.
        
        Returns:
            PlayerComposition: the composition of the player
        """
        return self.instance.getPlayerComposition()

    def get_polygons(self):
        """
        Gets the polygons that make up the player's model.
        
        Returns:
            list of Polygon: the model polygons
        """
        return self.instance.getPolygons()

    def get_team(self) -> int:
        """
        Gets the current team cape team number the player is on.
        
        Returns:
            int: team number, or 0 if not on any team
        """
        return self.instance.getTeam()

    def is_friends_chat_member(self) -> bool:
        """
        Checks whether this player is a member of the same friends chat as the local player.
        
        Returns:
            bool: True if the player is a friends chat member, False otherwise
        """
        return self.instance.isFriendsChatMember()

    def is_friend(self) -> bool:
        """
        Checks whether this player is a friend of the local player.
        
        Returns:
            bool: True if the player is a friend, False otherwise
        """
        return self.instance.isFriend()

    def is_clan_member(self) -> bool:
        """
        Checks whether the player is a member of the same clan as the local player.
        
        Returns:
            bool: True if the player is a clan member, False otherwise
        """
        return self.instance.isClanMember()

    def get_overhead_icon(self):
        """
        Gets the displayed overhead icon of the player.
        
        Returns:
            HeadIcon: the overhead icon
        """
        return self.instance.getOverheadIcon()

    def get_skull_icon(self):
        """
        Gets the displayed skull icon of the player. Only works on the local player.
        
        Returns:
            SkullIcon: the skull icon, or None if not applicable
        """
        return self.instance.getSkullIcon()
