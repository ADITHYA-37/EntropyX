import unittest
from backend.generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        gen = PasswordGenerator()
        pwd = gen.generate()
        self.assertEqual(len(pwd), 16)

    def test_custom_length(self):
        gen = PasswordGenerator(length=32)
        pwd = gen.generate()
        self.assertEqual(len(pwd), 32)

    def test_no_charset_selected(self):
        with self.assertRaises(ValueError):
            PasswordGenerator(use_upper=False, use_lower=False, use_digits=False, use_special=False).generate()

    def test_generated_password_has_variety(self):
        gen = PasswordGenerator(length=16)
        pwd = gen.generate()
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;':,./<>?" for c in pwd))

if __name__ == "__main__":
    unittest.main()
