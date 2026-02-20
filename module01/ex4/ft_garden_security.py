#!/usr/bin/env python3

class SecurePlant:
    """This class creates plant objects with protected data."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """This function initializes the class."""
        self.name = name
        self.height = 0
        self.age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set the plant's height."""
        if height >= 0:
            self.height = height
        else:
            print(f"Invalid operation attempted: "
                  f"height {height}cm [REJECTED]\n"
                  f"Security: Negative height rejected\n")

    def set_age(self, age: int) -> None:
        """Set the plant's age."""
        if age >= 0:
            self.age = age
        else:
            print(f"Invalid operation attempted: "
                  f"age {age} days [REJECTED]\n"
                  f"Security: Negative age rejected\n")

    def get_height(self) -> int:
        """Get the plant's height."""
        return self.height

    def get_age(self) -> int:
        """Get the plant's age."""
        return self.age


def ft_garden_security() -> None:
    """Create plants safely and print relevant information."""
    rose = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===\n"
          f"Plant created: {rose.name}\n"
          f"Height updated: {rose.get_height()}cm [OK]\n"
          f"Age updated: {rose.get_age()} days [OK]\n")
    rose.set_height(-5)
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


def main() -> None:
    """This is the main function."""
    ft_garden_security()


if __name__ == "__main__":
    main()
