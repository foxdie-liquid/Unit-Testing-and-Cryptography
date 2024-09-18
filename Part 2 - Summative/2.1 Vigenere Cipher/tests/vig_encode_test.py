from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):
    def test_vig_encode_normal(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", "TEST"), "LLWIMMUCUVFOFJFPBYDHXHFNXVK_XPSRQHFZ")
    def test_vig_encode_yttrium(self):
        self.assertEqual(vig_encode("LLWIMMUCUVFOFJFPBYDHXHFNXVK_XPSRQHFZ", "YTTRIUM"), "IDOZUFF_MNWWZVCHUOLAIEYFNCDLUHKHYARW")
    def test_vig_encode_cobalt(self):
        self.assertEqual(vig_encode("IDOZUFF_MNWWZVCHUOLAIEYFNCDLUHKHYARW", "COBALT"), "KRPZEYHNNNGOAIDHEGNOJEIYPQELE_MVZABO")
    def test_vig_encode_molybdenum(self):
        self.assertEqual(vig_encode("KRPZEYHNNNGOAIDHEGNOJEIYPQELE_MVZABO", "MOLYBDENUM"), "WE_WFAL_GZSBLFEKITG_VSTVQTIYYLYIJYCR")
    def test_vig_encode_helium(self):
        self.assertEqual(vig_encode("WE_WFAL_GZSBLFEKITG_VSTVQTIYYLYIJYCR", "HELIUM"), "CIKDZMSDRGLNSJPSBENDF_MGXXTFRXEMUFWC")