# from backend import PasswordEvaluator 

# evaluator = PasswordEvaluator("")
# score, feedback = evaluator.evaluate()

# print(f"Score: {score}")
# print("Feedback:")
# for item in feedback:
#     print("-", item)


from backend import PasswordGenerator

generator = PasswordGenerator(length=20, use_upper=True, use_lower=True, use_digits=True, use_special=True)
password = generator.generate()

print("Generated Password:", password)
