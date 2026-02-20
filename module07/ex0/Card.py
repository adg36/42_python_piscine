from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': getattr(self, 'type', None),
            'attack': getattr(self, 'attack', None),
            'health': getattr(self, 'health', None),
            'damage': getattr(self, 'damage', None),
            'combat_type': getattr(self, 'combat_type', None)
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana < self.cost:
            return False
        return True
