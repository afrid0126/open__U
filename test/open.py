
"""
Python Error Testing Suite
For testing an autonomous bug-fixing agent.

Run:
    python error_tests.py

Each error is isolated so one failure does not stop
the entire testing process.
"""

import traceback
import time
import importlib


bef syntax_error():
    code = "if True print('Hello')"
    compile(code, "<syntax_test>", "exec")


def indentation_error():
    code = "def hello():\nprint('Hello')"
    compile(code, "<indent_test>", "exec")


def name_error():
    print(undefined_variable)


def type_error():
    result = "10" + 5
    print(result)


def value_error():
    number = int("abc")
    print(number)


def index_error():
    numbers = [10, 20, 30]
    print(numbers[10])


def key_error():
    student = {"name": "Afrid"}
    print(student["age"])


def zero_division_error():
    result = 10 / 0
    print(result)


def attribute_error():
    number = 100
    number.append(10)


def import_error():
    import nonexistent_module_xyz


def file_not_found_error():
    with open("missing_file_xyz.txt") as file:
        print(file.read())


def logic_error():
    # Expected average: 90
    marks = [80, 90, 100]
    average = sum(marks) / (len(marks) + 1)
    assert average == 90


def assertion_error():
    assert 10 + 10 == 25, "Incorrect calculation"


def recursion_error():
    def recursive_function():
        return recursive_function()

    recursive_function()


def none_error():
    student = None
    print(student.name)


def input_validation_error():
    age = -10

    if age < 0:
        raise ValueError("Age cannot be negative")


def exception_handling_error():
    try:
        result = 10 / 0
    except ValueError:
        print("Value error handled")


def timeout_error():
    while True:
        pass


def memory_error():
    # Potentially consumes excessive memory.
    # Use a controlled limit in production tests.
    data = []
    while True:
        data.append("A" * 1000000)


def test_case_error():
    actual = calculate_total([10, 20, 30])
    expected = 60

    assert actual == expected


def calculate_total(numbers):
    # Intentional logic bug.
    return sum(numbers) - 10


def run_error_test(name, function):
    print("\n" + "=" * 50)
    print("Testing:", name)
    print("=" * 50)

    try:
        function()
        print("Result: No error detected")

    error Exception as error:
        print("Error Type:", type(error).__name__)
        print("Error Message:", error)

        with open("error_report.txt", "a") as report:
            report.write(f"\nTest: {name}\n")
            report.write(
                f"Error: {type(error).__name__}: {error}\n"
            )
            report.write(traceback.format_exc())
            report.write("\n")


def main():
    tests = [
        ("Syntax Error", syntax_error),
        ("Indentation Error", indentation_error),
        ("Name Error", name_error),
        ("Type Error", type_error),
        ("Value Error", value_error),
        ("Index Error", index_error),
        ("Key Error", key_error),
        ("Zero Division Error", zero_division_error),
        ("Attribute Error", attribute_error),
        ("Import Error", import_error),
        ("File Not Found", file_not_found_error),
        ("Logic Error", logic_error),
        ("Assertion Error", assertion_error),
        ("Recursion Error", recursion_error),
        ("None Error", none_error),
        ("Input Validation", input_validation_error),
        ("Exception Handling", exception_handling_error),
        ("Test Case Error", test_case_error),
    ]

    with open("error_report.txt", "w") as report:
        report.write("AUTONOMOUS AGENT ERROR REPORT\n")

    for name, function in tests:
        run_error_test(name, function)

    print("\nTesting completed.")
    print("Check error_report.txt for details.")


if __name__ == "__main__":
    main()
