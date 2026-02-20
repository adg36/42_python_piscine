from enum import Enum
from ex0.Card import Card
from typing import Any, Dict


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = CardType.ARTIFACT.value

    def play(self, game_state: dict) -> Dict[str, Any]:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect
            }
        else:
            return {
                    'card_played': self.name,
                    'mana_used': 0,
                    'effect': 'Not enough mana'
            }

    def activate_ability(self) -> Dict[str, Any]:
        return {
               'artifact': self.name,
               'effect': self.effect
        }


class CardType(Enum):
    ARTIFACT = "Artifact"
