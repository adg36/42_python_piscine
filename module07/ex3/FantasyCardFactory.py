from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.total_created = 0

    # creates fantasy themed creatures
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if type(name_or_power) is str:
            self.total_created += 1
            return CreatureCard(name_or_power, 5, "Legendary", 7, 5)
        elif type(name_or_power) is int:
            self.total_created += 1
            return CreatureCard(
                    "Goblin Warrior", name_or_power,
                    "Legendary", 7, 5)
        else:
            self.total_created += 1
            return CreatureCard("Fire Dragon", 5, "Legendary", 2, 7)

    # creates elemental spells
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if type(name_or_power) is str:
            self.total_created += 1
            return SpellCard(name_or_power, 3, "Common", "damage")
        elif type(name_or_power) is int:
            self.total_created += 1
            return SpellCard(
                    "Lightning Bolt", name_or_power,
                    "Common", "damage")
        else:
            self.total_created += 1
            return SpellCard("Lightning Bolt", 3, "Common", "damage")

    # creates magical artifacts
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if type(name_or_power) is str:
            self.total_created += 1
            return ArtifactCard(name_or_power, 2, "Rare", 1, "Permanent")
        elif type(name_or_power) is int:
            self.total_created += 1
            return ArtifactCard(
                    "Mana Crystal", name_or_power,
                    "Rare", 1, "Permanent")
        else:
            self.total_created += 1
            return ArtifactCard("Mana Crystal", 2, "Rare", 1, "Permanent")

    # creates themed deck
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        pass

    def get_supported_types(self) -> Dict[str, Any]:
        return {
                'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']
        }
