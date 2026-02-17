from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):

    # creates fantasy themed creatures
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return CreatureCard()

    # creates elemental spells
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return SpellCard()

    # creates magical artifacts
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard()

    # creates themed deck
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        cards = [CreatureCard, SpellCard, ArtifactCard]
        deck = {}
        for i in range(int):
            card = random.choice(cards)
            if card not in deck:
                deck[card] = 1
            else:
                deck[card] += 1

    def get_supported_types(self) -> Dict[str, Any]:
        return {
                'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']
        }
