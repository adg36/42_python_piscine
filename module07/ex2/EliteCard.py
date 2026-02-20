from enum import Enum
from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int,
                 rarity: str, combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.type = CardType.ELITE.value
        self.spells_cast = 0
        self.combats_fought = 0
        self.damage = random.randint(1, 12)

    def play(self, game_state: dict) -> Dict[str, Any]:
        if game_state["available_mana"] >= self.cost:
            game_state["available_mana"] -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'damage': self.damage
            }
        else:
            return {
                    'card_played': self.name,
                    'mana_used': 0,
                    'damage': 'Not enough mana'
            }

    def get_card_info(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.type,
            'damage': self.damage,
            'combat_type': self.combat_type,
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana < self.cost:
            return False
        return True

    def attack(self, target: str) -> Dict[str, Any]:
        self.combats_fought += 1
        return {
                'attacker': self.name,
                'target': target,
                'damage': self.damage,
                'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        return {
                'defender': self.name,
                'damage_taken': incoming_damage,
                'damage_blocked': self.damage - incoming_damage,
                'still_alive': (self.damage - incoming_damage) > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'combats_fought': self.combats_fought}

    def cast_spell(self, spell_name: str, targets: list) -> Dict[str, Any]:
        self.spells_cast += 1
        return {
                'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': self.cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        return {
                'channeled': amount,
                'total_mana': self.cost + amount
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'spells_cast': self.spells_cast}


class CardType(Enum):
    ELITE = "Elite"
