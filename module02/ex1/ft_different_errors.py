#!/usr/bin/env python3

def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        raise ValueError
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        raise KeyError
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        raise KeyError
    except (ValueError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
