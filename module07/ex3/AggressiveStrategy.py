from typing import Any, Dict, List
from ex3.GameStrategy import GameStrategy
import random


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        playable_cards = hand.copy()

        playable_cards.sort(key=lambda c: getattr(c, 'cost', 0))

        for card in playable_cards:
            cards_played.append(card.name)
            mana_used += getattr(card, 'cost', 0)
            damage = getattr(card, 'damage', 0)
            damage = random.randint(1, damage) if damage > 0 else 0
            damage_dealt += damage
            targets_attacked = self.prioritize_targets(battlefield)

        targets_attacked = self.prioritize_targets(battlefield)

        return {
                'cards_played': cards_played,
                'mana_used': mana_used,
                'targets_attacked': targets_attacked,
                'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return type(self).__name__

    def prioritize_targets(self, available_targets: list) -> List[Any]:
        return sorted(
                available_targets,
                key=lambda t: getattr(t, "health", float("inf"))
        )
