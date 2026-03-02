#!/usr/bin/env python3


def main() -> None:
    
    def mage_counter() -> callable:
        total = 0
        def counter():
            nonlocal total
            total += 1
            return total
        return counter

    def spell_accumulator(initial_power: int) -> callable:
        total = initial_power
        def new_total_power(power: int):
            nonlocal total
            total += power
            return total
        return new_total_power

    def enchantment_factory(enchantment_type: str) -> callable:


   # def memory_vault() -> dict[str, callable]:

    print("\nTesting mage counter...")

    counter = mage_counter()
    
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")

    new_total_power = spell_accumulator(53)

    print(f"Initial power is 53. "
          f"New total power is {new_total_power(8)}")


if __name__ == "__main__":
    main()
