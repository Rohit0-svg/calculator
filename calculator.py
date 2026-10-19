# Menu-driven calculator


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(choice, x, y):
    if choice == "1":
        return x + y
    if choice == "2":
        return x - y
    if choice == "3":
        return x * y
    if choice == "4":
        if y == 0:
            return "Error: cannot divide by zero"
        return x / y


def main():
    print("-------------------- Hello There --------------------")
    while True:
        print("\n1 - Addition   2 - Subtraction   3 - Multiplication   4 - Division   5 - Exit")
        choice = input("Select here: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid option, please choose 1 to 5.")
            continue
        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")
        print("Your answer is", calculate(choice, x, y))


if __name__ == "__main__":
    main()
