from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestInsertString(TestCase):
    def test_shift_normal(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 5), "HELLOWORLD")
    def test_shift_7(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 7), "FCJJMUMPJB")
    def test_shift_21(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 21), "ROVVYGYBVN")
    def test_shift_255minus10(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 255-10), "BYFFIQILFX")
    def test_shift_1000minus25(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 1000-25), "ZWDDGOGJDV")