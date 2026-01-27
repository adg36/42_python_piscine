#!/usr/bin/env python3

def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        50 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        data = {}
        data["missing\\_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        data = {}
        int(data["missing\\_plant"])
    except (ValueError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
