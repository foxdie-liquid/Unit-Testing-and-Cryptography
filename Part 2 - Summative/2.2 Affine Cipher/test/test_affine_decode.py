from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class TestInsertString(TestCase):
    def test_affine_decode_normal(self):
        self.assertEqual(affine_decode("EVQQZXZIQS", 3, 9), "HELLOWORLD")
    def test_affine_decode_1n5(self):
        self.assertEqual(affine_decode("HELLOWORLD", 1, 5), "ITCCRFRGCO")
    def test_affine_decode_3n7(self):
        self.assertEqual(affine_decode("CZGGJRJMGY", 3, 7), "LQNNIMIDNJ")
    def test_affine_decode_7n6(self):
        self.assertEqual(affine_decode("HGRRSMSTRX", 7, 6), "JDRRXNXDRB")
    def test_affine_decode_5n6(self):
        self.assertEqual(affine_decode("PAJJYMYNJV", 5, 6), "HVXXJPJVXR")