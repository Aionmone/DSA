# Circular Queue implementation in Python

from exceptions.queue import QueueEmpty, QueueFull

class CircularQueue:

    def __init__(self, capacity= 10):
        """Initiate Queue"""
        self.__capacity =  capacity
        self.__queue = [None] * self.__capacity
        self.__head = self.__tail = -1

    def __len__(self):
        """Return len(self)"""
        return len(self.__queue)

    def __str__(self) -> str:
        """Prints currunt queue"""
        return str(self.__queue)

    # Properties
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def peek(self):
        """Shows first item in Queue"""
        if self.isEmpty():
            raise QueueEmpty

        return self.__queue[self.__head]

    def enqueue(self, item) -> None:
        """Add item to queue"""
        if self.isFull():
            raise QueueFull

        if self.__head == -1:
            self.__head = 0
            self.__tail = 0
            self.__queue[self.__tail] = item
        else:
            self.__tail = (self.__tail + 1) % self.__capacity
            self.__queue[self.__tail] = item

    def dequeue(self):
        """Remove item from queue and return it."""
        if self.isEmpty():
            raise QueueEmpty

        if self.__head == self.__tail:
            item = self.__queue[self.__head]
            self.__queue[self.__head] = None
            self.__head = self.__tail = -1
            return item

        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        return item

    def display(self) -> list:
        """Returns self"""
        return self.__queue

    def isEmpty(self) -> bool:
        """Checks if Queue is empty or not."""
        if self.__head == -1:
            return True
        return False

    def isFull(self):
        """Checks if Queue is full or not."""
        if (self.__tail + 1) % self.__capacity == self.__head:
            return True
        return False
