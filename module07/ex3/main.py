#!/usr/bin/env python3

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

    game.configure_engine(factory, strategy)
    
    battlefield = []

    # create AggressiveStrategy
    print("Simulating aggressive turn...")
    hand = ["Fire Dragon (5)", "Goblin Warrior (2)", "Lightning Bolt (3)"]
    targets = ['Enemy Player']
    print(f"Hand: {hand}")
    result = strategy.execute_turn(hand, battlefield)
    print(f"Strategy: {type(strategy).__name__}")
    print(f"Actions: {result}")

    # print available types



if __name__ == "__main__":
    main()
