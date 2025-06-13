import unittest
from backend.generator import PasswordGenerator
from backend.evaluator import PasswordEvaluator

class TestIntegration(unittest.TestCase):

    def test_generated_password_is_strong(self):
        gen = PasswordGenerator(length=20)
        pwd = gen.generate()
        evaluator = PasswordEvaluator(pwd)
        score, _ = evaluator.evaluate()
        self.assertGreaterEqual(score, 70)

if __name__ == "__main__":
    unittest.main()
