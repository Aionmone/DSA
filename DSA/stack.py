"""Implementation of stack data structure"""

from typing import Any
from exceptions.stack import StackFull, StackEmpty

class Stack:
    """Stack data structure.
    
    Methods:
        Push:
            Add new data to stack.
        Pop:
            Return last item in stack and remove it.
        Display:
            Shows the current stack data.
        isEmpty:
            Checks if stack is empty or not.
        isFull:
            Checks if stack is full or not.

    Properties:
        capacity:
            Get/Set the stack capacity.
        peek:
            Shows the last item in stack.
    """

    def __init__(self, capacity = 15):
        """Init stack and its capacity."""
        self.__stack = []
        self.__capacity = capacity

    def __len__(self) -> int:
        """Returns the aquired capacity of stack.
        
        Return:
            @int: The length of stack.
        """
        return len(self.__stack)

    def __str__(self) -> str:
        """Returns stack."""
        return str(self.__stack)

    # Properties
    @property
    def capacity(self) -> int:
        """Stack capacity getter.
        
        Return:
            Capacity: The current stack capacity.
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity) -> None:
        """Stack capacity setter."""
        self.__capacity = capacity

    @property
    def peek(self) -> Any:
        """Shows last item in stack.

        Return:
            Last item in stack, None if empty.
        """
        if self.isEmpty():
            return None
        return self.__stack[-1]

    def push(self, data) -> None:
        """Adds new data to stack.
        
        Raise:
            StackFull:
                Indicates stack full capacity occupation.
        """
        if self.isFull():
            raise StackFull
        self.__stack.append(data)

    def pop(self) -> Any:
        """Retreves last item in stack and delete it.
        
        Return:
            @any: last item in stack.

        Raise:
            StackEmpty:
                Indicates stack empty.
        """
        if self.isEmpty():
            raise StackEmpty
        return self.__stack.pop()

    def display(self) -> list:
        """Shows stack items.
        
        Return:
            Stack:
                The items in stack.
        """
        return self.__stack

    def isEmpty(self) -> bool:
        """Checks if stack is empty.
        
        Return:
            @bool: True if empty, False otherwise.
        """
        if self.__stack:
            return False
        return True

    def isFull(self) -> bool:
        """Checks if stack is full.
        
        Return:
            @bool: True if full, False otherwise.
        """
        if len(self) >= self.__capacity:
            return True
        return False
        