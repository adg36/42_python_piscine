#!/usr/bin/env python3

def main() -> None:

    def spell_combiner(spell1: callable, spell2: callable) -> callable:
        def combined(*args, **kwargs):
            r1 = spell1(*args, **kwargs)
            r2 = spell2(*args, **kwargs)
            return (r1, r2)
        return combined

    def power_amplifier(base_spell: callable, multipler: int) -> callable:

    def conditional_caster(condition: callable, spell: calable) -> callable:

    def spell_sequence(spells: list[callable]) -> callable:


if __name__ == "__main__":
    main()
