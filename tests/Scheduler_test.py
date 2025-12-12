import unittest
from modules.Scheduler import Scheduler
from modules.Process import Process

class TestScheduler(unittest.TestCase):
    def test_Scheduler_class_exists(self):
        scheduler = Scheduler()
        self.assertIsNotNone(scheduler)

    def test_Scheduler_type(self):
        scheduler = Scheduler()
        self.assertIsInstance(scheduler, Scheduler)

    def test_Scheduler_has_processList(self):
        scheduler = Scheduler()
        self.assertTrue(hasattr(scheduler, 'processList'))
        self.assertIsNotNone(scheduler.processList)
        self.assertEqual(type(scheduler.processList).__name__, 'CircularList')
    def test_Scheduler_attributes(self):
        scheduler = Scheduler()
        self.assertTrue(hasattr(scheduler, 'currentNode'))
        self.assertEqual(scheduler.currentNode, None)
        self.assertTrue(hasattr(scheduler, '_timeSlice'))
        self.assertNotEqual(scheduler._timeSlice, 0) # _timeSlice should have a default non-zero value

    def test_Scheduler_process_list_initially_empty(self):
        scheduler = Scheduler()
        self.assertEqual(scheduler.processList.size, 0)

    def test_Scheduler_add_test_process(self):
        scheduler = Scheduler()
        testProcess = Process("TestProcess", 10)
        scheduler.add_process(testProcess)
        self.assertEqual(scheduler.processList.size, 1)
        self.assertEqual(scheduler.processList.head.data, testProcess)
        self.assertEqual(scheduler.currentNode.data, testProcess)

    # This test was AI generated using inline suggestion based on the function definition
    def test_Scheduler_add_multiple_processes(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 5)
        process2 = Process("Process2", 8)
        process3 = Process("Process3", 12)

        scheduler.add_process(process1)
        scheduler.add_process(process2)
        scheduler.add_process(process3)

        self.assertEqual(scheduler.processList.size, 3)
        self.assertEqual(scheduler.processList.head.data, process1)
        self.assertEqual(scheduler.processList.head.next.data, process2)
        self.assertEqual(scheduler.processList.head.next.next.data, process3)
        self.assertEqual(scheduler.currentNode.data, process1)
    
    def test_scheduler_stepping_forward_in_time(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3  # Set time slice to 3 for this test
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 10)

        scheduler.add_process(process1)
        scheduler.add_process(process2)

        self.assertEqual(scheduler.currentNode.data, process1)
        scheduler.step()
        self.assertEqual(scheduler.processList.head.data.processTime, 7)
        self.assertEqual(scheduler.currentNode.data, process2)
        scheduler.step()
        self.assertEqual(scheduler.currentNode.data, process1)
        self.assertEqual(scheduler.processList.head.next.data.processTime, 7)

    def test_Scheduler_step_completing_process(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 3)
        process2 = Process("Process2", 5)
        scheduler.add_process(process1)
        scheduler.add_process(process2)

        self.assertEqual(scheduler.currentNode.data, process1)
        scheduler.step()

        self.assertNotEqual(scheduler.processList.head.data, process1)
        self.assertNotEqual(scheduler.processList.size, 2)
        self.assertEqual(scheduler.currentNode.data, process2)
        self.assertEqual(scheduler.processList.head.data.processTime, 5)
        scheduler.step()

        self.assertEqual(scheduler.processList.head.data.processTime, 2)
        self.assertEqual(scheduler.currentNode.data, process2)
        scheduler.step()

        self.assertIsNone(scheduler.processList.head)
        self.assertEqual(scheduler.processList.size, 0)
        self.assertIsNone(scheduler.currentNode)

    def test_Scheduler_step_on_empty_list(self):
        scheduler = Scheduler()
        self.assertIsNone(scheduler.currentNode)
        try:
            scheduler.step()  # Should not raise an error

        except Exception as e:
            self.fail(f"Scheduler.step() raised an exception on empty list: {e}")

    def test_Scheduler_step_with_single_process_to_completion(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 5)
        scheduler.add_process(process1)
        self.assertEqual(scheduler.currentNode.data, process1)
        scheduler.step()
        self.assertEqual(scheduler.processList.head.data.processTime, 2)
        self.assertEqual(scheduler.currentNode.data, process1)
        scheduler.step()
        self.assertIsNone(scheduler.processList.head)
        self.assertEqual(scheduler.processList.size, 0)
        self.assertIsNone(scheduler.currentNode)
        self.assertLessEqual(process1.processTime, 0)

    def test_find_process(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 15)
        process3 = Process("Process3", 20)

        scheduler.add_process(process1)
        scheduler.add_process(process2)
        scheduler.add_process(process3)

        found_node = scheduler.processList.find("Process2")
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, process2)

        not_found_node = scheduler.processList.find("NonExistentProcess")
        self.assertIsNone(not_found_node)

    def test_kill_process_in_list(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 10)
        process3 = Process("Process3", 10)

        scheduler.add_process(process1)
        scheduler.add_process(process2)
        scheduler.add_process(process3)

        self.assertEqual(scheduler.processList.size, 3)

        killSuccess = scheduler.kill("Process2")
        self.assertTrue(killSuccess)
        self.assertEqual(scheduler.processList.size, 2)
        self.assertEqual(scheduler.processList.head.data, process1)
        self.assertEqual(scheduler.processList.head.next.data, process3)
        self.assertEqual(scheduler.currentNode.data, process1)
        scheduler.step()
        self.assertEqual(scheduler.currentNode.data, process3)
        self.assertEqual(process2.processTime, 10)  # Ensure process2 was not modified

    def test_kill_current_process(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 10)

        scheduler.add_process(process1)
        scheduler.add_process(process2)

        self.assertEqual(scheduler.currentNode.data, process1)

        killSuccess = scheduler.kill("Process1")
        self.assertTrue(killSuccess)
        self.assertEqual(scheduler.processList.size, 1)
        self.assertEqual(scheduler.processList.head.data, process2)
        self.assertEqual(scheduler.currentNode.data, process2)
        scheduler.step()
        self.assertEqual(scheduler.currentNode.data, process2)
        self.assertEqual(process1.processTime, 10)  # Ensure process1 was not modified

    def test_kill_last_process(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 10)

        scheduler.add_process(process1)

        self.assertEqual(scheduler.currentNode.data, process1)

        killSuccess = scheduler.kill("Process1")
        self.assertTrue(killSuccess)
        self.assertEqual(scheduler.processList.size, 0)
        self.assertIsNone(scheduler.processList.head)
        self.assertIsNone(scheduler.currentNode)
        self.assertEqual(process1.processTime, 10)  # Ensure process1 was not modified

    def test_kill_non_existent_process(self):
        scheduler = Scheduler()
        scheduler._timeSlice = 3
        process1 = Process("Process1", 10)
        scheduler.add_process(process1)

        self.assertEqual(scheduler.processList.size, 1)

        try:
            killSuccess = scheduler.kill("NonExistentProcess")  # Should not raise an error
            self.assertFalse(killSuccess)
        except Exception as e:
            self.fail(f"Scheduler.kill() raised an exception for non-existent process: {e}")

        self.assertEqual(scheduler.processList.size, 1)
        self.assertEqual(scheduler.processList.head.data, process1)
        self.assertEqual(scheduler.currentNode.data, process1)
    
    def test_kill_process_empty_list(self):
        scheduler = Scheduler()
        self.assertIsNone(scheduler.currentNode)

        try:
            killSuccess = scheduler.kill("AnyProcess")  # Should not raise an error
            self.assertFalse(killSuccess)
        except Exception as e:
            self.fail(f"Scheduler.kill() raised an exception on empty list: {e}")

        self.assertIsNone(scheduler.currentNode)
        self.assertEqual(scheduler.processList.size, 0)

    def test_retrieve_current_process(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 10)
        scheduler.add_process(process1)
        self.assertEqual(scheduler.get_current(), process1)
        
    def test_iterate_through_processes(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 20)
        process3 = Process("Process3", 30)

        scheduler.add_process(process1)
        scheduler.add_process(process2)
        scheduler.add_process(process3)

        processesInOrder = [process1, process2, process3]
        for yieldedProcess in scheduler:
            expectedProcess = processesInOrder.pop(0)
            self.assertEqual(yieldedProcess, expectedProcess)

    def test_str_output_of_scheduler(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 20)

        scheduler.add_process(process1)
        scheduler.add_process(process2)

        schedulerStr = str(scheduler)
        self.assertIn("Process1", schedulerStr)
        self.assertIn("Process2", schedulerStr)
        self.assertIn("10", schedulerStr)
        self.assertIn("20", schedulerStr)

