from typing import Iterator
from runelite_python.java.api.actor import Actor

class ClickQueue:
    def __init__(self, click_queue_instance):
        self.click_queue = click_queue_instance

    def add(self, x: int, y: int):
        self.click_queue.add(x, y)

    def clear(self):
        self.click_queue.clear()

    def is_empty(self) -> bool:
        return self.click_queue.isEmpty()

    def size(self) -> int:
        return self.click_queue.size()
    
    def iterator(self, object_type = None):
        if object_type is None:
            return self.click_queue.iterator()
        else:
            return [object_type(obj) for obj in self.click_queue.iterator()]
    
    def __iter__(self) -> Iterator[Actor]:
        return self.click_queue.iterator()