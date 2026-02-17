# instant magic effects

from enum import Enum
from ex0.Card import Card
from typing import Any, Dict


class SpellCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.SPELL.value

    def play(self, game_state: dict) -> Dict[str, Any]:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f'Deal {self.cost} {self.effect_type} to target'
            }
        else:
            return {
                    'card_played': self.name,
                    'mana_used': 0,
                    'effect': 'Not enough mana'
            }

    def resolve_effect(self, targets: list) -> Dict[str, Any]:
        return {
                'card': self.name,
                'effect_type': self.effect_type,
                'results': [
                    {'target': target,
                     'effect': f'{self.effect_type} '
                     'applied with strength {self.cost}'}
                    for target in targets
                ]
        }


class CardType(Enum):
    SPELL = "Spell"
