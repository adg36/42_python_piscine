#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if temp < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        elif 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp


def test_temperature_input() -> None:
    inputs = ["25", "abc", "100", "-50"]
    for i in inputs:
        check_temperature(i)
    print("All tests completed - program didn't crash!")


def ft_first_exception() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()


def main():
    ft_first_exception()


if __name__ == "__main__":
    main()
