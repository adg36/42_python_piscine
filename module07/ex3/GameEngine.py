from typing import Any, Dict
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    
    def __init__(self) -> None:
        self.turns_simulated = 0
        self.total_damage = 0
        self.factory = None
        self.strategy = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        self.turns_simulated += 1
        hand = []  # can generate or play hand here
        return {
                'Hand': hand
        }

    def get_engine_status(self) -> Dict[str, Any]:
        return {
                'turns_simulated': self.turns_simulated,
                'strategy_used': (
                    self.strategy.__class__.__name__
                    if self.strategy else None
                ),
                'total_damage': self.total_damage,
                'cards_created': (
                    self.factory.total_created()
                    if self.factory else 0
                )
        }
