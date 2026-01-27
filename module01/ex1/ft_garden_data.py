#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int):
        """This function initialises the class."""
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    """Prints plant data."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===\n")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def main():
    ft_garden_data()


if __name__ == "__main__":
    main()
