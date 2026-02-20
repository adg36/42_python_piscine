#!/usr/bin/env python3

from alchemy.grimoire import validate_ingredients, record_spell

def ft_circular_curse() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

    print("\nCircular dependency curse avoided using late imports!"
          "\nAll spells processed safely!")
def main() -> None:
    ft_circular_curse()

if __name__ == "__main__":
    main()
