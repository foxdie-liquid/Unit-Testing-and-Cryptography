from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestInsertString(TestCase):
    def test_shift_normal(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 5), "MJQQTBTWQI")