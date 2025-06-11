from backend import PasswordEvaluator 

evaluator = PasswordEvaluator("")
score, feedback = evaluator.evaluate()

print(f"Score: {score}")
print("Feedback:")
for item in feedback:
    print("-", item)
