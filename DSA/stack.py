# Implementation of stack data structure

from exceptions.stack import StackFull, StackEmpty

class Stack:
    """Stack DSA"""

    def __init__(self, capacity = 15):
        '''Init stack and its capacity'''
        self.__stack = []
        self.__capacity = capacity

    def __len__(self) -> int:
        '''Returns the aquired capacity of stack'''
        return len(self.__stack)

    def __str__(self) -> str:
        '''Returns stack'''
        return str(self.__stack)

    # Properties
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def peek(self):
        '''Shows last item in stack'''
        if self.isEmpty():
            raise StackEmpty
        return self.__stack[-1]

    def push(self, item) -> None:
        '''Pushs new item to stack'''
        if self.isFull():
            raise StackFull
        self.__stack.append(item)

    def pop(self):
        '''Retreves last item in stack and delete it'''
        if self.isEmpty():
            raise StackEmpty
        return self.__stack.pop()

    def display(self):
        '''Shows stack items'''
        return self.__stack

    def isEmpty(self) -> bool:
        '''Checks if stack is empty'''
        if len(self.__stack) < 1:
            return True
        return False

    def isFull(self):
        '''Checks if stack is full'''
        if len(self.__stack) >= self.__capacity:
            return True
        return False
        