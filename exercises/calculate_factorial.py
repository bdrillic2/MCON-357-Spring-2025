import sys

# implement factorial_recursive method
def factorial_recursive(number):

    # handle negative input
    if number < 0:
        raise ValueError("Negative numbers are not allowed")

    # handle non-integer input
    if not str(number).isdigit():
        raise ValueError("Number must be an integer")

    # Base Case: If the number is 0 or 1, return 1
    if number == 0 or number == 1:
        return 1

    # Recursive Case: number * factorial of (number - 1)
    return number * factorial_recursive(number - 1)


def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # Call factorial_recursive method
    result = factorial_recursive(number)
    print("The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
