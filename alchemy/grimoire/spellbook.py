# resolve circular import by imoprting the module.
import alchemy.grimoire


def record_spell(spell_name: str, ingredients: str) -> str:
    """Try to record a spell using ingredients."""
    # resolve circular import using late import.
    from alchemy.grimoire.validator import validate_ingredients

    validation = alchemy.grimoire.validate_ingredients(ingredients)
    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    else:
        return f"Spell rejected: {spell_name} ({validation})"
