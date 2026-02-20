#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """This function initializes the class."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Makes plant grow."""
        self.height += 1

    def get_older(self) -> None:
        """Makes plant age."""
        self.age += 1

    def get_info(self) -> None:
        """Gets and prints information on my plants."""
        days = 8
        initial_height = self.height
        for day in range(1, days):
            if day in (1, 7):
                print(f"=== Day {day} ===\n"
                      f"{self.name}: {self.height}cm, {self.age} days old")
            final_height = self.height
            self.grow()
            self.get_older()
        growth = final_height - initial_height
        print(f"Growth this week: +{growth}cm\n")


def main() -> None:
    """This is the main function."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    for plant in plants:
        plant.get_info()


if __name__ == "__main__":
    main()
