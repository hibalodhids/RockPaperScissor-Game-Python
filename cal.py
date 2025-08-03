
import numpy as np
score = 0
total_question = 5

for i in range(total_question):
   num1 = np.random.randint(1,10)
   num2 = np.random.randint(1,10)
   operation = np.random.choice(['+', '-', '*', '/'])

   if operation == '+':
      sol = num1 + num2
   elif operation == '-':
      sol = num1 - num2
   elif operation == '*':
      sol = num1 * num2
   elif operation == '/':
      sol = num1 / num2

   try:
      user = input(f"Q{i+1}:What is {num1} {operation} {num2}?")

      if user == sol:
         print("Correct!")
         score += 1
      else:
         print("Wrong!")
   except ValueError:
      print("Invalid input! Please enter a number.")
      print(f"ypor total score:{score} out of total question:{total_question}")