#!/usr/bin/env python3

import functools
import operator
from typing import Callable


def main() -> None:

    def spell_reducer(spells: list[int], operation: str) -> int:
        if operation == "add":
            result = functools.reduce(operator.add, spells)
        elif operation == "multiply":
            result = functools.reduce(operator.mul, spells)
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

    def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
        elements = [
            ("fire_enchant", "fire"),
            ("ice_enchant", "ice"),
            ("lightning_enchant", "lightning")
        ]

        enchants: dict[str, Callable] = {}
        for name, elem in elements:
            enchants[name] = functools.partial(
                base_enchantment, 50, elem)
        return enchants

    @functools.lru_cache(maxsize=128)
    def memoized_fibonacci(n: int) -> int:
        if n < 2:
            return n
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)

    def spell_dispatcher() -> Callable:

        @functools.singledispatch
        def dispatch(spell):
            print(f"{spell} launched with success")

        @dispatch.register(int)
        def _(spell):
            print(f"{spell} units of damage caused")

        @dispatch.register(str)
        def _(spell):
            print(f"{spell} enchantment completed")

        @dispatch.register(list)
        def _(spell):
            for item in spell:
                print(f"{item} cast")
        return dispatch

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

    dispatcher = spell_dispatcher()
    dispatcher("Fire")
    dispatcher(50)
    dispatcher(["Heal", "Levitate", "Burn"])


if __name__ == "__main__":
    main()
