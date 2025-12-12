#from CircularList import CircularList
import unittest

class TestCircularListNode(unittest.TestCase):
    def test_node_exists(self):
        node = Node()
        self.assertIsNotNone(node)