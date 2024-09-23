from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text

class TestInsertString(TestCase):
    def test_convert_to_text_normal(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977, 36), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_convert_to_text_hello(self):
        self.assertEqual(convert_to_text(18726742329939, 10), "HELLOWORLD")
    def test_convert_to_text_evil(self):
        self.assertEqual(convert_to_text(1097760813042385710430, 15), "EVILSCARYDILLAR")
    def test_convert_to_text_mouse(self):
        self.assertEqual(convert_to_text(806771775309892672025368, 17), "MOUSEINBAKEDBEANS")
    def test_convert_to_text_six(self):
        self.assertEqual(convert_to_text(874638191183853005, 13), "NUMBERSIXTHEJ")