#!/usr/bin/env python3

def ft_garden_intro() -> None:
    """This function prints information about my plant."""
    name = "Rose"
    height = "25cm"
    age = "30 days"
    print("=== Welcome to My Garden ===\n"
          "Plant:", name,
          "\nHeight:", height,
          "\nAge:", age,
          "\n\n=== End of Program ===")


def main() -> None:
    """This is the main function."""
    ft_garden_intro()


if __name__ == "__main__":
    main()
