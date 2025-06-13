import unittest
from backend.evaluator import PasswordEvaluator

class TestPasswordEvaluator(unittest.TestCase):

    def test_empty_password(self):
        evaluator = PasswordEvaluator("")
        score, feedback = evaluator.evaluate()
        self.assertEqual(score, 0)
        self.assertTrue(any("empty" in f.lower() for f in feedback))

    def test_short_password(self):
        evaluator = PasswordEvaluator("abc")
        score, feedback = evaluator.evaluate()
        self.assertLess(score, 40)
        self.assertIn("too short", " ".join(feedback).lower())

    def test_strong_password(self):
        evaluator = PasswordEvaluator("S3cure!P@ssword2025")
        score, feedback = evaluator.evaluate()
        self.assertGreaterEqual(score, 80)

    def test_character_feedback(self):
        evaluator = PasswordEvaluator("onlylower")
        _, feedback = evaluator.evaluate()
        self.assertTrue(any("uppercase" in f.lower() or "digits" in f.lower() for f in feedback))

if __name__ == "__main__":
    unittest.main()
