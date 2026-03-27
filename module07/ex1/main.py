from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    # define game state
    game_state = {
            'available_mana': 10,
            'battlefield': []
    }

    # create deck
    deck = Deck()

    # create cards
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell_card = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact_card = ArtifactCard(
            "Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn")

    # add cards to deck
    deck.add_card(creature_card)
    deck.add_card(spell_card)
    deck.add_card(artifact_card)

    # print deck stats
    print(f"Deck stats: {deck.get_deck_stats()}")

    # drawing and playing cards
    print("\nDrawing and playing cards:")

    for i in range(3):
        deck.shuffle()
        drawn_card = deck.draw_card()
        print(f"\nDrew: {drawn_card.name} ({drawn_card.type})")
        a_play = drawn_card.play(game_state)
        print(f"Play result: {a_play}")

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
