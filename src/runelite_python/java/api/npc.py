from runelite_python.java.api.actor import Actor

class NPC(Actor):
    """
    Represents a non-player character in the game.

    `net.runelite.api.NPC <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/NPC.java>`_

    Methods:
        - get_id()
        - get_name()
        - get_combat_level()
        - get_index()
        - get_composition()
        - get_transformed_composition()
        - get_model_overrides()
        - get_chathead_overrides()
    """

    def __init__(self, npc_instance):
        super().__init__(npc_instance)
        self.npc_instance = npc_instance

    def get_id(self) -> int:
        """
        Gets the ID of the NPC.
        
        Returns:
            int: the ID of the NPC
        """
        return self.npc_instance.getId()

    def get_name(self) -> str:
        """
        Gets the name of the NPC.
        
        Returns:
            str: the name of the NPC
        """
        return self.npc_instance.getName()

    def get_combat_level(self) -> int:
        """
        Gets the combat level of the NPC.
        
        Returns:
            int: the combat level of the NPC
        """
        return self.npc_instance.getCombatLevel()

    def get_index(self) -> int:
        """
        Gets the index position of this NPC in the clients cached NPC array.
        
        Returns:
            int: the NPC index
        """
        return self.npc_instance.getIndex()

    def get_composition(self):
        """
        Gets the composition of this NPC.
        
        Returns:
            NPCComposition: the composition
        """
        return self.npc_instance.getComposition()

    def get_transformed_composition(self):
        """
        Get the composition for this NPC and transform it if required.
        
        Returns:
            Optional[NPCComposition]: the transformed NPC
        """
        return self.npc_instance.getTransformedComposition()

    def get_model_overrides(self):
        """
        Gets model overrides for the NPC.
        
        Returns:
            Optional[NpcOverrides]: the model overrides
        """
        return self.npc_instance.getModelOverrides()

    def get_chathead_overrides(self):
        """
        Gets chathead overrides for the NPC.
        
        Returns:
            Optional[NpcOverrides]: the chathead overrides
        """
        return self.npc_instance.getChatheadOverrides()