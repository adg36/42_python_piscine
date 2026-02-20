from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    
    platform = TournamentPlatform()

    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 1200, "0-0", "dragon_001")
    ice_wizard = TournamentCard("Ice Wizard", 7, "Rare", 1150, "0-0", "wizard_001")
    cards = (fire_dragon, ice_wizard)
    for card in cards:
        message = platform.register_card(card)
        print(message)

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    print(leaderboard)


if __name__ == "__main__":
    main()
