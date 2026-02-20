from ex4.TournamentCard import TournamentCard
from typing import Any, Dict, List
import random


class TournamentPlatform:
    cards = {}

    def __init__(self) -> None:
        self.total_cards = 0
        self.matches_played = 0
        self.avg_rating = 0
        self.status = 'active'

    def register_card(self, card: TournamentCard) -> str:
        self.total_cards += 1
        self.cards[card.card_id] = card
        self.avg_rating += ((self.avg_rating + card.rating) / self.total_cards)
        bases = TournamentCard.__bases__
        interfaces = [cls.__name__ for cls in bases]
        return (f"{card.name} (ID: {card.card_id}):\n"
                f"- Interfaces: {interfaces}\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.record}\n")        

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        self.matches_played += 1
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        winner = random.choice([card1, card2])
        loser = card2 if winner is card1 else card1
        winner.rating += 16
        winner.record = "1-0"
        loser.rating -= 16
        loser.record = "0-1"
        return {
                'winner': winner.card_id,
                'loser': loser.card_id,
                'winner_rating': winner.rating,
                'loser_rating': loser.rating
        }
    
    def get_leaderboard(self) -> List[Any]:
        sorted_ids = sorted(
                self.cards, reverse=True)
        return sorted_ids

    def generate_tournament_report(self) -> Dict[str, Any]:
        return {
            'total_cards': self.total_cards,
            'matches_played': self.matches_played,
            'avg_rating': self.avg_rating,
            'platform_status': self.status
        }
