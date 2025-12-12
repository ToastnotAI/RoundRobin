from modules.CircularList import Node, CircularList
import unittest

class TestCircularListNode(unittest.TestCase):
    def test_node_exists(self):
        node = Node()
        self.assertIsNotNone(node)

    def test_node_type(self):
        node = Node()
        self.assertIsInstance(node, Node)

    def test_node_initializes_with_data(self):
        data = "test_data"
        node = Node(data)
        self.assertEqual(node.data, data)
    
    def test_node_has_next_and_prev_attributes(self):
        node = Node()
        self.assertTrue(hasattr(node, 'next'))
        self.assertTrue(hasattr(node, 'prev'))

class TestCircularList(unittest.TestCase):
    def test_CircularList_class_exists(self):
        cList = CircularList()
        self.assertIsNotNone(cList)
    
    def test_CircularList_type(self):
        cList = CircularList()
        self.assertIsInstance(cList, CircularList)

    def test_CircularList_has_attributes(self):
        cList = CircularList()
        self.assertTrue(hasattr(cList, 'head'))
        self.assertTrue(hasattr(cList, 'size'))
    
    def test_CircularList_initial_size(self):
        cList = CircularList()
        self.assertEqual(cList.size, 0)
    
    def test_CircularList_head_initially_none(self):
        cList = CircularList()
        self.assertIsNone(cList.head)

    def test_assign_first_node_as_head(self):
        cList = CircularList()
        node = Node("first")
        cList.add(node)
        self.assertEqual(cList.head, node)
        self.assertEqual(cList.size, 1)
        self.assertEqual(cList.head.next, node)
        self.assertEqual(cList.head.prev, node)
    
    def test_add_multiple_nodes(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        third_node = Node("third")

        cList.add(first_node)
        cList.add(second_node)
        cList.add(third_node)

        self.assertEqual(cList.size, 3)

        self.assertEqual(cList.head, first_node)
        self.assertEqual(cList.head.next, second_node)
        self.assertEqual(cList.head.prev, third_node)

        self.assertEqual(second_node.next, third_node)
        self.assertEqual(second_node.prev, first_node)

        self.assertEqual(third_node.next, first_node)
        self.assertEqual(third_node.prev, second_node)

    def test_delete_node(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        third_node = Node("third")

        cList.add(first_node)
        cList.add(second_node)
        cList.add(third_node)

        # Deleting second node
        cList.delete(second_node)
        self.assertEqual(cList.size, 2)

        self.assertEqual(cList.head, first_node)
        self.assertEqual(cList.head.next, third_node)
        self.assertEqual(cList.head.prev, third_node)

        self.assertEqual(third_node.next, first_node)
        self.assertEqual(third_node.prev, first_node)

        self.assertIsNone(second_node.next)
        self.assertIsNone(second_node.prev)

    def test_delete_head_node(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        third_node = Node("third")

        cList.add(first_node)
        cList.add(second_node)
        cList.add(third_node)

        cList.delete(first_node)
        self.assertEqual(cList.size, 2)
        self.assertEqual(cList.head, second_node)
        self.assertEqual(cList.head.next, third_node)
        self.assertEqual(cList.head.prev, third_node)

    def test_delete_tail(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        third_node = Node("third")

        cList.add(first_node)
        cList.add(second_node)
        cList.add(third_node)

        cList.delete(third_node)
        self.assertEqual(cList.size, 2)
        self.assertEqual(cList.head, first_node)
        self.assertEqual(cList.head.next, second_node)
        self.assertEqual(cList.head.prev, second_node)

    def test_delete_last_node_in_list(self):
        cList = CircularList()
        only_node = Node("only")
        cList.add(only_node)

        cList.delete(only_node)
        self.assertEqual(cList.size, 0)
        self.assertIsNone(cList.head)

    def test_error_when_trying_to_delete_when_node_not_in_list(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        absent_node = Node("absent")
        cList.add(first_node)
        cList.add(second_node)

        with self.assertRaises(ValueError):
            cList.delete(absent_node)

    def test_error_when_deleting_node_from_empty_list(self):
        cList = CircularList()
        absent_node = Node("absent")

        with self.assertRaises(ValueError):
            cList.delete(absent_node)

    def test_find_node_by_data(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")
        third_node = Node("third")

        cList.add(first_node)
        cList.add(second_node)
        cList.add(third_node)

        found_node = cList.find("second")
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node, second_node)

    def test_find_node_not_in_list(self):
        cList = CircularList()
        first_node = Node("first")
        second_node = Node("second")

        cList.add(first_node)
        cList.add(second_node)

        found_node = cList.find("absent")
        self.assertIsNone(found_node)

    def test_iterate_through_list(self):
        cList = CircularList()
        nodesData = ["first", "second", "third", "fourth"]
        nodes = [Node(data) for data in nodesData]
        for node in nodes:
            cList.add(node)
        
        for yieldedNode in cList:
            expected = nodes.pop(0)
            self.assertEqual(yieldedNode, expected)
        


    

        


    

    

        