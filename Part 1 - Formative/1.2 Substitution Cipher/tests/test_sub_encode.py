from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestInsertString(TestCase):
    def test_insert_string_two_words_lowercase(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")