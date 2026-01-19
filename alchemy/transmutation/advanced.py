from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create philosopher's stone."""
    return (
        "Philosopher’s stone created using "
        + f"{lead_to_gold()} and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """Get elixir of life."""
    return "Elixir of life: eternal youth achieved!"
