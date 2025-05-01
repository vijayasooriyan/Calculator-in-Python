# Console-Based Calculator in Python

#### Video Demo: https://youtu.be/DqBwR9K81Og
#### Description:

This project is a **console-based calculator** built using **Python**, intended as a final project submission for the CS50x course. It demonstrates basic user interaction through a command-line menu and implements core arithmetic operations: addition, subtraction, multiplication, and division.

---

## Project Overview

The calculator is entirely text-based and is run from the terminal. When executed, it displays a menu with five options. Users can perform one of the following operations:

1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
5. Exit the program

Once the user selects an option, the program prompts for the required inputs (two numbers), performs the corresponding arithmetic operation, displays the result, and returns to the main menu. If the user chooses to divide and the second number is zero, a custom error message is shown ("Divide by zero Error!") instead of crashing the program.

The program continues running in a loop until the user chooses to exit.

---

## Files in the Project

### `project.py`
This is the main program file that contains:

- `menu()`: Displays the main menu and handles user input.
- `add()`, `sub()`, `mul()`, `div()`: Functions for performing the four operations. Each function receives two floating-point inputs from the user, calculates the result, and prints it to the console.
- A check to exit the program using `sys.exit()` with appropriate messages based on user input.

### `test_project.py`
This file includes unit tests for the calculator functions. While the original calculator relies on user input, the test file simulates logic verification through Python's assert statements.

The tests included are:

- `test_add()`: Verifies the correctness of addition.
- `test_sub()`: Verifies the correctness of subtraction.
- `test_mul()`: Verifies the correctness of multiplication.
- `test_div()`: Verifies the correctness of division and includes a test for `ZeroDivisionError` using `pytest.raises`.

Note: The testing does not call the actual `add()`, `sub()`, etc., from the main code due to their interactive nature, but rather verifies the underlying arithmetic logic separately.

---

## Design Decisions

### Recursion for Menu Looping
One notable design choice is the use of recursion—each arithmetic function calls the `menu()` again after completing its operation. This keeps the program running until the user exits. While a loop could have been used, recursion helps keep the logic segmented and clean for a small-scale project.

### Error Handling
A simple but important error-handling mechanism is included in the `div()` function to prevent the classic divide-by-zero crash. Instead of raising an exception, the program gracefully notifies the user and continues running.

### Separation of Concerns
Although the tests are not deeply integrated with the functions (since the calculator functions require `input()`), the separation of the testing logic demonstrates an understanding of how to validate core functionalities logically.

---

## Possible Improvements

- **Refactor for testability**: Modify the calculator functions to accept parameters instead of relying on user input so they can be directly tested.
- **Loop-based menu**: Replace recursion with a `while` loop to manage memory more efficiently.
- **Advanced features**: Add support for more operations like power, modulus, square root, or even a GUI interface using Tkinter.

---

## Conclusion

This calculator project showcases a simple but effective implementation of user interaction, logic, and control flow in Python. It meets the requirements for interactivity, functionality, testing, and documentation as set by the CS50 project specification. The program could be a stepping stone to more complex projects such as graphical calculators, web apps, or even command-line financial tools.

