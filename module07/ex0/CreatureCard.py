from enum import Enum
from ex0.Card import Card
from typing import Any, Dict


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack > 0 and health > 0:
            self.attack = attack
            self.health = health
        else:
            raise ValueError("ERROR: "
                             "attack and health must be positive values.")
        self.type = CardType.CREATURE.value

    def play(self, game_state: dict) -> Dict[str, Any]:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            game_state["battlefield"].append(self.name)
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
        else:
            return {
                    'card_played': self.name,
                    'mana_used': 0,
                    'effect': 'Not enough mana'
            }

    def attack_target(self, target) -> Dict[str, Any]:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }


class CardType(Enum):
    CREATURE = "Creature"
