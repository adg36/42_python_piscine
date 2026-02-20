from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if card_name in self.cards:
            self.cards.remove(card_name)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards[0]

    def get_deck_stats(self) -> dict:

        creatures = sum(
                1 for card in self.cards
                if isinstance(card, CreatureCard))
        spells = sum(
                1 for card in self.cards
                if isinstance(card, SpellCard))
        artifacts = sum(
                1 for card in self.cards
                if isinstance(card, ArtifactCard))
        total_cost = sum(card.cost for card in self.cards)
        avg_cost = round(total_cost / len(self.cards), 1)

        return {
                'total_cards': len(self.cards),
                'creatures': creatures,
                'spells': spells,
                'artifacts': artifacts,
                'avg_cost': avg_cost
        }
