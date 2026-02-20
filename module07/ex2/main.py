from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")

    for parent in EliteCard.__bases__:
        methods = []
        for key in parent.__dict__.keys():
            if not key.startswith("_"):
                methods.append(key)
        print(f"- {parent.__name__}: {methods}")

    # create Elite Card
    elite_card = EliteCard("Arcane Warrior", 4, "Ultra-Rare", "melee")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombate phase:")
    attack_result = elite_card.attack("Enemy")
    print(f"Attack result: {attack_result}")
    defense_result = elite_card.defend(2)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    cast_spell = elite_card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {cast_spell}")
    channel_mana = elite_card.channel_mana(3)
    print(f"Mana channel: {channel_mana}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
