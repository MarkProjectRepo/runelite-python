from abc import ABC, abstractmethod

class Publisher(ABC):
    def __init__(self, delay=1):
        self._subscribers = set()
        self.delay = delay
        self.num_updates = 1

    def add_subscriber(self, subscriber):
        """Add a subscriber."""
        self._subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        """Remove a subscriber."""
        self._subscribers.discard(subscriber)
    
    @abstractmethod
    def get_message(self):
        pass

    def prepare_message(self):
        if self.num_updates % self.delay == 0:
            self.last_msg = self.get_message()
            self.num_updates = 1
        return self.last_msg

    def publish(self):
        message = self.prepare_message()

        for subscriber in self._subscribers:
            subscriber.update(message)
        self.num_updates += 1
