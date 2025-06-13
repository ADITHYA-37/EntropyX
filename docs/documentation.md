# EntropyX – Detailed Code Documentation

This document provides a comprehensive technical overview of the core modules and logic used in EntropyX, a password strength checker and generator application built with Python and Tkinter.



## `backend/evaluator.py`

### `class PasswordEvaluator`

A class that evaluates password strength based on multiple criteria and returns a score along with user-friendly feedback.

#### Constructor:

```python
PasswordEvaluator(password: str)
```

* Ensures the input is a non-empty string.
* Initializes scoring and feedback mechanisms.

#### Methods:

* **`evaluate() -> Tuple[int, List[str]]`**
  Executes the full evaluation pipeline and returns a normalized score (0–100) along with feedback.

* **`_check_length()`**
  Adds score based on length; penalizes short passwords.

* **`_check_char_variety()`**
  Uses regular expressions to check for:

  * Uppercase letters
  * Lowercase letters
  * Digits
  * Special characters

* **`_check_entropy()`**
  Calculates entropy using the formula:
  `entropy = len(password) * log2(number_of_unique_characters)`

* **`_check_dictionary_word()`**
  Penalizes passwords found in the English dictionary using NLTK.

* **`_check_common_patterns()`**
  Identifies common weak patterns (e.g., "password", "123456").

* **`_normalize_score()`**
  Clamps the final score within the 0–100 range.



## `backend/generator.py`

### `class PasswordGenerator`

Generates secure random passwords based on configurable parameters.

#### Constructor:

```python
PasswordGenerator(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True)
```

* Accepts options for character types and password length.
* Validates that at least one character type is selected.

#### Method:

* **`generate() -> str`**

  * Constructs a character set from selected types.
  * Ensures representation from each type.
  * Shuffles and returns a secure password using `SystemRandom`.



## `frontend/app.py`

### `class EntropyXApp`

Controls the GUI for EntropyX using the Tkinter library.

#### Constructor:

```python
EntropyXApp(root: tk.Tk)
```

* Sets up the main application window.
* Initializes the password checker and generator UI elements.

#### Key Methods:

* **`_load_logo()`**
  Loads and displays the logo image from the `assets/` directory.

* **`_build_password_checker_ui()`**
  Creates the interface for password input, evaluation, score display, and feedback.

* **`_build_password_generator_ui()`**
  Builds the interface to generate passwords based on user-selected criteria.

* **`toggle_password_visibility()`**
  Toggles the password input between masked and plain text.

* **`check_password_strength()`**
  Uses the evaluator to compute strength and display feedback.

* **`generate_password()`**
  Generates a password using the selected options and displays it.

* **`copy_to_clipboard()`**
  Copies the generated password to the clipboard.



## `tests/` Directory

This folder contains unit and integration tests that verify functionality of the backend modules and ensure system reliability.



### `test_evaluator.py`

Tests for `PasswordEvaluator`.

#### Covered Cases:

* Empty input
* Short and weak passwords
* Strong passwords
* Missing character types



### `test_generator.py`

Tests for `PasswordGenerator`.

#### Covered Cases:

* Default password generation
* Custom length settings
* Error raised if no character type is enabled
* Character variety in generated passwords


### `test_integration.py`

Integration test that validates a generated password passes the evaluation logic with a strong score.



## Running the Tests

To run all tests:

```bash
python -m unittest discover tests/
```

Or with `pytest` (if installed):

```bash
pytest tests/
```



## Developer Notes

* GUI logic is separated from backend logic for testability.
* Password logic is modular, allowing future enhancements like breach checking.
* The application uses secure methods and is safe for educational or personal use.
* Feedback and scoring are aligned with basic principles of password entropy.
