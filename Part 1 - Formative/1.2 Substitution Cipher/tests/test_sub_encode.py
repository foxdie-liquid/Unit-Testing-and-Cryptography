from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestInsertString(TestCase):
    def test_regular_sub(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")
    def test_different_sub(self):
        self.assertEqual(sub_encode("HELLOWORLD", "ACBEDGFIHKJMLONQPSRUTWVYXZ"), "IDMMNVNSME")
    def test_different2_sub(self):
        self.assertEqual(sub_encode("HELLOWORLD", "ZYXWVUTSRQPONMLKJIHGFEDCBA"), "SVOOLDLIOW")