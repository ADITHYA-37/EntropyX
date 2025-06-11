import random
import string


class PasswordGenerator:
    """
    Generates a secure random password with customizable options for character sets.
    Uses SystemRandom for cryptographically secure randomness.
    """

    def __init__(self, length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
        if not isinstance(length, int) or length < 4:
            raise ValueError("Password length must be an integer and at least 4 characters.")
        
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self) -> str:
        """
        Generate a secure password based on the selected criteria.
        :return: A randomly generated password as a string.
        """
        charset = ''
        if self.use_upper:
            charset += string.ascii_uppercase
        if self.use_lower:
            charset += string.ascii_lowercase
        if self.use_digits:
            charset += string.digits
        if self.use_special:
            charset += string.punctuation

        if not charset:
            raise ValueError("At least one character type must be selected.")

        # Ensure at least one character from each selected group is included
        password = []
        secure_random = random.SystemRandom()

        if self.use_upper:
            password.append(secure_random.choice(string.ascii_uppercase))
        if self.use_lower:
            password.append(secure_random.choice(string.ascii_lowercase))
        if self.use_digits:
            password.append(secure_random.choice(string.digits))
        if self.use_special:
            password.append(secure_random.choice(string.punctuation))

        # Fill the rest of the password
        remaining_length = self.length - len(password)
        password += [secure_random.choice(charset) for _ in range(remaining_length)]

        # Shuffle to avoid predictable sequences
        secure_random.shuffle(password)
        return ''.join(password)
