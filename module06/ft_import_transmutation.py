#!/usr/bin/env python3

# demonstration script

import alchemy.elements
from alchemy.potions import healing_potion as heal, strength_potion as strength
from alchemy.elements import create_fire, create_water

def ft_import_transmutation() -> None:
    print("=== Import Transmutation Mastery ===")
    
    # method 1
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    # method 2
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    # method 3
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")

    # method 4
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {alchemy.elements.create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength()}")

    print("\nAll import transmutation methods mastered!")

def main() -> None:
    ft_import_transmutation()


if __name__ == "__main__":
    main()
