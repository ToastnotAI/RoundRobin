from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler:
    currentNode = None
    _timeSlice = 3


    def __init__(self):
        self.processList = CircularList()

        # overwrite find to search by processName
        def find_by_name(targetName):
            currentNode = self.processList.head
            for _ in range(self.processList.size):
                if currentNode.data.processName == targetName:
                    return currentNode
                currentNode = currentNode.next
            return None
        self.processList.find = find_by_name

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
        
    def kill(self, processName):
        processToKillNode = self.processList.find(processName)
        if processToKillNode is None:
            return False
        processToKill = processToKillNode.data


        if processToKillNode == self.currentNode:
            if self.processList.size == 1:
                self.currentNode = None
            else:
                self.currentNode = self.currentNode.next   

        self.processList.delete(processToKillNode)
        return True

    def get_current(self):
        if self.currentNode is None:
            return None
        return self.currentNode.data

    def __iter__(self):
        for node in self.processList:
            yield node.data

    def __str__(self):
        processes = []
        for process in self:
            processes.append(f"{process.processName}({process.processTime})")
        return "Scheduler Processes: " + " -> ".join(processes)




