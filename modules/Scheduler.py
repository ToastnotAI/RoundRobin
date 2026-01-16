from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler(CircularList):
    """A class to represent a round-robin scheduler.
    Attributes:
        processList: A circular list of processes managed by the scheduler.
        currentNode: A pointer to the current process node being executed.
        _timeSlice: The time slice allocated to each process per step.
    """


    currentNode = None # Pointer to current process node, defaults to none if no processes
    _timeSlice = 3 # time units per process per step


    def find(self, processName):
        """Finds a process node by its name.
        Args:
            processName: The name of the process to find.
        Returns:
            The node with the given process name, or None if not found.
        """
        for node in self:
            if node.data[0] == processName:
                return node
        return None
    

    def add_process(self, process):
        """Adds a process to the scheduler.
        Args:
            process: The process to add to the scheduler.
        """

        self.add(process)
        if self.currentNode is None:
            self.currentNode = self.head


    def step(self):
        """Advances the scheduler by one time slice."""
        if self.currentNode is None:
            return

        # Deduct time slice from current process
        self.currentNode.data[1] -= self._timeSlice

        # If process is complete, remove it from the list
        if self.currentNode.data[1] <= 0:
            nodeToDelete = self.currentNode
            self.currentNode = self.currentNode.next
            self.delete(nodeToDelete)

            # If all processes are complete, set currentNode to None
            if self.size == 0:
                self.currentNode = None

        # Move to the next process
        else:
            self.currentNode = self.currentNode.next

        
    def kill(self, processName):
        """Kills a process by its name.
        Args:
            processName: The name of the process to kill.
        Returns:
            True if the process was found and killed, False otherwise.
        """

        # Find the node corresponding to the process name
        processToKillNode = self.find(processName)
        if processToKillNode is None:
            return False

        processToKill = processToKillNode # Process object is the data of the circular list node

        # If the process to kill is the current process, move currentNode pointer
        if processToKillNode == self.currentNode:
            if self.size == 1:
                self.currentNode = None # No more processes left

            else:
                self.currentNode = self.currentNode.next # Move to next process   


        self.delete(processToKillNode)
        return True


    def get_current(self):
        """Gets the current process being executed."""
        return self.currentNode

    
    def kill_current(self):
        """Kills the current process being executed.
        Returns:
            True if the current process was killed, False otherwise.
        """

        return self.kill(self.currentNode.data[0])


    def __str__(self):
        """Returns a user-friendly string representation of the Scheduler."""
        processes = []
        for process in self:
            processes.append(f"{process.data[0]}({process.data[1]})")
        return "Scheduler Processes: " + " -> ".join(processes)




