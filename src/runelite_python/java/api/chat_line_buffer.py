from runelite_python.java.helpers import wrap_iterator
from runelite_python.java.api.message_node import MessageNode

class ChatLineBuffer:
    """
    Represents the buffer containing all messages in the chatbox.

    `net.runelite.api.ChatLineBuffer <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/ChatLineBuffer.java>`_

    Methods:
        - get_lines()
        - get_length()
        - remove_message_node(node)
    """

    def __init__(self, buffer_instance):
        self.instance = buffer_instance

    @wrap_iterator(MessageNode)
    def get_lines(self):
        """
        Gets an array of message nodes currently in the chatbox.

        Returns:
            list[MessageNode]: messages in the chatbox
        """
        return self.instance.getLines()

    def get_length(self) -> int:
        """
        Gets the length of the get_lines() array.

        Returns:
            int: the length
        """
        return self.instance.getLength()

    def remove_message_node(self, node: MessageNode) -> None:
        """
        Removes a message node.

        This method modifies the underlying MessageNode array. If removing multiple MessageNodes at a time,
        clone the original get_lines() array; as items in the array will get modified and be left in an
        inconsistent state.

        Args:
            node (MessageNode): the MessageNode to remove
        """
        self.instance.removeMessageNode(node.instance)
