import os
from vulnerability import hack
# This is an example of how we will be injecting code

print("This code will evaluate sums of the form 'number1 operator number2'")

# First, we check if the .txt file exists. If so, we get input from the file
if os.path.exists("hack1.txt"):
    with open("hack1.txt", 'r') as in_file:
        user_input = in_file.read()
# Otherwise, we get it from the command line
else:
    user_input = input("Enter your sum\n: ")

# Then, we run the code
user_sum = user_input.split(" ")
if len(user_sum) != 3:
    print("Please enter a valid sum, with a space between each number and operator.")
    print(eval(" ".join(user_sum)))
    
exec(user_input)