from typing import Any, Dict, List


class AggressiveStrategy:

    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        return {
                'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
                'mana_used': 5,
                'targets_attacked': ['Enemy Player'],
                'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        return f"{type(AggressiveStrategy).__name__}"


    def prioritize_targets(self, available_targets: list) -> List[Any]:
        return [target for target in available_targets if 
