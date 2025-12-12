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
