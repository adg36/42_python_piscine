#!/usr/bin/env python3

class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant: str) -> None:
        if plant == "":
            raise ValueError("Error adding plant: "
                             "Plant name cannot be empty!")
        else:
            self.plants.append(plant)
        print(f"Added {plant} successfully")

    @staticmethod
    def water_plants(plant_list: list) -> None:
        print("Opening watering system")
        try:
            for plant in plant_list:
                if plant == "":
                    raise ValueError()
                else:
                    print(f"Watering {plant} - success")
        except ValueError:
            pass
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Error checking {plant_name}: "
                             f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Error checking {plant_name}: "
                             f"Water level {water_level} is too low (min 1)")
        if sunlight_hours < 2:
            raise ValueError(f"Error checking {plant_name}: "
                             f"Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error checking {plant_name}: "
                             f"sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
        return (f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})")


class GardenError(Exception):
    def __init__(self, message: str = "A garden problem occurred!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in tank") -> None:
        super().__init__(message)


def test_water_error() -> None:
    raise WaterError()


def test_garden_management() -> None:
    garden = GardenManager()
    plants_to_add = ["tomato", "lettuce", ""]
    print("\nAdding plants to garden...")
    for plant in plants_to_add:
        try:
            garden.add_plant(plant)
        except ValueError as e:
            print(e)
    plants_to_water = ["tomato", "lettuce"]
    print("\nWatering plants...")
    garden.water_plants(plants_to_water)
    print("\nChecking plant health...")
    try:
        print(garden.check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(e)
    try:
        print(garden.check_plant_health("lettuce", 15, 8))
    except ValueError as e:
        print(e)
    print("\nTesting error recovery...")
    try:
        test_water_error()
    except GardenError as e:
        print("Caught GardenError:", e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


def ft_garden_management() -> None:
    print("=== Garden Management System ===")
    test_garden_management()


def main() -> None:
    ft_garden_management()


if __name__ == "__main__":
    main()
