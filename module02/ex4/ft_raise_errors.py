#!/usr/bin/env python3


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         "is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         "is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("\nTesting good values...")
    print(check_plant_health("tomato", 3, 5))
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 3, 5))
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 5))
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(e)
    finally:
        print("\nAll error raising tests completed!")


def ft_raise_errors() -> None:
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()


def main() -> None:
    ft_raise_errors()


if __name__ == "__main__":
    main()
