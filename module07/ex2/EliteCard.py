# multiple inheritance implementation

from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int,
                 rarity: str, damage: int, combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type

    def play(self, game_state: dict) -> Dict[str, Any]:
        pass

    def attack(self, target: str) -> Dict[str, Any]:
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
        pass

    def cast_spell(self, spell_name: str, targets: list) -> Dict[str, Any]:
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
        pass
