import unittest
from modules.Process import Process

class TestProcess(unittest.TestCase):
    def test_Process_class_exists(self):
        process = Process("TestProcess", 10)
        self.assertIsNotNone(process)
    
    def test_Process_type(self):
        process = Process("TestProcess", 10)
        self.assertIsInstance(process, Process)

    def test_Process_attributes(self):
        process = Process("TestProcess", 10)
        self.assertTrue(hasattr(process, "processTime"))
        self.assertTrue(hasattr(process, "processName"))
    
    def test_Process_must_have_name_and_time(self):
        with self.assertRaises(TypeError):
            process = Process()  # Missing arguments

        with self.assertRaises(TypeError):
            process = Process("OnlyName")  # Missing time argument

    def test_strict_types_for_Process(self):
        with self.assertRaises(TypeError):
            process = Process(123, "NotAnInt")  # Invalid types
        
        #check valid case does not raise type error
        try:
            process = Process("ValidName", 10)
        except TypeError:   
            self.fail("Process raised TypeError unexpectedly!")

    def test_Process_initialization(self):
        name = "TestProcess"
        time = 10
        process = Process(name, time)
        self.assertEqual(process.processName, name)
        self.assertEqual(process.processTime, time)
    
