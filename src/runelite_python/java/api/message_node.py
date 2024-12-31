from runelite_python.java.api.node import Node

class MessageNode(Node):
    """
    Represents a message in the chatbox.

    `net.runelite.api.MessageNode <https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/MessageNode.java>`_

    Methods:
        - get_id()
        - get_type()
        - get_name()
        - set_name(name)
        - get_sender()
        - set_sender(sender)
        - get_value()
        - set_value(value)
        - get_runelite_format_message()
        - set_runelite_format_message(message)
        - get_timestamp()
        - set_timestamp(timestamp)
    """

    def __init__(self, message_instance):
        super().__init__(message_instance)
        self.instance = message_instance

    def get_id(self) -> int:
        """
        Get the id for this message node.

        Returns:
            int: The message node ID
        """
        return self.instance.getId()

    def get_type(self):
        """
        Gets the type of message.

        Returns:
            ChatMessageType: the message type
        """
        return self.instance.getType()

    def get_name(self) -> str:
        """
        Gets the name of the player that sent the message.

        Returns:
            str: the player name
        """
        return self.instance.getName()

    def set_name(self, name: str) -> None:
        """
        Sets the name of the player that sent the message.

        Args:
            name (str): the new player name
        """
        self.instance.setName(name)

    def get_sender(self) -> str:
        """
        Gets the sender of the message. (ie. friends chat name)

        Returns:
            str: the message sender
        """
        return self.instance.getSender()

    def set_sender(self, sender: str) -> None:
        """
        Sets the sender of the message.

        Args:
            sender (str): the new message sender
        """
        self.instance.setSender(sender)

    def get_value(self) -> str:
        """
        Gets the message contents.

        Returns:
            str: the message contents
        """
        return self.instance.getValue()

    def set_value(self, value: str) -> None:
        """
        Sets the message contents.

        Args:
            value (str): the new message contents
        """
        self.instance.setValue(value)

    def get_runelite_format_message(self) -> str:
        """
        Gets the overriden message format.

        Returns:
            str: the message format
        """
        return self.instance.getRuneLiteFormatMessage()

    def set_runelite_format_message(self, runelite_format_message: str) -> None:
        """
        Sets the overriden message format.

        If this value is not null, the message contents as returned by
        get_value() will be replaced with the format set here
        when a message is processed.

        Args:
            runelite_format_message (str): the new message format
        """
        self.instance.setRuneLiteFormatMessage(runelite_format_message)

    def get_timestamp(self) -> int:
        """
        Get the timestamp for the message, in seconds from the unix epoch.

        Returns:
            int: The message timestamp
        """
        return self.instance.getTimestamp()

    def set_timestamp(self, timestamp: int) -> None:
        """
        Set the timestamp of the message.

        Args:
            timestamp (int): The new timestamp value
        """
        self.instance.setTimestamp(timestamp)

    def __bool__(self) -> bool:
        """
        Checks if the underlying Java instance is None.

        Returns:
            bool: True if the instance is None, False otherwise
        """
        return self.instance is not None