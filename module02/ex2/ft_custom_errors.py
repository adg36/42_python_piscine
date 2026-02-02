#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "A garden problem occurred!") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    print("\nTesting PlantError...")
    raise PlantError()


def test_water_error() -> None:
    print("\nTesting WaterError...")
    raise WaterError()


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        test_plant_error()
    except PlantError as e:
        print("Caught PlantError:", e)
    try:
        test_water_error()
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")
    errors = [PlantError(), WaterError()]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


def main() -> None:
    ft_custom_errors()


if __name__ == "__main__":
    main()
