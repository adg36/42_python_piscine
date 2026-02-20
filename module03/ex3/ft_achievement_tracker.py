#!/usr/bin/env python3


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer",
               "speed_demon", "perfectionist"}
    print(f"Player alice achievements: {alice}\n"
          f"Player bob achievements: {bob}\n"
          f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}\n"
          f"Total unique achievements: {len(unique)}\n")

    common = alice.intersection(bob, charlie)
    alice_unique = alice.difference(bob, charlie)
    bob_unique = bob.difference(alice, charlie)
    charlie_unique = charlie.difference(alice, bob)
    rare = alice_unique.union(bob_unique, charlie_unique)
    print(f"Common to all players: {common}\n"
          f"Rare achievements (1 player): {rare}\n")

    # Alice vs Bob only, no Charlie!
    alice_bob_common = alice.intersection(bob)
    alice_only = alice.difference(bob)
    bob_only = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_bob_common}\n"
          f"Alice unique: {alice_only}\n"
          f"Bob unique: {bob_only}\n")


if __name__ == "__main__":
    ft_achievement_tracker()
