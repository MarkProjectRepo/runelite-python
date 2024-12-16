class Skill:
    """
    An enumeration of skills that a player can level.

    `net.runelite.api.Skill <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/Skill.java>`_

    Attributes:
        ATTACK
        DEFENCE
        STRENGTH
        HITPOINTS
        RANGED
        PRAYER
        MAGIC
        COOKING
        WOODCUTTING
        FLETCHING
        FISHING
        FIREMAKING
        CRAFTING
        SMITHING
        MINING
        HERBLORE
        AGILITY
        THIEVING
        SLAYER
        FARMING
        RUNECRAFT
        HUNTER
        CONSTRUCTION
    """

    def __init__(self, skill_instance):
        """
        Initialize the Skill wrapper.

        Args:
            skill_instance: The Java Skill enum instance to wrap
        """
        self.instance = skill_instance

    def get_name(self) -> str:
        """
        Gets the name of the skill.

        Returns:
            str: the skill name
        """
        return self.instance.getName()

    def __str__(self) -> str:
        """
        Returns the string representation of the skill.

        Returns:
            str: the skill name
        """
        return self.get_name()

    def __eq__(self, other):
        """
        Compares this skill with another skill for equality.

        Args:
            other: The other skill to compare with

        Returns:
            bool: True if the skills are equal, False otherwise
        """
        if isinstance(other, Skill):
            return self.instance.equals(other.instance)
        return False

    def __hash__(self):
        """
        Returns the hash code of this skill.

        Returns:
            int: the hash code
        """
        return hash(self.instance)
