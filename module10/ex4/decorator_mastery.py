#!/usr/bin/env python3

import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def func_timer():
        print(f"Casting {func.__name__}")
        start = time.time()
        result = func()
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        print(f"{result}")
        return result
    return func_timer


def power_validator(min_power: int) -> Callable:

    def validator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] >= min_power:
                result = func(*args, **kwargs)
            else:
                result = "Insufficient power for this spell"
            print(result)
            return result
        return wrapper
    return validator

# def retry_spell(max_attempts: int) -> Callable:


# class MageGuild:


# @staticmethod
# def validate_mage_name(name: str) -> bool:


# def cast_spell(self, spell_name: str, power: int) -> str:


def main() -> None:

    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        return f"Result: {fireball.__name__} cast!"
    fireball()

    print("\nTesting power validator...")

    @power_validator(10)
    def cast_spell(power, target):
        return f"Caused {power} points of damage to {target}"
    cast_spell(8, "Dragon")
    cast_spell(15, "Goblin")


if __name__ == "__main__":
    main()
