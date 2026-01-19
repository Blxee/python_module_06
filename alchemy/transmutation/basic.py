from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Lead transmuted using fire element."""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Lead transmuted using earth element."""
    return f"Stone transmuted to gem using {create_earth()}"
