# Node Class

from typing import ItemsView
# Node class implementation

class Node:
    """Node implementation for Linked list DS.
    
    Attributes:
        data:
            Data storage in node.
        prev:
            Pointer to the previous Node.
        Next:
            Pointer to the next Node.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.prev: Node = None
        self.next: Node = None
