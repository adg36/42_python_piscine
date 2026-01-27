#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    errors = 0
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                errors = 1
                raise ValueError()
            else:
                print("Watering", plant)
    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    if errors == 0:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    good_plant_list = ["tomato", "lettuce", "carrots"]
    bad_plant_list = ["tomato", None]
    print("\nTesting normal watering...")
    water_plants(good_plant_list)
    print("\nTesting with error...")
    water_plants(bad_plant_list)
    print("\nCleanup always happens, even with errors!")


def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


def main() -> None:
    ft_finally_block()


if __name__ == "__main__":
    main()
