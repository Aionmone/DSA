# Implementation of stack data structure

from exceptions.stack import StackFull, StackEmpty

class Stack:
    """Stack DSA"""

    def __init__(self, capacity = 15):
        '''Init stack and its capacity'''
        self.__stack = []
        self.__capacity = capacity

    def __len__(self):
        '''Returns the aquired capacity of stack'''
        return len(self.__stack)

    def __str__(self):
        '''Returns stack'''
        return self.__stack

    def push(self, item) -> None:
        '''Pushs new item to stack'''
        if self.__isFull():
            raise StackFull
        self.__stack.append(item)

    def pop(self):
        '''Retreves last item in stack and delete it'''
        if self.__isEmpty():
            raise StackEmpty
        return self.__stack.pop()

    def display(self):
        '''Shows stack items'''
        return self.__stack

    # Properties
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def isEmpty(self) -> bool:
        return self.__isEmpty()

    @property
    def isFull(self):
        return self.__isFull()

    @property
    def peek(self):
        '''Shows last item in stack'''
        if self.__isEmpty():
            raise StackEmpty
        return self.__stack[-1]

    # Private methods
    def __isEmpty(self):
        '''Checks if stack is empty'''
        if len(self.__stack) < 1:
            return True
        return False

    def __isFull(self):
        '''Checks if stack is full'''
        if len(self.__stack) >= self.__capacity:
            return True
        return False