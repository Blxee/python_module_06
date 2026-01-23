"""Module that demonstrates usage of different import styles."""


def main() -> None:
    """Demonstrate different import styles."""
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    # import the alchemy module directly.
    import alchemy

    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

    print("\nMethod 2 - Specific function import:")
    # import only a specific item from the alchemy module.
    from alchemy.elements import create_water

    print("create_water():", create_water())

    print("\nMethod 3 - Aliased import:")
    # import an item from the alchemy module aliased.
    from alchemy.potions import healing_potion as heal

    print("heal():", heal())

    print("\nMethod 4 - Multiple imports:")
    # import multiple items from the alchemy module.
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion

    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
