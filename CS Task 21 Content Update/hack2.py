import os
from vulnerability import hack

print("This code reads in a number and adds 1 to it")

# First, we check if the .txt file exists. If so, we get input from the file
if os.path.exists("hack2.txt"):
    with open("hack2.txt", 'r') as in_file:
        user_input = in_file.read()
# Otherwise, we get it from the command line
else:
    user_input = input("Enter your number\n: ")

# Then, we run the code
print(eval(f'{user_input} + 1'))