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
        
        self.assertNotEqual(scheduler.processList.head.data, process2)
        self.assertEqual(scheduler.processList.size, 0)



