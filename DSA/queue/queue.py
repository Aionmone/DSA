# Queue implementation in Python

from exceptions.queue import QueueEmpty, QueueFull

class Queue:

    def __init__(self, capacity= None):
        '''Initiate Queue'''
        self.__queue = []
        self.__capacity =  capacity

    def __len__(self):
        '''Return len(self)'''
        return len(self.__queue)

    def __str__(self) -> str:
        '''Prints currunt queue'''
        return str(self.__queue)

    # Properties
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def peek(self):
        '''Shows last item in stack'''
        if self.isEmpty():
            raise QueueEmpty
        return self.__queue[0]

    def enqueue(self, item) -> None:
        '''Add item to queue'''
        if self.isFull():
            raise QueueFull
        self.__queue.append(item)

    def dequeue(self) -> None:
        '''Remove item from queue'''
        if self.isEmpty():
            raise QueueEmpty
        return self.__queue.pop(0)

    def display(self):
        '''Returns self'''
        return self.__queue()

    def isEmpty(self) -> bool:
        '''Checks either Queue is empty or not.'''
        if len(self.__queue) < 1:
            return True
        return False

    def isFull(self):
        '''Checks either Queue is full or not.'''
        if self.__capacity and len(self.__queue) >= self.__capacity:
            return True
        return False
