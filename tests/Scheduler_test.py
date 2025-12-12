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

    def test_Scheduler_process_list_initially_empty(self):
        scheduler = Scheduler()
        self.assertEqual(scheduler.process_list.size, 0)

    def test_Scheduler_add_test_process(self):
        scheduler = Scheduler()
        testProcess = Process("TestProcess", 10)
        scheduler.add_process(testProcess)
        self.assertEqual(scheduler.process_list.size, 1)
        self.assertEqual(scheduler.process_list.head.data, testProcess)
    
    