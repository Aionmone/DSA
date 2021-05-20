# Queue implementation in Python

from typing import Any
from exceptions.queue import QueueEmpty, QueueFull

class Queue:
    """Queue data structure.
    
    Args:
        capacity: | default: None
            Init queue capacity.

    Methods:
        enqueue:
            Add new data to queue.
        dequeue:
            Return first item in queue and remove it.
        display:
            Return string representation of current queue.
        isEmpty:
            Checks if queue is empty or not.
        isFull:
            Checks if queue is full or not.

    Properties:
        capacity:
            Get/Set queue capacity.
        peek:
            Get first item in queue, None if empty.
    """

    def __init__(self, capacity= None):
        """Initiate Queue."""
        self.__queue = []
        self.__capacity =  capacity

    def __len__(self):
        """Return len(self)."""
        return len(self.__queue)

    def __str__(self) -> str:
        """Prints currunt queue."""
        return str(self.__queue)

    # Properties
    @property
    def capacity(self):
        """Get Queue capacity."""
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """Set Queue capacity."""
        self.__capacity = value

    @property
    def peek(self):
        """Shows first item in queue.
        
        Return:
            @any: first item in queue, None if empty.
        """
        if self.isEmpty():
            return None
        return self.__queue[0]

    def enqueue(self, item) -> None:
        """Add item to queue.
        
        Args:
            data: The data to be placed in queue.

        Raise:
            QueueFull:
                Indicates queue full capacity occupation.
        """
        if self.isFull():
            raise QueueFull
        self.__queue.append(item)

    def dequeue(self) -> Any:
        """Remove item from queue.
        
        Return:
            @any: The first item in queue.
        
        Raise:
            QueueEmpty:
                Indicates queue empty.
        """
        if self.isEmpty():
            raise QueueEmpty
        return self.__queue.pop(0)

    def display(self) -> str:
        """Returns self.
        
        Return:
            @str: String representation of queue.
        """
        return ", ".join(self.__queue())

    def isEmpty(self) -> bool:
        """Checks either Queue is empty or not.
        
        Return:
            @bool: True if empty, False otherwise.
        """
        if self.__queue:
            return False
        return True

    def isFull(self) -> bool:
        """Checks either Queue is full or not.
        
        Return:
            @bool: True if full, False otherwise.
        """
        if self.__capacity and len(self.__queue) >= self.__capacity:
            return True
        return False
