#!/usr/bin/env python3

from typing import Callable


def main() -> None:

    def mage_counter() -> Callable:
        total = 0

        def counter():
            nonlocal total
            total += 1
            return total
        return counter

    def spell_accumulator(initial_power: int) -> Callable:
        total = initial_power

        def new_total_power(power: int):
            nonlocal total
            total += power
            return total
        return new_total_power

    def enchantment_factory(enchantment_type: str) -> Callable:
        def enchantment(item_name):
            return f"{enchantment_type} {item_name}"
        return enchantment

    def memory_vault() -> dict[str, Callable]:

        storage = {}

        def store(key, value):
            storage[key] = value

        def recall(key):
            return storage.get(key, "Memory not found")

        vault = {
                "store": store,
                "recall": recall
        }

        return vault

    print("\nTesting mage counter...")

    counter = mage_counter()

    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")

    new_total_power = spell_accumulator(53)

    print(f"Initial power is 53. "
          f"New total power is {new_total_power(8)}")

    print("\nTesting enchantment factory...")

    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    print(enchantment_factory("Frozen")("Shield"))

    print("\nTesting memory vault...")

    vault = memory_vault()
    vault["store"]("spell", 42)
    print(vault["recall"]("spell"))
    print(vault["recall"]("heal"))


if __name__ == "__main__":
    main()
