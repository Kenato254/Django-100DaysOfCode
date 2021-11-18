import unittest

class TestStringMethod(unittest.TestCase):

    def setUp(self):
        '''Repetitious set-up run by different test methods'''
        self.variable = 'foo'.upper()

    def test_upper(self):
        self.assertEqual(self.variable, 'FOO')
        
    def test_isupper(self):
        self.assertTrue(self.variable.isupper(), True)

    def tearDown(self):
        """Tides up after test method has been run. Runs whether setUp() succeeds or not"""
        self.variable

