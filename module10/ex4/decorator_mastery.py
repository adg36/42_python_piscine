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
            if args[-1] >= min_power:
                result = func(*args, **kwargs)
            else:
                result = "Insufficient power for this spell"
            print(result)
            return result
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for n in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying "
                          f"attempt {n} of {max_attempts} attempts")
                else:
                    return result
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper_repeat
    return decorator_repeat


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.isalnum():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        return f"Result: {fireball.__name__} cast!"
    fireball()

    print("\nTesting retry spell...")

    @retry_spell(3)
    def lightning_bolt(power: int, target: str) -> str:
        return f"Caused {power} points of damage to {target}"
    result = lightning_bolt()
    print(result)

    print("\nTesting MageGuild...")

    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("Joh#nna"))
    guild.cast_spell("Lightning", 15)
    guild.cast_spell("Lightning", 5)


if __name__ == "__main__":
    main()
