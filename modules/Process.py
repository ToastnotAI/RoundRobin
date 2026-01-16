class Process:
    """A class to represent a process.
    Attributes:
        processName: The name of the process.
        processTime: The time required for the process to complete.
    """

    processName = None
    processTime = None


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

        self.processName = name
        self.processTime = time


    def __repr__(self):
        """Returns a string representation of the Process."""
        return f"Process(name={self.processName}, time={self.processTime})"
        

    def __str__(self):
        """Returns a user-friendly string representation of the Process."""
        return f"Process {self.processName} with {self.processTime} time units remaining"
        