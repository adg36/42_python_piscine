# advanced potion recipes

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water

def healing_potion() -> str:
    fire_result = alchemy.elements.create_fire()
    water_result = alchemy.elements.create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"

def strength_potion() -> str:
    earth_result = alchemy.elements.create_earth()
    fire_result = alchemy.elements.create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"

def invisibility_potion() -> str:
    fire_result = alchemy.elements.create_fire()
    water_result = alchemy.elements.create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"
    return "Invisibility potion brewed with [air_result] and [water_result]"

def wisdom_potion() -> str:
    fire_result = alchemy.elements.create_fire()
    water_result = alchemy.elements.create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"
    return "Wisdom potion brewed with all elements: [all_four_results]"
