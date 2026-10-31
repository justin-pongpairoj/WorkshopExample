"""
main.py
Entry point for the Scientific Calculator. Run this file to start the
program: `python main.py`
"""

import ui


def main():
    print("Welcome to the Scientific Calculator!")

    while True:
        print(ui.MENU)
        raw_choice = input("Choose an operation (0-12): ").strip()

        if not raw_choice.isdigit():
            print("Please enter a number from the menu.\n")
            continue

        choice = int(raw_choice)

        if choice == 0:
            print("Goobye, thanks for using the Scientific Calculator!")
            break

        if choice not in range(1, 13):
            print("Invalid choice. Try again.\n")
            continue

        x = ui.get_number("Enter a number: ")
        y = None
        if choice not in ui.SINGLE_INPUT_OPS:
            y = ui.get_number("Enter another number: ")

        try:
            result = ui.run_operation(choice, x, y)
            print(f"\nResult: {result}\n")
        except ValueError as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
