def record_spell(spell_name: str, ingredients: str) -> str:
    """Try to record a spell using ingredients."""
    from alchemy.grimoire.validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    else:
        return f"Spell rejected: {spell_name} ({validation})"
