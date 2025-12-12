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
        self.currentNode.data.processTime -= self._timeSlice
        self.currentNode = self.currentNode.next