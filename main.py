# The code below is to check the PasswordEvaluator
# from backend import PasswordEvaluator

# evaluator = PasswordEvaluator("")
# score, feedback = evaluator.evaluate()

# print(f"Score: {score}")
# print("Feedback:")
# for item in feedback:
#     print("-", item)

# The code below is to check the PasswordGenerator
# from backend import PasswordGenerator

# generator = PasswordGenerator(length=20, use_upper=True, use_lower=True, use_digits=True, use_special=True)
# password = generator.generate()

# print("Generated Password:", password)

#The code is the main code to run the GUI

import tkinter as tk
from frontend import EntropyXApp

if __name__ == "__main__":
    root = tk.Tk()
    app = EntropyXApp(root)
    root.mainloop()