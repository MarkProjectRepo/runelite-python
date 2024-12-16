# Dedicated to retrieving information on the visible NPCs around the player
from runelite_python.java.api.world_view import WorldView
from runelite_python.java.api.actor import Actor

def get_npcs_by_proximity(world_view: WorldView, other: Actor):
    npcs = world_view.npcs()
    # print([npc for npc in npcs.iterator()])
    # Calculate distance from other object and sort actors by proximity
    actors_sorted_by_proximity = sorted(
        npcs,
        key=lambda x: other.get_local_location().distance_to(x.get_local_location())
    )

    return actors_sorted_by_proximity

def get_npc_by_id(world_view: WorldView, npc_id: int):
    npcs = world_view.npcs()
    for npc in npcs.iterator():
        if npc.get_id() == npc_id:
            return npc
    return None