                         # Task 1: Calculate Factorial Using a Function

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))

        fact = factorial(num)

        if fact is None:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {fact}")

    except ValueError:
        print("Please enter a valid integer.")

                               # Task 2: Using the Math Module for Calculations

        import math

        if __name__ == "__main__":
            try:
                num = float(input("Enter a number: "))

                if num <= 0:
                    print("Please enter a number greater than 0 for log and square root.")
                else:
                    square_root = math.sqrt(num)
                    log_value = math.log(num)  # natural log (base e)
                    sine_value = math.sin(num)  # radians

                    print(f"Square root of {num} = {square_root}")
                    print(f"Natural logarithm (log e) of {num} = {log_value}")
                    print(f"Sine of {num} (in radians) = {sine_value}")

            except ValueError:
                print("Please enter a valid number.")
