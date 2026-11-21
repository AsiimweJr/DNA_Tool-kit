"""Basic Calculator Program: addition, subtraction, multiplication, division.
Type 5 or q at the menu, or q at any number prompt, to quit."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def get_number(prompt):
    """Ask for a number. Returns None if the user types q to quit."""
    while True:
        text = input(prompt).strip().lower()
        if text == "q":
            return None
        try:
            return float(text)
        except ValueError:
            print("That is not a number, try again (or type q to quit).")


def main():
    print("=== BASIC CALCULATOR ===")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit (or type q)")

        choice = input("Enter choice (1-5): ").strip().lower()

        if choice in ("5", "q"):
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter 1 to 5.")
            continue

        num1 = get_number("Enter first number (q to quit): ")
        if num1 is None:
            break
        num2 = get_number("Enter second number (q to quit): ")
        if num2 is None:
            break

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        else:
            result = divide(num1, num2)
            symbol = "/"

        print(f"\n{num1} {symbol} {num2} = {result}")

    print("Goodbye!")


main()
