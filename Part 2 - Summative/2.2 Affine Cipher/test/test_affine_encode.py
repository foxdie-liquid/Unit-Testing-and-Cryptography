from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestInsertString(TestCase):
    def test_affine_encode_normal(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 9), "EVQQZXZIQS")
    def test_affine_encode_5n6(self):
        self.assertEqual(affine_encode("PAJJYMYNJV", 5, 6), "DGZZWOWTZH")
    def test_affine_encode_9n5(self):
        self.assertEqual(affine_encode("DGZZWOWTZH", 9, 5), "GHWWVBVUWQ")
    def test_affine_encode_7n3(self):
        self.assertEqual(affine_encode("GHWWVBVUWQ", 7, 3), "TABBUKUNBL")
    def test_affine_encode_1n4(self):
        self.assertEqual(affine_encode("TABBUKUNBL", 1, 4), "XEFFYOYRFP")