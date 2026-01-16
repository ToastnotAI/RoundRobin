class Node:
    """A node in a circular doubly linked list.
    Attributes:
        data: The data stored in the node.
        next: A pointer to the next node in the list.
        prev: A pointer to the previous node in the list.
    """

    data = None
    next = None
    prev = None


    def __init__(self, data=None):
        """Initializes a Node with the given data."""
        self.data = data


class CircularList:
    """A circular doubly linked list.
    Attributes:
        head: A pointer to the head node in the list.
        size: The number of nodes in the list.
    """

    # Head pointer to act as entry point to list
    head = None
    size = 0

    def add(self, node):
        """Adds a node to the circular list.
        Args:
            node: The node to add to the list.
        """

        self.size += 1
        # Set head if list is empty, otherwise at end of cycle
        if self.head is None:
            self.head = node
            node.next = node
            node.prev = node

        else:
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node


    def delete(self, node):
        """Deletes a node from the circular list.
        Args:
            node: The node to delete from the list.
        """

        # Check if node is in the list
        if node.next is None or node.prev is None:
            raise(ValueError(f"Node {node.data} not in list"))

        self.size -= 1
        # Modify surrounding pointers
        node.next.prev = node.prev
        node.prev.next = node.next

        # Update head if head is target node
        if node == self.head:
            if self.size == 0:
                self.head = None
            else:
                self.head = node.next
        
        # Delete target pointers
        node.next = None
        node.prev = None


    def find(self, targetNodeData):
        """Finds a node in the circular list by its data.
        Args:
            targetNodeData: The data of the node to find.
        Returns:
            The node with the given data, or None if not found.
        """

        for node in self:
            if node.data == targetNodeData:
                return node

        return None


    def __iter__(self):
        """Iterates over the nodes in the circular list.
        Yields:
            The next node in the list.
        """
        
        currentNode = self.head
        for _ in range(self.size):
            yield currentNode
            currentNode = currentNode.next


        