from typing import Optional

class Node:
    """
    Represents a doubly linked node.

    `net.runelite.api.Node <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/Node.java>`_

    Methods:
        - get_next()
        - get_previous()
        - get_hash()
    """

    def __init__(self, node_instance):
        self.instance = node_instance

    def get_next(self) -> Optional['Node']:
        """
        Gets the next node.

        Returns:
            Optional[Node]: the next node, or None if there isn't one
        """
        next_node = self.instance.getNext()
        return Node(next_node) if next_node is not None else None

    def get_previous(self) -> Optional['Node']:
        """
        Gets the previous node.

        Returns:
            Optional[Node]: the previous node, or None if there isn't one
        """
        prev_node = self.instance.getPrevious()
        return Node(prev_node) if prev_node is not None else None

    def get_hash(self) -> int:
        """
        Gets the hash value of the node.

        Returns:
            int: the hash value
        """
        return self.instance.getHash()
