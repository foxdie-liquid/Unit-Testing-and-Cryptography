from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigenereCipher(TestCase):

    def test_vig_decode_normal(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXHFNXVK_XPSRQHFZ", "TEST"), ("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"))
    def test_vig_decode_burger(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXHFNXVK_XPSRQHFZ", "BURGER"), ("KSFCIWTJDPBYEQPJYHCOGBBXWBUUTZRY_BBI"))
    def test_vig_decode_meat(self):
        self.assertEqual(vig_decode("KSFCIWTJDPBYEQPJYHCOGBBXWBUUTZRY_BBI", "MEAT"), ("ZOFKXSTRSLBFTMPRMDCWVYBEKYUBHVRFOYBQ"))
    def test_vig_decode_buzzbuzz(self):
        self.assertEqual(vig_decode("ZOFKXSTRSLBFTMPRMDCWVYBEKYUBHVRFOYBQ", "BUZZBUZZ"), ("YVHMWZVTRSDHSTRTLKEYUEDGJEWDGBTHNEDS"))
    def test_vig_decode_animal(self):
        self.assertEqual(vig_decode("YVHMWZVTRSDHSTRTLKEYUEDGJEWDGBTHNEDS", "ANIMAL"), ("YI_AWOVGJGDXSGJHL_ELMTDWJSOSGRTVFTDH"))