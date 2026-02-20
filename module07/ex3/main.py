from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")

    game = GameEngine()
    factory = FantasyCardFactory()
    print(f"Factory: {type(factory).__name__}")

    strategy = AggressiveStrategy()
    print(f"Strategy: {type(strategy).__name__}")

    available_types = factory.get_supported_types()
    print(f"Available types: {available_types}")
    game.configure_engine(factory, strategy)

    battlefield = ["Enemy Player"]

    print("\nSimulating aggressive turn...")
    game.simulate_turn()
    hand = []
    for _ in range(5):
        card = factory.create_creature("Fire Dragon")
        hand.append(card)
    for _ in range(2):
        card = factory.create_creature("Goblin Warrior")
        hand.append(card)
    for _ in range(3):
        card = factory.create_creature("Lightning Bolt")
        hand.append(card)

    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]\n")

    print("Turn execution:")
    result = strategy.execute_turn(hand, battlefield)
    print(f"Strategy: {type(strategy).__name__}")
    print(f"Actions: {result}")

    creature_card = factory.create_creature(9)
    spell_card = factory.create_spell()
    artifact_card = factory.create_artifact()

    cards = [creature_card, spell_card, artifact_card]

    for card in cards:
        hand.append(card)

    print("\nGame Report:")
    game_report = game.get_engine_status()
    print(game_report)

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
