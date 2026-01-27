#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int):
        """This function initializes the class."""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory():
    """Creates plants."""
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    total = 0
    for plant in plants:
        print(f"Created: {plant.name}"
              f"({plant.height}cm, {plant.age} days)")
        total += 1
    print(f"\nTotal plants created: {total}")


def main():
    ft_plant_factory()


if __name__ == "__main__":
    main()
