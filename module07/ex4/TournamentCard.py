from enum import Enum
from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 rating: int, record: str, card_id: str) -> None:
        super().__init__(name, cost, rarity)
        self.rating = rating
        self.record = "0-0"
        self.card_id = card_id

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

    def attack(self, target) -> Dict[str, Any]:
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

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> Dict[str, Any]:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> None:
        pass


class CardType(Enum):
    TOURNAMENT = "Tournament"
