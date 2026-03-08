#!/usr/bin/env python3

from typing import Callable


def main() -> None:
    def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
        def combined(*args, **kwargs):
            r1 = spell1(*args, **kwargs)
            r2 = spell2(*args, **kwargs)
            return (r1, r2)
        return combined

    def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
        def mega_spell(*args, **kwargs):
            result = base_spell(*args, **kwargs) * multiplier
            return result
        return mega_spell

    def conditional_caster(condition: Callable, spell: Callable) -> Callable:
        def conditional_spell(*args, **kwargs):
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        return conditional_spell

    def spell_sequence(spells: list[Callable]) -> Callable:
        def cast_spells(*args, **kwargs):
            spell_results = []
            for spell in spells:
                result = spell(*args, **kwargs)
                spell_results.append(result)
            return spell_results
        return cast_spells

    print("\nTesting spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    fire_and_heal = combined('Dragon')
    print(f"{fire_and_heal[0]}, {fire_and_heal[1]}")

    print("\nTesting power amplifier...")

    def fireball(target: str) -> int:
        return 10

    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Dragon")
    amplified = mega_fireball("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")

    def is_alive(health: int) -> bool:
        if health > 0:
            return True
        return False

    def heal(health: int) -> int:
        while health < 5:
            health += 1
        return health

    heal_if_alive = conditional_caster(is_alive, heal)
    success = heal_if_alive(1)
    failure = heal_if_alive(-2)
    print(f"Success: Health level is now {success}. Failure: {failure}")

    print("\nTesting spell_sequence...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    spells = [fireball, heal]
    cast_spells = spell_sequence(spells)
    print(cast_spells("Dragon"))


if __name__ == "__main__":
    main()
