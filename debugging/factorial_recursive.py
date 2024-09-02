#!/usr/bin/python3
import sys  # Importing the sys module to work with command-line arguments

def factorial(n):
    # If n is 0, return 1 because the factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Otherwise, return n multiplied by the factorial of (n-1)
        # This is a recursive function call
        return n * factorial(n - 1)

# Convert the first command-line argument to an integer
# and store the result of the factorial function in 'f'
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)