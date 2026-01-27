#!/usr/bin/env python3

class GardenManager:
    """A class to manage gardens."""
    gardens = []

    def __init__(self) -> None:
        """This function initializes the class."""
        pass

    @classmethod
    def create_garden_network(cls, garden: "Garden") -> None:
        """Creates network of gardens."""
        cls.gardens.append(garden)

    @classmethod
    def print_manager_stats(cls) -> None:
        """Prints global statistics."""
        total_gardens = 0
        for garden in cls.gardens:
            total_gardens += 1
        scores = "Garden scores - "
        for i in range(total_gardens):
            if i == total_gardens - 1:
                scores += f"{cls.gardens[i].owner}: {cls.gardens[i].score}"
            else:
                scores += f"{cls.gardens[i].owner}: {cls.gardens[i].score}, "
        print(scores)
        print(f"Total gardens managed: {total_gardens}")

    class GardenStats:
        """An inner class to calculate and show garden statistics."""
        def __init__(self) -> None:
            """This function initializes the class."""
            pass

        @staticmethod
        def print_garden_stats(garden: "Garden") -> None:
            """A helper that calculates and prints statistics."""
            print(f"\n=== {garden.owner}'s Garden Report ===\n"
                  "Plants in garden:")
            for plant in garden.plants:
                print(f"- {plant.describe()}")
            total = 0
            regular = 0
            flowering = 0
            prize = 0
            validation_test = True
            for plant in garden.plants:
                if plant.validated_height is False:
                    validation_test = False
                total += 1
                category = plant.get_category()
                if category == "regular":
                    regular += 1
                elif category == "flowering":
                    flowering += 1
                elif category == "prize":
                    prize += 1
            print(f"\nPlants added: {total}, "
                  f"Total growth: {garden.total_growth}cm"
                  f"\nPlant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers")
            print(f"\nHeight validation test: {validation_test}")


class Garden:
    """A blueprint to represent gardens."""
    def __init__(self, owner: str, total_growth: int, score: int):
        """This function initializes the class."""
        self.owner = owner
        self.score = score
        self.total_growth = 0
        self.plants = []

    def add_plant(self, plant: "Plant") -> None:
        """Adds one plant to garden."""
        self.plants.append(plant)
        category = plant.get_category()
        if category == "prize":
            self.score += plant.points
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plants(self) -> None:
        """Makes plants grow."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1


class Plant:
    """A blueprint to represent plants."""
    def __init__(self, name: str, height: int) -> None:
        """This function initialises the class."""
        self.name = name
        self.height = 0
        self.validated_height = False
        self.set_height(height)

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """Check if height is not negative."""
        return height >= 0

    def set_height(self, height: int) -> None:
        """Set the plant's height."""
        if self.is_valid_height(height):
            self.height = height
            self.validated_height = True
        else:
            print(f"Invalid operation attempted: "
                  f"height {height}cm [REJECTED]\n"
                  f"Security: Negative height rejected\n")

    def get_height(self) -> int:
        """Get the plant's height."""
        return self.height

    def grow(self) -> None:
        """Makes plant grow."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_category(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    """A blueprint to represent flowers."""
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def describe(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def get_category(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    """A prize-winning flower."""
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def describe(self) -> str:
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming), "
                f"Prize points: {self.points}")

    def get_category(self) -> str:
        return "prize"


class Tree(Plant):
    """A blueprint to represent trees."""
    def __init__(self, name: str, height: int) -> None:
        super().__init__(name, height)


def ft_garden_analytics() -> None:
    """Displays garden statistics."""
    print("=== Garden Management System Demo ===\n")
    alices_garden = Garden("Alice", 0, 208)
    GardenManager.create_garden_network(alices_garden)
    bobs_garden = Garden("Bob", 0, 92)
    GardenManager.create_garden_network(bobs_garden)
    oak = Tree("Oak Tree", 100)
    alices_garden.add_plant(oak)
    rose = FloweringPlant("Rose", 25, "red")
    alices_garden.add_plant(rose)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alices_garden.add_plant(sunflower)
    alices_garden.grow_plants()
    stats = GardenManager.GardenStats()
    stats.print_garden_stats(alices_garden)
    GardenManager.print_manager_stats()


def main() -> None:
    ft_garden_analytics()


if __name__ == "__main__":
    main()
