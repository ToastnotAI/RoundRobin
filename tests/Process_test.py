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
        self.assertTrue(hasattr(process, 'data'))
        self.assertIsInstance(process.data, list)
    def test_Process_must_have_name_and_time(self):
        with self.assertRaises(TypeError):
            process = Process()  # Missing arguments

        with self.assertRaises(TypeError):
            process = Process("OnlyName")  # Missing time argument

    def test_strict_types_for_Process(self):
        with self.assertRaises(TypeError):
            process = Process(123, 23)  # Invalid name type

        with self.assertRaises(TypeError):
            process = Process("validName", "NotAnInt")  # Invalid time type
        
        #check valid case does not raise type error
        try:
            process = Process("ValidName", 10)
        except TypeError:   
            self.fail("Process raised TypeError unexpectedly!")

    def test_Process_initialization(self):
        name = "TestProcess"
        time = 10
        process = Process(name, time)
        self.assertEqual(process.data[0], name)
        self.assertEqual(process.data[1], time)
    
    def test_get_process_repr(self):
        name = "TestProcess"
        time = 10
        process = Process(name, time)
        expectedRepr = f"Process(name={name}, time={time})"
        self.assertEqual(repr(process), expectedRepr)
    
    def test_get_process_str(self):
        name = "TestProcess"
        time = 10
        process = Process(name, time)
        processStr = str(process)
        self.assertIn(name, processStr)
        self.assertIn(str(time), processStr)
