from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestInsertString(TestCase):
    def test_shift_normal(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 5), "MJQQTBTWQI")
    def test_shift_7(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 7), "OLSSVDVYSK")
    def test_shift_21(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 21), "CZGGJRJMGY")
    def test_shift_255(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 255), "CZGGJRJMGY")
    def test_shift_1000(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 1000), "TQXXAIADXP")