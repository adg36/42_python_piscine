# validates spell ingredients

def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    for ingredient in valid:
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
