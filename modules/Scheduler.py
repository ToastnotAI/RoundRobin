from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler:
    """A class to represent a round-robin scheduler.
    Attributes:
        processList: A circular list of processes managed by the scheduler.
        currentNode: A pointer to the current process node being executed.
        _timeSlice: The time slice allocated to each process per step.
    """

    processList = None # Circular list of processes
    currentNode = None # Pointer to current process node, defaults to none if no processes
    _timeSlice = 3 # time units per process per step
    

    def __init__(self):
        """Initializes a Scheduler with an empty process list and overwrites the find of CircularList."""

        self.processList = CircularList()
        def find_by_name(targetName):
            """Finds a process node in the circular list by its process name.
            This overwrites the default find method of CircularList to search by processName.
            Args:
                targetName: The name of the process to find.
            Returns:
                The node with the given process name, or None if not found.
            """

            for node in self.processList:
                if node.data.processName == targetName:
                    return node
            return None
        self.processList.find = find_by_name
    

    def add_process(self, process):
        """Adds a process to the scheduler.
        Args:
            process: The process to add to the scheduler.
        """

        self.processList.add(Node(process))
        if self.currentNode is None:
            self.currentNode = self.processList.head


    def step(self):
        """Advances the scheduler by one time slice."""
        if self.currentNode is None:
            return

        # Deduct time slice from current process
        self.currentNode.data.processTime -= self._timeSlice

        # If process is complete, remove it from the list
        if self.currentNode.data.processTime <= 0:
            nodeToDelete = self.currentNode
            self.currentNode = self.currentNode.next
            self.processList.delete(nodeToDelete)

            # If all processes are complete, set currentNode to None
            if self.processList.size == 0:
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
        processToKillNode = self.processList.find(processName)
        if processToKillNode is None:
            return False

        processToKill = processToKillNode.data # Process object is the data of the circular list node

        # If the process to kill is the current process, move currentNode pointer
        if processToKillNode == self.currentNode:
            if self.processList.size == 1:
                self.currentNode = None # No more processes left

            else:
                self.currentNode = self.currentNode.next # Move to next process   


        self.processList.delete(processToKillNode)
        return True


    def get_current(self):
        """Gets the current process being executed.
        Returns:
            The current process, or None if there are no processes.
        """
        
        # Cannot just return currentNode as it is a Node object, need to return its data (Process object)
        if self.currentNode is None: 
            return None

        return self.currentNode.data

    
    def kill_current(self):
        """Kills the current process being executed.
        Returns:
            True if the current process was killed, False otherwise.
        """

        return self.kill(self.currentNode.data.processName)


    def __iter__(self):
        """Iterates over the processes in the scheduler."""

        for node in self.processList:
            yield node.data


    def __str__(self):
        """Returns a user-friendly string representation of the Scheduler."""
        processes = []
        for process in self:
            processes.append(f"{process.processName}({process.processTime})")
        return "Scheduler Processes: " + " -> ".join(processes)




