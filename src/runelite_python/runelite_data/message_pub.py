from typing import Callable
from runelite_python.runelite_data.publisher import Publisher
from runelite_python.java.api.client import Client
from runelite_python.java.api.message_node import MessageNode


class MessagePublisher(Publisher):
    def __init__(self, 
                 client: Client, 
                 publisher_name: str = None, 
                 delay=1,
                 filter_func: Callable = None,
                 enum = None):
        super().__init__(delay)
        self.client = client
        self.publisher_name = publisher_name if publisher_name else self.__class__.__name__
        self.filter_func = filter_func
        self.chat_length = 0
        self.enum = enum

    def get_message(self):
        messages = self.client.get_messages()
        processed_messages = []
        try:
            for message in messages.iterator():
                message = MessageNode(message)
                name = self._clean_text(message.get_name())
                value = self._clean_text(message.get_value())
                sender = self._clean_text(message.get_sender())
                type = message.get_type()

                msg_data = {
                    "name": name,
                    "value": value,
                    "sender": sender,
                    "type": type
                }
                if self.filter_func and self.filter_func(msg_data):
                    processed_messages.append(msg_data)
                elif self.filter_func == None:
                    processed_messages.append(msg_data)
                
        except Exception as e:
            # print(f"Error processing messages: {e}")
            pass
        return processed_messages

    def _clean_text(self, text: str) -> str:
        """Clean chat text by removing formatting tags and special characters."""
        if not text:
            return text
            
        # Remove color tags
        if '<col' in text:
            text = text.split('>', 1)[1]
            
        # Remove image tags
        if '<img=' in text:
            text = text.split('>', 1)[1]
            
        # Remove non-breaking spaces
        text = text.replace('\xa0', ' ')
        
        return text.strip()
    
    def _message_type(self, sender: str, name: str) -> str:
        msg_type = ""
        if sender and name:
            msg_type = "clan_chat"
        elif sender and not name:
            msg_type = "clan_announcement"
        elif name:
            msg_type = "player_message"
        else:
            msg_type = "game_message"

        return msg_type

    def get_raw_messages(self):
        """Returns the raw message iterator from the client."""
        return self.client.get_messages()

    def refresh_chat(self):
        """Refreshes the chat display."""
        return self.client.refresh_chat()
    

class ChatPublisher(MessagePublisher):
    def __init__(self, client: Client, publisher_name: str = None, **kwargs):
        filter_func = lambda x: x['type'] == self.enum.PUBLICCHAT and x['name']
        super().__init__(client, publisher_name, 1, filter_func, **kwargs)
        self.chat_history = []
        self.MAX_CHAT_LENGTH = 100
        self.WINDOW_SIZE = 10  # Size of sliding window for comparison

    def get_message(self):
        messages = super().get_message()
        
        # If we've hit the chat limit, find the alignment using sliding window
        if len(messages) >= self.MAX_CHAT_LENGTH:
            alignment_index = self._find_alignment(messages)
            print(alignment_index)
            if alignment_index is not None:
                new_messages = messages[alignment_index:]
                self.chat_history = messages[-self.MAX_CHAT_LENGTH:]
                return '\n'.join([f"{m['name']}: {m['value']}" for m in new_messages])
            
        # If we haven't hit the limit or no alignment found, process normally
        new_messages = messages[self.chat_length:]
        self.chat_length = len(messages)
        self.chat_history = messages[-self.MAX_CHAT_LENGTH:]
        return '\n'.join([f"{m['name']}: {m['value']}" for m in new_messages])

    def _get_window_hash(self, messages, start_idx):
        """Generate a hash for a window of messages."""
        window = messages[start_idx:start_idx + self.WINDOW_SIZE]
        return hash(tuple(f"{m['name']}:{m['value']}" for m in window))

    def _find_alignment(self, current_messages):
        """Find alignment using sliding window hash comparison."""
        if not self.chat_history or len(current_messages) < self.WINDOW_SIZE:
            return None
            
        # Get hashes for all windows in history
        history_hashes = {
            self._get_window_hash(self.chat_history, i): i 
            for i in range(len(self.chat_history) - self.WINDOW_SIZE + 1)
        }
        
        # Slide window across current messages to find match
        for i in range(len(current_messages) - self.WINDOW_SIZE + 1):
            current_hash = self._get_window_hash(current_messages, i)
            if current_hash in history_hashes:
                return i
                
        return None

class ChatTest(MessagePublisher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_message(self):
        messages = self.client.get_chat_line_map().get(self.enum.PUBLICCHAT)
        print(messages)
        while True:
            # msg = messages.get(self.chat_length)
            # print(msg)
            if msg is None:
                # print(MessageNode(messages.get(self.chat_length-1)))
                self.chat_length += 1
                continue
            msg = MessageNode(msg)
            print(msg, self.chat_length)
            self.chat_length += 1
