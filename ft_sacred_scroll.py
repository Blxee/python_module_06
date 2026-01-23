"""Module that demostrates direct module access vs package level access."""

import alchemy


def main():
    """Demonstrate __init__.py usage."""
    print("\n=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")

    # call the functions using direct module access.
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")

    # try to access the package level interface.
    print("alchemy.create_fire():", alchemy.create_fire())
    print("alchemy.create_water():", alchemy.create_water())

    # try to access hidden functions using the package level interface.
    try:
        print("alchemy.create_earth(): ", end="")
        alchemy.create_earth()
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_air(): ", end="")
        alchemy.create_air()
    except AttributeError:
        print("AttributeError - not exposed")

    # print the version and author of the alchemy package.
    version = alchemy.__version__
    author = alchemy.__author__
    print("\nPackage metadata:")
    print("Version:", version)
    print("Author:", author)


if __name__ == "__main__":
    main()
