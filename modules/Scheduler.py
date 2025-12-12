from modules.CircularList import CircularList, Node
from modules.Process import Process
class Scheduler:
    def __init__(self):
        self.process_list = CircularList()
        self.test_process = Process("TestProcess", 10)