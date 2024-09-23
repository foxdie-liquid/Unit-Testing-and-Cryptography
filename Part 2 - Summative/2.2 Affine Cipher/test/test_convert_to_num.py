from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num

class TestInsertString(TestCase):
    def test_convert_to_num_normal(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)
    def test_convert_to_num_hello(self):
        self.assertEqual(convert_to_num("HELLOWORLD"), 18726742329939)
    def test_convert_to_num_evil(self):
        self.assertEqual(convert_to_num("EVILSCARYDILLAR"), 1097760813042385710430)
    def test_convert_to_num_mouse(self):
        self.assertEqual(convert_to_num("MOUSEINBAKEDBEANS"), 806771775309892672025368)
    def test_convert_to_num_six(self):
        self.assertEqual(convert_to_num("NUMBERSIXTHEJ"), 874638191183853005)