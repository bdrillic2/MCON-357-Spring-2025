# implement factorial_recursive method
def factorial_recursive(number):
    # Base Case: If the number is 0 or 1, return 1
    if number == 0 or number == 1:
        return 1

    # Recursive Case: number * factorial of (number - 1)
    return number * factorial_recursive(number - 1)


def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
    if number < 0:
        print("Error: You must enter a non-negative integer.")
        return

    # Call factorial_recursive method
    result = factorial_recursive(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
