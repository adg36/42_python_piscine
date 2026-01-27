#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int):
        """This function initializes the class."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Makes plant grow."""
        self.height += 1

    def get_older(self):
        """Makes plant age."""
        self.age += 1


def get_info():
    """Gets and prints information on my plants."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    days = 8
    for plant in plants:
        initial_height = plant.height
        for day in range(1, days):
            if day == 1 or day == 7:
                print(f"=== Day {day} ===\n"
                      f"{plant.name}: {plant.height}cm, {plant.age} days old")
            final_height = plant.height
            plant.grow()
            plant.get_older()
        growth = final_height - initial_height
        print(f"Growth this week: +{growth}cm\n")


def main():
    get_info()


if __name__ == "__main__":
    main()
