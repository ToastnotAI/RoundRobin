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

    def test_Scheduler_has_process_list(self):
        scheduler = Scheduler()
        self.assertTrue(hasattr(scheduler, 'process_list'))
        self.assertIsNotNone(scheduler.process_list)
        self.assertEqual(type(scheduler.process_list).__name__, 'CircularList')

    def test_Scheduler_attributes(self):
        scheduler = Scheduler()
        self.assertTrue(hasattr(scheduler, 'current_process'))
        self.assertEqual(scheduler.current_process, None)
        self.assertTrue(hasattr(scheduler, '_time_slice'))
        self.assertNotEqual(scheduler._time_slice, 0) # _time_slice should have a default non-zero value

    def test_Scheduler_process_list_initially_empty(self):
        scheduler = Scheduler()
        self.assertEqual(scheduler.process_list.size, 0)

    def test_Scheduler_add_test_process(self):
        scheduler = Scheduler()
        testProcess = Process("TestProcess", 10)
        scheduler.add_process(testProcess)
        self.assertEqual(scheduler.process_list.size, 1)
        self.assertEqual(scheduler.process_list.head.data, testProcess)
        self.assertEqual(scheduler.current_process, testProcess)

    # This test was AI generated using inline suggestion based on the function definition
    def test_Scheduler_add_multiple_processes(self):
        scheduler = Scheduler()
        process1 = Process("Process1", 5)
        process2 = Process("Process2", 8)
        process3 = Process("Process3", 12)

        scheduler.add_process(process1)
        scheduler.add_process(process2)
        scheduler.add_process(process3)

        self.assertEqual(scheduler.process_list.size, 3)
        self.assertEqual(scheduler.process_list.head.data, process1)
        self.assertEqual(scheduler.process_list.head.next.data, process2)
        self.assertEqual(scheduler.process_list.head.next.next.data, process3)
        self.assertEqual(scheduler.current_process, process1)
    
    def test_scheduler_stepping_forward_in_time(self):
        scheduler = Scheduler()
        scheduler._time_slice = 3  # Set time slice to 3 for this test
        process1 = Process("Process1", 10)
        process2 = Process("Process2", 10)

        scheduler.add_process(process1)
        scheduler.add_process(process2)

        self.assertEqual(scheduler.current_process, process1)
        scheduler.step()
        self.assertEqual(scheduler.current_process, process2)
        self.assertEqual(process1.remaining_time, 7)
        scheduler.step()
        self.assertEqual(scheduler.current_process, process1)
        self.assertEqual(process2.remaining_time, 7)
        

