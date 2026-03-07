#!/usr/bin/env python3

import functools
import operator


def main() -> None:

    def spell_reducer(spells: list[int], operation: str) -> int:
        if operation == "add":
            result = functools.reduce(lambda a, b: operator.add(a, b), spells)
        elif operation == "multiply":
            result = functools.reduce(lambda a, b: operator.mul(a, b), spells)
        elif operation == "max":
            result = (
                functools.reduce(
                    lambda a, b: a if operator.gt(a, b) else b, spells)
            )
        elif operation == "min":
            result = (
                functools.reduce(
                    lambda a, b: a if operator.lt(a, b) else b, spells)
            )
        return result

    def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
        elements = [
            ("fire_enchant", "fire"),
            ("ice_enchant", "ice"),
            ("lightning_enchant", "lightning")
        ]

        enchants = {}
        for name, elem in elements:
            enchants[name] = functools.partial(
                base_enchantment, 50, elem)
        return enchants

    @functools.lru_cache(maxsize=128)
    def memoized_fibonacci(n: int) -> int:
        if n < 2:
            return n
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)

    @functools.singledispatch
    def spell_dispatcher(): 
        print(f"{spell} launched with success")

    @spell_dispatcher.register(int)
    def _(spell):
        print(f"{spell} units of damage caused")

    @spell_dispatcher.register(str)
    def _(spell):
        print(f"{spell} enchantment completed")

    @spell_dispatcher.register(list)
    def _(spell):
        print(f"{spell} cast for spell in ")


    print("\nTesting spell reducer...")

    spell_powers = [24, 17, 39, 19, 41, 21]
    operations = [
        ("Sum", "add"),
        ("Product", "multiply"),
        ("Max", "max"),
        ("Min", "min")
    ]
    for name, operation in operations:
        result = spell_reducer(spell_powers, operation)
        print(f"{name}: {result}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power, element, target):
        print(f"{element} hits {target} with strenght of {power}")

    enchants = partial_enchanter(base_enchantment)
    enchants["fire_enchant"]("Evil Witch")

    print("\nTesting memoized fibonacci...")

    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")

    spell_dispatcher("Fire")
    spell_dispatcher(50)
    spell_dispatcher(["Heal", "Burn", "Levitate"])


if __name__ == "__main__":
    main()
