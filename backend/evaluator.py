import math
import re
from typing import Tuple, List

#Dictionary check with nltk
try:
    from nltk.corpus import words
    import nltk
    nltk.download('words', quiet=True)
    ENGLISH_WORDS = set(words.words())
    NLTK_AVAILABLE = True
except Exception:
    ENGLISH_WORDS = set()
    NLTK_AVAILABLE = False


class PasswordEvaluator:
    """
    Evaluates password strength based on length, entropy, character variety,
    and optional dictionary word detection using NLTK.
    """

    def __init__(self, password: str):
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")
        self.password = password
        self.score = 0
        self.feedback: List[str] = []

    def evaluate(self) -> Tuple[int, List[str]]:
        """
        Run the full password evaluation and return a normalized score and feedback.
        :return: Tuple[int, List[str]]: (score out of 100, feedback list)
        """
        if not self.password:
            self.feedback.append("Password cannot be empty.")
            self.score = 0
            return self.score, self.feedback

        self._check_length()
        self._check_char_variety()
        self._check_entropy()
        self._check_dictionary_word()
        self._check_common_patterns()
        self._normalize_score()
        return self.score, self.feedback

    def _check_length(self):
        length = len(self.password)
        if length < 8:
            self.feedback.append("Password is too short (minimum 8 characters).")
        elif length < 12:
            self.score += 10
        elif length < 16:
            self.score += 20
        else:
            self.score += 30

    def _check_char_variety(self):
        patterns = {
            'uppercase': r'[A-Z]',
            'lowercase': r'[a-z]',
            'digits': r'\d',
            'special': r'[!@#$%^&*(),.?":{}|<>]'
        }

        variety_score = 0
        for name, regex in patterns.items():
            if re.search(regex, self.password):
                variety_score += 10
            else:
                self.feedback.append(f"Add more {name} characters.")

        self.score += variety_score

    def _check_entropy(self):
        unique_chars = len(set(self.password))
        if unique_chars == 0:
            return

        entropy = len(self.password) * math.log2(unique_chars)

        if entropy < 28:
            self.feedback.append("Very low entropy. Use more varied characters.")
        elif entropy < 50:
            self.score += 10
        elif entropy < 80:
            self.score += 20
        else:
            self.score += 30

    def _check_dictionary_word(self):
        if not NLTK_AVAILABLE or not ENGLISH_WORDS:
            self.feedback.append("Dictionary check skipped (nltk not available).")
            return

        if self.password.lower() in ENGLISH_WORDS:
            self.feedback.append("Password is a dictionary word. Use more randomness.")
            self.score -= 20

    def _check_common_patterns(self):
        weak_patterns = [
            r'^123456$', r'^password$', r'^admin$', r'^letmein$',
            r'password[0-9]*$', r'12345678$', r'qwerty$', r'111111$'
        ]

        for pattern in weak_patterns:
            if re.fullmatch(pattern, self.password.lower()):
                self.feedback.append("Password matches a known weak pattern.")
                self.score -= 25
                break

    def _normalize_score(self):
        # Clamp score between 0 and 100
        self.score = max(0, min(100, self.score))
