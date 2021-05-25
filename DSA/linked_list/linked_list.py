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
        __init__:
            Init Linked List class.
        __len__:
            Fetches linked list length.
        __contains__:
            Return key in self.
        __getitem__:
            x.__getitem__(y) <==> x[y]
        __setitem__:
            Set self[key] to value.
        __delitem__:
            Delete self[key].
        __iter__:
            Iterate over linked list data.
        __next__:
            Fetches next Node.
        push:
            Add new node at head.
        insert:
            Add new data to linked list.
        append:
            Add new node at tail.
        remove:
            Remove first occurrence of value.
        pop:
            Delete last Node and return it.
        clear:
            Remove all items from linked list.
        index:
            Return first index of value.
        get:
            Retrieves data from linked list.
        count:
            Return number of occurrences of value.
        reverse:
            Reverse linked list.
        display:
            Retern list representation of linked list.
    """
    def __init__(self, iteriable = None) -> None:
        """Initiate LinkedList class."""
        self.__head = None
        if iteriable:
            self.__iteriate(iteriable)

    def __len__(self) -> int:
        """Return the length of list.

        Return:
            length: @int
                The length of linked list, 0 if empty.
        """
        length = 0
        current = self.__head
        while current:
            length += 1
            current = current.next
        return length

    def __contains__(self, key) -> bool:
        """Return key in self.

        Args:
            key:
                The key to search for.

        Return:
            @bool: True if key exitst, False otherwise.
        """
        current = self.__head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def __getitem__(self, key: int) -> Any:
        """x.__getitem__(y) <==> x[y]

        Args:
            key:
                Index of linked list.

        Return:
            data:
                The Node data.

        Raise:
            IndexError:
                Raises if list is empty or index out of range.
        """
        key = self.__correct_index(key)

        node = self.__get_node(key)
        return node.data

    def __setitem__(self, key: int, value) -> None:
        """Set self[key] to value.

        Args:
            key:
                Index of linked list.
            value:
                The value to be added.

        Raise:
            IndexError:
                Raises if list is empty or index out of range.
        """
        key = self.__correct_index(key)

        node = self.__get_node(key)
        node.data = value

    def __delitem__(self, key: int) -> None:
        """Return key in self.

        Args:
            key:
                Index of linked list.
        """
        key = self.__correct_index(key)

        if key == 0:
            self.__head = self.__head.next
            return

        pre_node = self.__get_prev_node(key)
        pre_node.next = pre_node.next.next

    def __iter__(self):
        """Iteriate over linked list nodes."""
        self.current = self.__head
        return self

    def __next__(self):
        """Fetches next node.

        Return:
            Node data:
                The data in linked list node.

        Raise:
            StopIteration:
                Stops iteration when reache last Node.
        """
        if self.current:
            data = self.current.data
            self.current = self.current.next
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

    def insert(self, index: int, data) -> None:
        """Insert new data before index.

        Args:
            data:
                The data to be inserted.
            index: @int
                The index at which data should be inserted.

        Raise:
            IndexError:
                Raises when given index not exist.
        """
        index = self.__correct_index(index)

        if index == 0:
            self.push(data)
            return

        new_node = Node(data)
        prev_node = self.__get_prev_node(index)

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
    def remove(self, value) -> None:
        """Delete Node at index.

        Args:
            value: Node data.

        Raise:
            ValueError: Value is not present.
        """
        pass

    def pop(self, index: int = -1) -> Any:
        """Delete last Node and return it.

        Args:
            index: @int | Node index.
        Return:
            data: The last Node data.
        Raise:
            IndexError: Index out of range.
        """
        node = self.__get_node(index)
        del self[index]
        return node.data

    def clear(self) -> None:
        """Remove all items from linked list."""
        self.__head = None

    def index(self, value) -> int:
        """Return first index of value.
        
        Args:
            value:
                Node data.
        Return:
            index: @int
                Index of fist occurrence of value, -1 if not found.
        """
        found = False
        index = -1
        current = self.__head
        while current:
            index += 1
            if current.data == value:
                found = True
                break
            current = current.next

        if found:
            return index
        raise ValueError(f"Value '{value}' not present.")

    def get(self, key, default = None) -> Any:
        """Retrieves data from index.
        
        Args:
            key: Node index.
            default: The default return if index does't exist.
        Return:
            data: The data of node, None if not exist.
        """
        try:
            return self[key]
        except IndexError:
            return default

    def count(self, key) -> int:
        """Return number of occurrences of value.

        Args:
            key: The Node data

        Return:
            @int: Number of occurrences of value.
        """
        occurrence = 0
        current = self.__head
        while current:
            if current.data == key:
                occurrence += 1
            current = current.next
        return occurrence

    def reverse(self) -> None:
        """Reverse linked list."""
        pass

    def display(self) -> list:
        """Retern list representation of linked list."""
        return list(self)

    # Private methods
    def __iteriate(self, iteriable) -> None:
        """Make linked list from iteriable"""
        for data in iteriable:
            self.append(data)

    def __isEmpty(self) -> bool:
        """Checks if linked list is empty.

        Return:
            @bool: True if empty, False otherwise.
        """
        if self.__head:
            return False
        return True

    def __correct_index(self, index) -> int:
        """Checks if index is valid.

        Return:
            index: @int | Corrected index.
        Raise:
            IndexError: Index out of range.
        """
        # Negative index
        if index < 0 and abs(index) <= len(self):
            return len(self) + index

        # Positive index
        if index < len(self):
            return index

        raise IndexError("Index out of range.")

    # Node getting operations
    def __get_node(self, index: int) -> Node:
        """Fetches Node in linked list.

        Args:
            index: @int | The index of desired Node.
        Return:
            Node: The node of index.
        """
        index = self.__correct_index(index)

        node = self.__head
        for i in range(index):
            if node.next:
                node = node.next
        return node

    def __get_prev_node(self, index: int) -> Node:
        """Fetches the previous Node.

        Args:
            index: @int
                The index of Next node.

        Return:
            Node: @object
                Node of the previous Node.
        """
        index = self.__correct_index(index)

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
