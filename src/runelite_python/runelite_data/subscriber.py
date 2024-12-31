from abc import ABC, abstractmethod

class Subscriber(ABC):
    def __init__(self):
        self.actions = []

    @abstractmethod
    def update(self, message):
        """Receive update with a message."""
        pass

    