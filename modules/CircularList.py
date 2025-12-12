class Node:
    data = None
    next = None
    prev = None

    def __init__(self, data=None):
        self.data = data


class CircularList:
    head = None
    size = 0

    def add(self, node):
        self.size += 1
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
        if node.next is None or node.prev is None:
            raise(ValueError(f"Node {node.data} not in list"))

        self.size -= 1
        # modify surrounding pointers
        node.next.prev = node.prev
        node.prev.next = node.next

        #update head if head is target node
        if node == self.head:
            if self.size == 0:
                self.head = None
            else:
                self.head = node.next
        
        #delete target pointers
        node.next = None
        node.prev = None

        