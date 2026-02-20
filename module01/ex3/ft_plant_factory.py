#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """This function initializes the class."""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    """Creates plants."""
    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    total = 0
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        print(f"Created: {plant.name} "
              f"({plant.height}cm, {plant.age} days)")
        total += 1
    print(f"\nTotal plants created: {total}")


def main() -> None:
    """This is the main function."""
    ft_plant_factory()


if __name__ == "__main__":
    main()
