from modules.CircularList import Node
class Process(Node):
    """A class to represent a process.
    Attributes:
        self.data: A list containing the process name and process time.
            data[0]: The name of the process.
            data[1]: The time required for the process to complete.
    """
    
    data = [None, None]  # [processName, processTime]
    def __init__(self, name, time):
        """Initializes a Process with the given name and time.
        Args:
            name: The name of the process.
            time: The time required for the process to complete.
        """

        if not isinstance(name, str):
            raise TypeError("processName must be a string")

        if not isinstance(time, int):
            raise TypeError("processTime must be an integer")


        self.data = [name, time]


    def __repr__(self):
        """Returns a string representation of the Process."""
        return f"Process(name={self.data[0]}, time={self.data[1]})"


    def __str__(self):
        """Returns a user-friendly string representation of the Process."""
        return f"Process {self.data[0]} with {self.data[1]} time units remaining"
        