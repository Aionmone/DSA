"""Singly linked list implementation

Implement linked list data structure in python.

Usage:
    from DSA import LinkedList

    linked_list = LinkedList()
    linked_list.insert('data')

    linked_list.show()
"""

from typing import Any
from DSA.linked_list.node import Node

class LinkedList:
    """Singly linked list implementation.

    Methods:
        __len__:
            Fetches linked list length.
        __iter__:
            Iterate over linked list data.
        push:
            Add new node at head.
        append:
            Add new node at tail.
        insert_after:
            Add new data to linked list.
        display:
            Retern list representation of linked list.
        get:
            Retrieves data from linked list.
    """
    def __init__(self) -> None:
        """Initiate LinkedList class."""
        self.__head = None

    def __len__(self) -> int:
        """Return the length of list.

        Return:
            length: @int
                The length of linked list, 0 if empty.
        """
        if self.__isEmpty():
            return 0

        length = 1
        node = self.__head
        while node.next != None:
            length += 1
            node = node.next
        return length

    def __iter__(self):
        """Iteriate over linked list nodes."""
        self.temp = self.__head
        return self

    def __next__(self):
        """Fetches next node.

        Return:
            Node data: @any
                The data in linked list node.

        Raise:
            StopIteration:
                Stops iteration when reache last Node.
        """
        if self.temp:
            data = self.temp.data
            self.temp = self.temp.next
            return data
        else:
            raise StopIteration

    # Insertion operations
    def push(self, data) -> None:
        """Add data at the head of linked list.

        Args:
            data:
                New data to add to linked list.
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def insert_after(self, data: Any, index: int) -> None:
        """Insert new data after index.

        Args:
            data:
                The data to be inserted.
            index: @int
                The index at which data should be inserted.

        Raise:
            IndexError:
                Raises when given index not exist.
        """
        if self.__isEmpty():
            self.__head = Node(data)
            return

        if index >= len(self):
            raise IndexError

        new_node = Node(data)
        prev_node = self.__get_node(index)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data) -> None:
        """Add data at the tail of linked list.

        Args:
            data:
                New data to add to linked list.
        """
        if self.__isEmpty():
            self.__head = Node(data)
            return

        last_node = self.__get_last_node()
        last_node.next = Node(data)

    # Deletion operation
    def delete(self, index: int) -> None:
        """Delete Node at index.

        Args:
            index: @int
                The required Node index.

        Raise:
            IndexError:
                Raises when given index not exist.
        """
        if self.__isEmpty() or index >= len(self):
            raise IndexError

        if index == 0:
            self.__head = None
            return

        pre_node = self.__get_prev_node(index)
        pre_node.next = pre_node.next.next

    def pop(self) -> Any:
        """Delete last Node and return it.

        Return:
            data:
                The last Node data.
        """
        last_node = self.__get_last_node()
        pre_node = self.__get_prev_node((len(self) - 1))
        pre_node.next = None
        return last_node.data

    def get(self, index, default = None) -> Any:
        """Retrieves data from index.
        
        Args:
            index:
                The index of node.
            default:
                The default return if index does't exist.
            
        Return:
            data: The data of node, None if not exist.
        """
        if index >= len(self):
            return default

        node = self.__head
        for i in range(index):
            if node.next != None:
                node = node.next

        return node.data

    def display(self) -> str:
        """Retern tuple representation of linked list."""
        return tuple(self)

    def __isEmpty(self) -> bool:
        """Checks if linked list is empty.

        Return:
            @bool: True if empty, False otherwise.
        """
        if self.__head:
            return False
        return True

    # Node getting operations
    def __get_node(self, index) -> Node:
        """Fetches Node in linked list.
        
        Args:
            index:
                The index of desired Node.

        Return:
            Node:
                The node of index.
        """
        node = self.__head
        for i in range(index):
            if node.next:
                node = node.next
        return node

    def __get_prev_node(self, index) -> Node:
        """Fetches the previous Node.

        Args:
            index: @int
                The index of Next node.

        Return:
            Node: @object
                Node of the previous Node.
        """
        prev_node = self.__head
        for node in range(index):
            if node == (index - 1):
                break
            if prev_node.next:
                prev_node = prev_node.next
        return prev_node

    def __get_last_node(self) -> Node:
        """Fetches the last Node in linked list.

        Return:
            Node: @object
                Last Node in linked list.
        """
        last_node = self.__head
        while last_node.next:
            last_node = last_node.next
        return last_node
