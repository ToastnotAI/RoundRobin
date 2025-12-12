from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler:
    current_process = None
    _time_slice = 3


    def __init__(self):
        self.process_list = CircularList()

    def add_process(self, process):
        self.process_list.add(Node(process))
        self.current_process = self.process_list.head.data