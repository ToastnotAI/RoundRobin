class Process:
    processName = None
    processTime = None

    def __init__(self, name, time):
        if not isinstance(name, str):
            raise TypeError("processName must be a string")
        if not isinstance(time, int):
            raise TypeError("processTime must be an integer")
        
        self.processName = name
        self.processTime = time
        