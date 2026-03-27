from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    # define a game state
    game_state = {
            'available_mana': 6,
            'battlefield': []
    }

    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    new_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    info = new_card.get_card_info()
    print(info)

    # playing card
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {new_card.is_playable(6)}")
    print(f"Play result: {new_card.play(game_state)}")

    # attacking
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {new_card.attack_target('Goblin Warrior')}")

    # testing mana
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {new_card.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
