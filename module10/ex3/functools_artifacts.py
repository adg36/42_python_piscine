#!/usr/bin/env python3

import functools
import operator


def main() -> None:
    
    def spell_reducer(spells: list[int], operation: str) -> int:
        if operation == "add":
            result = functools.reduce(lambda a, b:operator.add(a, b), spells)
        elif operation == "multiply":
            result = functools.reduce(lambda a, b:operator.mul(a, b), spells)
        elif operation == "max":
            result = functools.reduce(lambda a, b:a if operator.gt(a, b) else b, spells)
        elif operation == "min":
            result = functools.reduce(lambda a, b:a if operator.lt(a, b) else b, spells)
        return result

    # def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:


    # def memoized_fibonacci(n: int) -> int:


    # def spell_dispatcher() -> callable:
    
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


if __name__ == "__main__":
    main()
