import os
from vulnerability import hack

def login(username):
    users = ['Nkoli', 'Hyperion', 'Ori', 'Tony']
    if username in users:
        return f"Welcome, {username}."
    else:
        return ""

print("This code will log a username in")

# First, we check if the .txt file exists. If so, we get input from the file
if os.path.exists("hack3.txt"):
    with open("hack3.txt", 'r') as in_file:
        user_input = in_file.read()
        print(eval(user_input))

# Otherwise, we get it from the command line
else:
    user_input = input("Enter your username\n: ")

# Then, we run the code
print(eval(f"login('{user_input}')"))