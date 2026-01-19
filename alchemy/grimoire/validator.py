def validate_ingredients(ingredients: str) -> str:
    """Validate whether the ingredients are correct."""
    if not isinstance(ingredients, str):
        return ""

    possible_ingredients: set[str] = {"fire", "water", "earth", "air"}
    valid: str = "VALID"

    ingredients_list = ingredients.split()
    for i in ingredients_list:
        if i not in possible_ingredients:
            valid = "INVALID"
            break

    return f"{ingredients} - {valid}"
