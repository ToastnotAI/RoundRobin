from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler:
    currentNode = None
    _timeSlice = 3


    def __init__(self):
        self.processList = CircularList()

    def add_process(self, process):
        self.processList.add(Node(process))
        if self.currentNode is None:
            self.currentNode = self.processList.head

    def step(self):
        if self.currentNode is None:
            return
        self.currentNode.data.processTime -= self._timeSlice
        if self.currentNode.data.processTime <= 0:
            nodeToDelete = self.currentNode
            self.currentNode = self.currentNode.next
            self.processList.delete(nodeToDelete)

            if self.processList.size == 0:
                self.currentNode = None

        else:
            self.currentNode = self.currentNode.next

