#!/usr/bin/env python3

class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """This function initialises the class."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A blueprint to represent flowers."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """The flower's ability to bloom."""
        print(self.name, "is blooming beautifully!\n")


class Tree(Plant):
    """A blueprint to represent trees."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """The tree's ability to produce shade."""
        print(self.name, "provides", self.trunk_diameter + 28,
              "square meters of shade\n")


class Vegetable(Plant):
    """A blueprint to represent vegetables."""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def ft_plant_types() -> None:
    """Create instances of plant types."""
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 35, 14, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Birch", 300, 2543, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    pumpkin = Vegetable("Pumpkin", 30, 100, "autumn harvest", "vitamin A")
    flowers = [rose, tulip]
    trees = [oak, pine]
    vegetables = [tomato, pumpkin]
    print("=== Garden Plant Types ===\n")
    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, "
              f"{flower.age} days, {flower.color} color")
        flower.bloom()
    for tree in trees:
        print(f"{tree.name} (Tree): {tree.height}cm, "
              f"{tree.age} days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade()
    for veg in vegetables:
        print(f"{veg.name} (Vegetable): {veg.height}cm, "
              f"{veg.age} days, {veg.harvest_season}\n"
              f"{veg.name} is rich in {veg.nutritional_value}\n")


def main() -> None:
    """This is the main function."""
    ft_plant_types()


if __name__ == "__main__":
    main()
