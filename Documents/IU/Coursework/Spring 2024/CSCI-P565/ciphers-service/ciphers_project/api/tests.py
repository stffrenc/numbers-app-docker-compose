from django.test import TestCase
from .ciphers import ceasar_encode

# Create your tests here.

class CiphersTest(TestCase):
    def test_ceasar_encoding_1(self):
        plain_text = 'hello'
        shift = 1
        expected = 'ifmmp'
        output = ceasar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_ceasar_encoding_2(self):
        plain_text = 'winter'
        shift = 3
        expected = 'zlqwhu'
        output = ceasar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_ceaser_encoding_3(self):
        plain_text = 'xyz XYZ'
        shift = 3
        expected = 'abc ABC'
        output = ceasar_encode(plain_text, shift)
        self.assertEqual(expected, output)
        