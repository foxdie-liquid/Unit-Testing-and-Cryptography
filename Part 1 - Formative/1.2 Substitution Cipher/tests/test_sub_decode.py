from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestReverseString(TestCase):
    def test_regular_sub(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")
    def test_different_sub(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "ACBEDGFIHKJMLONQPSRUTWVYXZ"), "LYUUIAINUT")
    def test_different_sub(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "ZYXWVUTSRQPONMLKJIHGFEDCBA"), "NCGGSZSLGF")
