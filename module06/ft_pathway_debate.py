#!/usr/bin/env python3

from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life


def ft_pathway_debate() -> None:
    print("=== Pathway Debate Mastery ===")

    # absolute
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    # relative
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    # package access
    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): {lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


def main() -> None:
    ft_pathway_debate()


if __name__ == "__main__":
    main()
