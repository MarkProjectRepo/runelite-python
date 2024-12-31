from runelite_python.runelite_data.subscriber import Subscriber
from typing import Callable

class MasterSubscriber(Subscriber):
    def update(self, data: dict):
        for action in self.actions:
            action(data)

    def add_action(self, fn: Callable):
        self.actions.append(fn)
