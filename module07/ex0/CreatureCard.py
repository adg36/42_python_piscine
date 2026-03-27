from enum import Enum
from typing import Any, Dict
from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive.")

        self.attack = attack
        self.health = health
        self.type = CardType.CREATURE.value

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:

        if not self.is_playable(game_state["available_mana"]):
            return {
                'card_played': self.name,
                'mana_used': 0,
                'effect': 'Not enough mana'
            }

        game_state["available_mana"] -= self.cost
        game_state["battlefield"].append(self.name)

        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }

    def attack_target(self, target) -> Dict[str, Any]:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> Dict[str, Any]:

        info = super().get_card_info()

        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })

        return info


class CardType(Enum):
    CREATURE = "Creature"
